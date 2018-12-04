var new_time_entry_sector_one   = '00:00:00';
var new_time_entry_sector_two   = '00:00:00';
var new_time_entry_sector_three = '00:00:00';
var new_time_entry_lap_time     = '00:00:00';

var new_time_entry_html_part_one    = '<div class="time_grid_entry new_lap_entry" id="';
var new_time_entry_html_part_two    = '"><div class="time_grid_data"><div class="lap_number"><span class="lap_number_text">';
var new_time_entry_html_part_three  = '</span></div><div class="sector_one"><span class="sector_one_text" id="';
var new_time_entry_html_part_four   = '_sector_one_text">';
var new_time_entry_html_part_five   = '</span></div><div class="sector_two"><span class="sector_two_text" id="';
var new_time_entry_html_part_six    = '_sector_two_text">';
var new_time_entry_html_part_seven  = '</span></div><div class="sector_three"><span class="sector_three_text" id="';
var new_time_entry_html_part_eight  = '_sector_three_text">';
var new_time_entry_html_part_nine   = '</span></div><div class="lap_time"><span class="lap_time_text" id="';
var new_time_entry_html_part_ten    = '_lap_time_text">';
var new_time_entry_html_part_eleven  = '</span></div></div></div>';

var current_lap = 0;

var one = current_lap.toString() + '_sector_one_text';
var two = current_lap.toString() + '_sector_two_text'
var three = current_lap.toString() + '_sector_three_text'
var four = current_lap.toString() + '_lap_time_text'

var current_time_entry_sector_one;
var current_time_entry_sector_two;
var current_time_entry_sector_three;
var current_time_entry_lap_time;

// zero if hasnt gone to pit, 1 if car has
var has_pitted = 0;

// Fastest lap
var fastest_lap_time = 0;
var fastest_lap_number = 0;

// Slowest lap
var slowest_lap_time = 0;
var slowest_lap_number = 0;

// Current lap time
var current_lap_time;


// Function to convert the time we are given in the UDP packets in seconds to a standard time format
function intTime_to_timeTime(time_str) {
  let step_one   = time_str / 60;
  let time_min   = Math.floor(step_one);

  let step_two   = (step_one - time_min) * 60;
  let time_sec   = Math.floor(step_two);

  let step_three = (step_two - time_sec) * 60;
  let time_mil   = Math.floor(step_three);



  if (time_min < 10){
    time_min = "0" + time_min.toString();
  } else{
    time_min = time_min.toString();
  }

  if (time_sec < 10){
    time_sec = "0" + time_sec.toString();
  } else{
    time_sec = time_sec.toString();
  }

  if (time_mil < 10){
    time_mil = "0" + time_mil.toString();
  } else{
    time_mil = time_mil.toString();
  }

  return time_min + ":" + time_sec + ":" + time_mil
}





// connect to websocket
var ws = new WebSocket('ws:localhost:8080/time/ws');

