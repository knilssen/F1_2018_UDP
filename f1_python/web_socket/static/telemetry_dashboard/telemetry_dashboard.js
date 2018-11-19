// connect to websocket
var ws = new WebSocket('ws://localhost:9090/ws');

// set up the html elements
// Lap
var laps_element = document.getElementById('lap_number');
// position
var race_position_element = document.getElementById('race_position');
// last lap shit
var last_lap_time_element = document.getElementById('last_lap_time');
//  pit shit
var pit_status_element = document.getElementById('pit_status');
// sector shit`
var current_sector_element = document.getElementById('current_sector');
// drs shit
var drs_status_element = document.getElementById('drs_status');
// gear shit
var current_gear_element = document.getElementById('current_gear');
// fia flags shit
var current_fia_flags_element = document.getElementById('current_fia_flags');


// create an array with the pit data strings
var pit_info = ['None', 'Pitting', 'In Pit Area'];

// create an array with the gear data strings
var gear_info = ['N','1','2','3','4','5','6','7','8'];
gear_info[-1] = 'R';

// create an array with the drs data strings
var drs_info = ['OFF', 'ON'];

// create an array with the fia flags data strings
var fia_info = ['None', 'Green', 'Blue', 'Yelliw', 'Red'];
fia_info[-1] = 'invalid/unknown';

// set the total laps to 0, then change when we do finally get the packet
var amount_of_laps = 0;

// get the speed_canvas container height and width
var speed_canvas_container = document.getElementById("speed_graph_container");
var rpm_canvas_container = document.getElementById("rpm_graph_container");
var gear_canvas_container = document.getElementById("gear_graph_container");
var throttle_brake_canvas_container = document.getElementById("throttle_brake_graph_container");

// Get the html5 canvas element and set the width to the chart width
var speed_canvas = document.getElementById("speed_chart_canvas");
speed_canvas.width = speed_canvas_container.offsetWidth;
speed_canvas.height = speed_canvas_container.offsetHeight;

var rpm_canvas = document.getElementById("rpm_chart_canvas");
rpm_canvas.width = rpm_canvas_container.offsetWidth;
rpm_canvas.height = rpm_canvas_container.offsetHeight;

var gear_canvas = document.getElementById("gear_chart_canvas");
gear_canvas.width = gear_canvas_container.offsetWidth;
gear_canvas.height = gear_canvas_container.offsetHeight;

var throttle_brake_canvas = document.getElementById("throttle_brake_chart_canvas");
throttle_brake_canvas.width = throttle_brake_canvas_container.offsetWidth;
throttle_brake_canvas.height = throttle_brake_canvas_container.offsetHeight;



// Get the canvas '2d' object, which can be used to draw text, lines, boxes, circles, and more - on the canvas.
// We do this since canvas doesnt actually let us draw, it is simply a container
var speed_ctx = speed_canvas.getContext("2d");
var speed_canvas_height = speed_canvas.height;
var speed_canvas_width = speed_canvas.width;

var rpm_ctx = rpm_canvas.getContext("2d");
var rpm_canvas_height = rpm_canvas.height;
var rpm_canvas_width = rpm_canvas.width;

var gear_ctx = gear_canvas.getContext("2d");
var gear_canvas_height = gear_canvas.height;
var gear_canvas_width = gear_canvas.width;

var throttle_brake_ctx = throttle_brake_canvas.getContext("2d");
var throttle_brake_canvas_height = throttle_brake_canvas.height;
var throttle_brake_canvas_width = throttle_brake_canvas.width;



// create an array that will hold our speed chart data, with the first data point being "0,0" equivilent
var speed_chart_data = [];
var rpm_chart_data = [];
var gear_chart_data = [];
var throttle_brake_chart_throttle_data = [];
var throttle_brake_chart_brake_data = [];

// Set a variable that will be how many points can be contained in the chart.
// For now, set this to the width of the chart so each input from our websocket will be a pixel apart
// Adjust as required
var chart_points_number = speed_canvas_width;

// Set a variable for the shift variable
var chart_shift_variable = speed_canvas_width / chart_points_number;

// translate the 0,0 point from the top left of the canvas to the bottom left of the canvas
speed_ctx.translate(0, speed_canvas_height);
speed_ctx.scale(1, -1);

rpm_ctx.translate(0, rpm_canvas_height);
rpm_ctx.scale(1, -1);

gear_ctx.translate(0, gear_canvas_height);
gear_ctx.scale(1, -1);

throttle_brake_ctx.translate(0, throttle_brake_canvas_height);
throttle_brake_ctx.scale(1, -1);

// set the chart line_widths
speed_ctx.lineWidth = "2";
rpm_ctx.lineWidth = "2";
gear_ctx.lineWidth = "2";
throttle_brake_ctx.lineWidth = "2";

// set the chart line_colors
speed_ctx.strokeStyle = "#8D8741";
rpm_ctx.strokeStyle = "#FF4136";
gear_ctx.strokeStyle = "#7FDBFF";
// throttle_brake uses two color lines, need function to draw and array to hold colors
throttle_brake_line_colors = ['#01FF70','#FF851B'];