// Function is called when go_websocket_server recieves a packet and sends it via the websocket
ws.onmessage = function(event){
  var data =  JSON.parse(event.data);

  switch (data.M_header.M_packetId) {
    // If the data inbound is the lap data packet, grab the amount of total laps
    case 2:
      if (data.M_lapData[data.M_header.M_playerCarIndex].M_currentLapNum > current_lap){

        // Check if lap is fastest lap and at same time check for slowest lap
        //
        // Check to make sure we have actually finished a full lap first. Not just jumping to a lap mid race like with the pcap or
        // starting this on a race that is currently in progress. Without this we would set fastest lap time to 0 and would never
        // actually find the fastest lap
        if (current_lap != 0) {
          // If we have already had a full lap and our fastest lap time and fastest lap is still 0 meaning we havent had a fastest lap
          // yet becuase this would be our first real compleated lap. Set this first lap to our fastest lap.
          if (fastest_lap_time == 0){
            fastest_lap_time = current_lap_time;
            fastest_lap_number = current_lap;
            // toggle the color for the row of the fastest lap
            document.getElementById('lap_' + fastest_lap_number).classList.toggle('fastest_lap');

            // Also set this as our slowest lap time since this would be our first completed lap, meaning it is not just our fastest lap
            // time, it is also our slowest lap time
            slowest_lap_time = current_lap_time;
            slowest_lap_number = current_lap;
          }
          // If our fastest lap time is not zero, meaning we have already compleated and set our first lap as our fastest. Now compare
          // current compleated lap with our fastest and see if we now have a new fastest lap!
          // Also, since we have now compleated two laps, we can now set the slowest of the two as our slowest lap. Eliminated the need for
          // more confusing logic statements, just check and do stuff here for it.
          else {
            // If current lap is faster than our recorded fastest lap time, we have found a new fastest lap!
            if (current_lap_time < fastest_lap_time) {
              // Toggle the color off the previous fastest lap
              document.getElementById('lap_' + fastest_lap_number).classList.toggle('fastest_lap');
              fastest_lap_time = current_lap_time;
              fastest_lap_number = current_lap;
              // Now after setting the new fastest lap number, toggle that lap numbers color on
              document.getElementById('lap_' + fastest_lap_number).classList.toggle('fastest_lap');
            }

            // Check if our past full lap is now the slowest
            if (current_lap_time > slowest_lap_time) {
              slowest_lap_time = current_lap_time;
              slowest_lap_number = current_lap;
              document.getElementById('lap_' + slowest_lap_number).classList.toggle('slowest_lap');
            }
            // In the wierd case in which the first lap is actually our slowest lap. We need to toggle its color for slowest lap since,
            // we arent going to toggle both the fastest and the slowest on the same lap after only one lap. Fastest takes preseident because it
            // truly is the fastest yet. So now toggle the color on the first lap.
            else {
              if (!document.getElementById('lap_' + slowest_lap_number).classList.contains('slowest_lap')){
                document.getElementById('lap_' + slowest_lap_number).classList.toggle('slowest_lap');
              }
            }
          }
        }

        // Check if we pitted this lap
        if (has_pitted != 0){
          document.getElementById('lap_' + current_lap).classList.toggle('car_pitted');
          // Set has pited to zero since we have already checked if we have, and now we are starting a new lap
          has_pitted = 0;
        }

        // Now set the current lap to the new lap we are starting
        current_lap = data.M_lapData[data.M_header.M_playerCarIndex].M_currentLapNum;
        // Create the string that is the html for the new lap to be added to our time chart
        var new_time_entry = new_time_entry_html_part_one + 'lap_' + current_lap.toString() + new_time_entry_html_part_two + current_lap.toString() + new_time_entry_html_part_three + current_lap.toString() + new_time_entry_html_part_four + new_time_entry_sector_one + new_time_entry_html_part_five + current_lap.toString() + new_time_entry_html_part_six + new_time_entry_sector_two + new_time_entry_html_part_seven + current_lap.toString() + new_time_entry_html_part_eight + new_time_entry_sector_three + new_time_entry_html_part_nine + current_lap.toString() + new_time_entry_html_part_ten + new_time_entry_lap_time + new_time_entry_html_part_eleven;
        // Add the new laps html row into our time chart
        document.getElementById('time_chart_grid').innerHTML += new_time_entry;

        // Get the elements for the new laps html elements representing the time values
        current_time_entry_sector_one   = document.getElementById(current_lap.toString() + '_sector_one_text');
        current_time_entry_sector_two   = document.getElementById(current_lap.toString() + '_sector_two_text');
        current_time_entry_sector_three = document.getElementById(current_lap.toString() + '_sector_three_text');
        current_time_entry_lap_time     = document.getElementById(current_lap.toString() + '_lap_time_text');
      }

      // Set the html elements for the current lap to the times sent over from our udp packets
      current_time_entry_lap_time.innerHTML       = intTime_to_timeTime(data.M_lapData[data.M_header.M_playerCarIndex].M_currentLapTime);
      current_lap_time                            = data.M_lapData[data.M_header.M_playerCarIndex].M_currentLapTime;
      // Since there is no sector three time udp packet data, we can check what sector we are in, and if we are in sector three then
      // we subtract the two sector times from our overall current lap time to get the time for sector three
      current_time_entry_sector_one.innerHTML     = intTime_to_timeTime(data.M_lapData[data.M_header.M_playerCarIndex].M_sector1Time);
      current_time_entry_sector_two.innerHTML     = intTime_to_timeTime(data.M_lapData[data.M_header.M_playerCarIndex].M_sector2Time);
      if (data.M_lapData[data.M_header.M_playerCarIndex].M_sector == 2) {
        current_time_entry_sector_three.innerHTML = intTime_to_timeTime(data.M_lapData[data.M_header.M_playerCarIndex].M_currentLapTime - data.M_lapData[data.M_header.M_playerCarIndex].M_sector2Time - data.M_lapData[data.M_header.M_playerCarIndex].M_sector1Time);
      }

      // Only check if we have pitted when we havent. Save the computer from checking if we have the status and setting the piting to 1 if we already have
      if (has_pitted == 0) {
        if (data.M_lapData[data.M_header.M_playerCarIndex].M_pitStatus == 1 || data.M_lapData[data.M_header.M_playerCarIndex].M_pitStatus == 2) {
          has_pitted = 1;
        }
      }


      // End of case thingy stuff stuff
      break;
  }
}