// Multiplier to convert speed in relation to canvas height where 0 is bottom and 350 km/h is the top
var speed_multiplier = speed_canvas_height / 350;
var rpm_multiplier = rpm_canvas_height / 12500;
var gear_multiplier = gear_canvas_height / 8;
var throttle_brake_multiplier = throttle_brake_canvas_height / 100;


// Function that shifts the chart
function chart_shift(chart_data) {
  // If our chart is full with data, delete the furthest left
  if (chart_data.length > chart_points_number) {
    chart_data.splice(0,1);
  };

  // shift the chart data
  for (x=0; x < chart_data.length; x++){
    chart_data[x][0] = chart_data[x][0] - chart_shift_variable;

  };
};

// Function to clear the chart before redraw
function clear_chart(chart_ctx, chart_canvas) {
  chart_ctx.clearRect(0, 0, chart_canvas.width, chart_canvas.height);
}

// Function to draw the chart
function draw_chart(chart_data, chart_ctx, chart_canvas) {
  // First we need to clear the chart
  chart_shift(chart_data);
  clear_chart(chart_ctx, chart_canvas);

  var previous_points = chart_data[0];

  // Begin the path of the line chart
  chart_ctx.moveTo(previous_points[0], previous_points[1]);
  chart_ctx.beginPath();


  for (x=0; x<chart_data.length; x++){
    chart_ctx.moveTo(previous_points[0], previous_points[1]);
    chart_ctx.lineTo(chart_data[x][0], chart_data[x][1]);
    previous_points = chart_data[x];
  };

  chart_ctx.stroke();
}

// Function to draw throttle_brake chart
function draw_throttle_brake_chart(throttle_data, brake_data, chart_ctx, chart_canvas) {
  // First we need to clear the chart
  chart_shift(throttle_data);
  chart_shift(brake_data);
  clear_chart(chart_ctx, chart_canvas);

  var data_array = [throttle_data,brake_data];

  for(y=0; y<2; y++){

    var previous_points = data_array[y][0];
    chart_ctx.moveTo(previous_points[0], previous_points[1]);
    chart_ctx.strokeStyle = throttle_brake_line_colors[y];
    chart_ctx.beginPath();

    for (x=0; x<data_array[y].length; x++){
      chart_ctx.moveTo(previous_points[0], previous_points[1]);
      chart_ctx.lineTo(data_array[y][x][0], data_array[y][x][1]);
      previous_points = data_array[y][x];
    };

    chart_ctx.stroke();

  };
}

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

// Function is called when live_map_tornado recieves a packet and sends it via the websocket
ws.onmessage = function(event){
  var data =  JSON.parse(event.data);

  // If the data inbound is the session data packet, grab the amount of total laps
  if (data.header.packetId == 1){
    if (amount_of_laps == 0) {
      amount_of_laps = data.totalLaps;
    }
  }

  // If the data inbound is the lap data packet
  if (data.header.packetId == 2){
    // set current lap number data
    if (amount_of_laps != 0) {
      laps_element.innerHTML = JSON.stringify(data.lapData.currentLapNum, null) + " of " + JSON.stringify(amount_of_laps, null);
    }
    // Set the data for the rest lap packet informations
    race_position_element.innerHTML = JSON.stringify(data.lapData.carPosition, null);
    last_lap_time_element.innerHTML = intTime_to_timeTime(data.lapData.lastLapTime);                        // convert to time format?
    pit_status_element.innerHTML = pit_info[data.lapData.pitStatus];                                        // 0 = none, 1 = pitting, 2 = in pit area
    current_sector_element.innerHTML = JSON.stringify((data.lapData.sector + 1), null);                     // 0 = sector1, 1 = sector2, 2 = sector3
  }

  // If the data inbound is the car telemetry packet
  if (data.header.packetId == 6){
    // Set the data for the telemetry packet information
    drs_status_element.innerHTML = drs_info[data.carTelemetryData.drs];                                     // 0 = off, 1 = on
    current_gear_element.innerHTML = gear_info[data.carTelemetryData.gear];
    speed_chart_data.push([speed_canvas_width, data.carTelemetryData.speed * speed_multiplier]);
    rpm_chart_data.push([rpm_canvas_width, data.carTelemetryData.engineRPM * rpm_multiplier]);
    gear_chart_data.push([gear_canvas_width, data.carTelemetryData.gear * gear_multiplier]);

    throttle_brake_chart_throttle_data.push([throttle_brake_canvas_width, data.carTelemetryData.throttle * throttle_brake_multiplier]);
    throttle_brake_chart_brake_data.push([throttle_brake_canvas_width, data.carTelemetryData.brake * throttle_brake_multiplier]);

    draw_chart(speed_chart_data, speed_ctx, speed_canvas);
    draw_chart(rpm_chart_data, rpm_ctx, rpm_canvas);
    draw_chart(gear_chart_data, gear_ctx, gear_canvas);
    draw_throttle_brake_chart(throttle_brake_chart_throttle_data, throttle_brake_chart_brake_data, throttle_brake_ctx, throttle_brake_canvas);
  }



  // If the data inbound is the car status packet
  if (data.header.packetId == 7){
    // Set the data for the status packet information
    current_fia_flags_element.innerHTML = fia_info[data.carStatusData.vehicleFiaFlags];                     // -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
  }

}
