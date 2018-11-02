// connect to websocket
var ws = new WebSocket('ws://localhost:9090/ws');

// Get Header html elements
var packetFormat = document.getElementById('packetFormat');
var packetVersion = document.getElementById('packetVersion');
var packetId = document.getElementById('packetId');
var sessionUID = document.getElementById('sessionUID');
var sessionTime = document.getElementById('sessionTime');
var frameIdentifier = document.getElementById('frameIdentifier');
var playerCarIndex = document.getElementById('playerCarIndex');


// Get car X, Y, and Z html elements
var car_1_pos_x = document.getElementById('car_1_pos_x');
var car_1_pos_y = document.getElementById('car_1_pos_y');
var car_1_pos_z = document.getElementById('car_1_pos_z');
var car_2_pos_x = document.getElementById('car_2_pos_x');
var car_2_pos_y = document.getElementById('car_2_pos_y');
var car_2_pos_z = document.getElementById('car_2_pos_z');
var car_3_pos_x = document.getElementById('car_3_pos_x');
var car_3_pos_y = document.getElementById('car_3_pos_y');
var car_3_pos_z = document.getElementById('car_3_pos_z');
var car_4_pos_x = document.getElementById('car_4_pos_x');
var car_4_pos_y = document.getElementById('car_4_pos_y');
var car_4_pos_z = document.getElementById('car_4_pos_z');
var car_5_pos_x = document.getElementById('car_5_pos_x');
var car_5_pos_y = document.getElementById('car_5_pos_y');
var car_5_pos_z = document.getElementById('car_5_pos_z');
var car_6_pos_x = document.getElementById('car_6_pos_x');
var car_6_pos_y = document.getElementById('car_6_pos_y');
var car_6_pos_z = document.getElementById('car_6_pos_z');
var car_7_pos_x = document.getElementById('car_7_pos_x');
var car_7_pos_y = document.getElementById('car_7_pos_y');
var car_7_pos_z = document.getElementById('car_7_pos_z');
var car_8_pos_x = document.getElementById('car_8_pos_x');
var car_8_pos_y = document.getElementById('car_8_pos_y');
var car_8_pos_z = document.getElementById('car_8_pos_z');
var car_9_pos_x = document.getElementById('car_9_pos_x');
var car_9_pos_y = document.getElementById('car_9_pos_y');
var car_9_pos_z = document.getElementById('car_9_pos_z');
var car_10_pos_x = document.getElementById('car_10_pos_x');
var car_10_pos_y = document.getElementById('car_10_pos_y');
var car_10_pos_z = document.getElementById('car_10_pos_z');
var car_11_pos_x = document.getElementById('car_11_pos_x');
var car_11_pos_y = document.getElementById('car_11_pos_y');
var car_11_pos_z = document.getElementById('car_11_pos_z');
var car_12_pos_x = document.getElementById('car_12_pos_x');
var car_12_pos_y = document.getElementById('car_12_pos_y');
var car_12_pos_z = document.getElementById('car_12_pos_z');
var car_13_pos_x = document.getElementById('car_13_pos_x');
var car_13_pos_y = document.getElementById('car_13_pos_y');
var car_13_pos_z = document.getElementById('car_13_pos_z');
var car_14_pos_x = document.getElementById('car_14_pos_x');
var car_14_pos_y = document.getElementById('car_14_pos_y');
var car_14_pos_z = document.getElementById('car_14_pos_z');
var car_15_pos_x = document.getElementById('car_15_pos_x');
var car_15_pos_y = document.getElementById('car_15_pos_y');
var car_15_pos_z = document.getElementById('car_15_pos_z');
var car_16_pos_x = document.getElementById('car_16_pos_x');
var car_16_pos_y = document.getElementById('car_16_pos_y');
var car_16_pos_z = document.getElementById('car_16_pos_z');
var car_17_pos_x = document.getElementById('car_17_pos_x');
var car_17_pos_y = document.getElementById('car_17_pos_y');
var car_17_pos_z = document.getElementById('car_17_pos_z');
var car_18_pos_x = document.getElementById('car_18_pos_x');
var car_18_pos_y = document.getElementById('car_18_pos_y');
var car_18_pos_z = document.getElementById('car_18_pos_z');
var car_19_pos_x = document.getElementById('car_19_pos_x');
var car_19_pos_y = document.getElementById('car_19_pos_y');
var car_19_pos_z = document.getElementById('car_19_pos_z');
var car_20_pos_x = document.getElementById('car_20_pos_x');
var car_20_pos_y = document.getElementById('car_20_pos_y');
var car_20_pos_z = document.getElementById('car_20_pos_z');


// Get car position in race elements
var car_1_pos = document.getElementById('car_1_pos');
var car_2_pos = document.getElementById('car_2_pos');
var car_3_pos = document.getElementById('car_3_pos');
var car_4_pos = document.getElementById('car_4_pos');
var car_5_pos = document.getElementById('car_5_pos');
var car_6_pos = document.getElementById('car_6_pos');
var car_7_pos = document.getElementById('car_7_pos');
var car_8_pos = document.getElementById('car_8_pos');
var car_9_pos = document.getElementById('car_9_pos');
var car_10_pos = document.getElementById('car_10_pos');
var car_11_pos = document.getElementById('car_11_pos');
var car_12_pos = document.getElementById('car_12_pos');
var car_13_pos = document.getElementById('car_13_pos');
var car_14_pos = document.getElementById('car_14_pos');
var car_15_pos = document.getElementById('car_15_pos');
var car_16_pos = document.getElementById('car_16_pos');
var car_17_pos = document.getElementById('car_17_pos');
var car_18_pos = document.getElementById('car_18_pos');
var car_19_pos = document.getElementById('car_19_pos');
var car_20_pos = document.getElementById('car_20_pos');

// Get car position in race elements and place them into an arrays
var car_position_elements = [car_1_pos, car_2_pos, car_3_pos, car_4_pos, car_5_pos, car_6_pos, car_7_pos, car_8_pos, car_9_pos, car_10_pos, car_11_pos, car_12_pos, car_13_pos, car_14_pos, car_15_pos, car_16_pos, car_17_pos, car_18_pos, car_19_pos, car_20_pos];

// Get the html5 canvas element and set the width to the screen width
// and set the height to fill the rest of the screne, eleminating the need to scroll
var canvas = document.getElementById("packet_canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight - (canvas.offsetTop);

// Get the canvas '2d' object, which can be used to draw text, lines, boxes, circles, and more - on the canvas.
// We do this since canvas doesnt actually let us draw, it is simply a container
var ctx = canvas.getContext("2d");
var canvas_height = canvas.height;
var canvas_width = canvas.width;

// Set the ctx x and y point for (0,0) from the upper left of the canvas object to the center point to allow
// our negative world coordinates
ctx.translate(canvas_width/2, canvas_height/2);

var previous_leaderboard = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];


// Function is called when live_map_tornado recieves a packet and sends it via the websocket
ws.onmessage = function(event){
  var data =  JSON.parse(event.data);

  // Load the header data of the most recent recieved packet to the webpage
  packetFormat.innerHTML = JSON.stringify(data.header.packetFormat, null);
  packetVersion.innerHTML = JSON.stringify(data.header.packetVersion, null);
  packetId.innerHTML = JSON.stringify(data.header.packetId, null);
  sessionUID.innerHTML = JSON.stringify(data.header.sessionUID, null);
  sessionTime.innerHTML = JSON.stringify(data.header.sessionTime, null);
  frameIdentifier.innerHTML = JSON.stringify(data.header.frameIdentifier, null);
  playerCarIndex.innerHTML = JSON.stringify(data.header.playerCarIndex, null);


  // If we receive a packet with the packetId of 0, which is the id for the motion_data packet
  if (data.header.packetId == 0){

    // Set the actual position coordinates for all cars to the display in grid above the html canvas live map
    car_1_pos_x.innerHTML = JSON.stringify(data.carMotionData[0].worldPositionX.toFixed(2), null);
    car_1_pos_y.innerHTML = JSON.stringify(data.carMotionData[0].worldPositionY.toFixed(2), null);
    car_1_pos_z.innerHTML = JSON.stringify(data.carMotionData[0].worldPositionZ.toFixed(2), null);
    car_2_pos_x.innerHTML = JSON.stringify(data.carMotionData[1].worldPositionX.toFixed(2), null);
    car_2_pos_y.innerHTML = JSON.stringify(data.carMotionData[1].worldPositionY.toFixed(2), null);
    car_2_pos_z.innerHTML = JSON.stringify(data.carMotionData[1].worldPositionZ.toFixed(2), null);
    car_3_pos_x.innerHTML = JSON.stringify(data.carMotionData[2].worldPositionX.toFixed(2), null);
    car_3_pos_y.innerHTML = JSON.stringify(data.carMotionData[2].worldPositionY.toFixed(2), null);
    car_3_pos_z.innerHTML = JSON.stringify(data.carMotionData[2].worldPositionZ.toFixed(2), null);
    car_4_pos_x.innerHTML = JSON.stringify(data.carMotionData[3].worldPositionX.toFixed(2), null);
    car_4_pos_y.innerHTML = JSON.stringify(data.carMotionData[3].worldPositionY.toFixed(2), null);
    car_4_pos_z.innerHTML = JSON.stringify(data.carMotionData[3].worldPositionZ.toFixed(2), null);
    car_5_pos_x.innerHTML = JSON.stringify(data.carMotionData[4].worldPositionX.toFixed(2), null);
    car_5_pos_y.innerHTML = JSON.stringify(data.carMotionData[4].worldPositionY.toFixed(2), null);
    car_5_pos_z.innerHTML = JSON.stringify(data.carMotionData[4].worldPositionZ.toFixed(2), null);
    car_6_pos_x.innerHTML = JSON.stringify(data.carMotionData[5].worldPositionX.toFixed(2), null);
    car_6_pos_y.innerHTML = JSON.stringify(data.carMotionData[5].worldPositionY.toFixed(2), null);
    car_6_pos_z.innerHTML = JSON.stringify(data.carMotionData[5].worldPositionZ.toFixed(2), null);
    car_7_pos_x.innerHTML = JSON.stringify(data.carMotionData[6].worldPositionX.toFixed(2), null);
    car_7_pos_y.innerHTML = JSON.stringify(data.carMotionData[6].worldPositionY.toFixed(2), null);
    car_7_pos_z.innerHTML = JSON.stringify(data.carMotionData[6].worldPositionZ.toFixed(2), null);
    car_8_pos_x.innerHTML = JSON.stringify(data.carMotionData[7].worldPositionX.toFixed(2), null);
    car_8_pos_y.innerHTML = JSON.stringify(data.carMotionData[7].worldPositionY.toFixed(2), null);
    car_8_pos_z.innerHTML = JSON.stringify(data.carMotionData[7].worldPositionZ.toFixed(2), null);
    car_9_pos_x.innerHTML = JSON.stringify(data.carMotionData[8].worldPositionX.toFixed(2), null);
    car_9_pos_y.innerHTML = JSON.stringify(data.carMotionData[8].worldPositionY.toFixed(2), null);
    car_9_pos_z.innerHTML = JSON.stringify(data.carMotionData[8].worldPositionZ.toFixed(2), null);
    car_10_pos_x.innerHTML = JSON.stringify(data.carMotionData[9].worldPositionX.toFixed(2), null);
    car_10_pos_y.innerHTML = JSON.stringify(data.carMotionData[9].worldPositionY.toFixed(2), null);
    car_10_pos_z.innerHTML = JSON.stringify(data.carMotionData[9].worldPositionZ.toFixed(2), null);
    car_11_pos_x.innerHTML = JSON.stringify(data.carMotionData[10].worldPositionX.toFixed(2), null);
    car_11_pos_y.innerHTML = JSON.stringify(data.carMotionData[10].worldPositionY.toFixed(2), null);
    car_11_pos_z.innerHTML = JSON.stringify(data.carMotionData[10].worldPositionZ.toFixed(2), null);
    car_12_pos_x.innerHTML = JSON.stringify(data.carMotionData[11].worldPositionX.toFixed(2), null);
    car_12_pos_y.innerHTML = JSON.stringify(data.carMotionData[11].worldPositionY.toFixed(2), null);
    car_12_pos_z.innerHTML = JSON.stringify(data.carMotionData[11].worldPositionZ.toFixed(2), null);
    car_13_pos_x.innerHTML = JSON.stringify(data.carMotionData[12].worldPositionX.toFixed(2), null);
    car_13_pos_y.innerHTML = JSON.stringify(data.carMotionData[12].worldPositionY.toFixed(2), null);
    car_13_pos_z.innerHTML = JSON.stringify(data.carMotionData[12].worldPositionZ.toFixed(2), null);
    car_14_pos_x.innerHTML = JSON.stringify(data.carMotionData[13].worldPositionX.toFixed(2), null);
    car_14_pos_y.innerHTML = JSON.stringify(data.carMotionData[13].worldPositionY.toFixed(2), null);
    car_14_pos_z.innerHTML = JSON.stringify(data.carMotionData[13].worldPositionZ.toFixed(2), null);
    car_15_pos_x.innerHTML = JSON.stringify(data.carMotionData[14].worldPositionX.toFixed(2), null);
    car_15_pos_y.innerHTML = JSON.stringify(data.carMotionData[14].worldPositionY.toFixed(2), null);
    car_15_pos_z.innerHTML = JSON.stringify(data.carMotionData[14].worldPositionZ.toFixed(2), null);
    car_16_pos_x.innerHTML = JSON.stringify(data.carMotionData[15].worldPositionX.toFixed(2), null);
    car_16_pos_y.innerHTML = JSON.stringify(data.carMotionData[15].worldPositionY.toFixed(2), null);
    car_16_pos_z.innerHTML = JSON.stringify(data.carMotionData[15].worldPositionZ.toFixed(2), null);
    car_17_pos_x.innerHTML = JSON.stringify(data.carMotionData[16].worldPositionX.toFixed(2), null);
    car_17_pos_y.innerHTML = JSON.stringify(data.carMotionData[16].worldPositionY.toFixed(2), null);
    car_17_pos_z.innerHTML = JSON.stringify(data.carMotionData[16].worldPositionZ.toFixed(2), null);
    car_18_pos_x.innerHTML = JSON.stringify(data.carMotionData[17].worldPositionX.toFixed(2), null);
    car_18_pos_y.innerHTML = JSON.stringify(data.carMotionData[17].worldPositionY.toFixed(2), null);
    car_18_pos_z.innerHTML = JSON.stringify(data.carMotionData[17].worldPositionZ.toFixed(2), null);
    car_19_pos_x.innerHTML = JSON.stringify(data.carMotionData[18].worldPositionX.toFixed(2), null);
    car_19_pos_y.innerHTML = JSON.stringify(data.carMotionData[18].worldPositionY.toFixed(2), null);
    car_19_pos_z.innerHTML = JSON.stringify(data.carMotionData[18].worldPositionZ.toFixed(2), null);
    car_20_pos_x.innerHTML = JSON.stringify(data.carMotionData[19].worldPositionX.toFixed(2), null);
    car_20_pos_y.innerHTML = JSON.stringify(data.carMotionData[19].worldPositionY.toFixed(2), null);
    car_20_pos_z.innerHTML = JSON.stringify(data.carMotionData[19].worldPositionZ.toFixed(2), null);


    // Save the actual position coordinates for all cars to be used to draw to the live map
    var car_1_x = data.carMotionData[0].worldPositionX;
    var car_1_y = data.carMotionData[0].worldPositionY;
    var car_1_z = data.carMotionData[0].worldPositionZ;
    var car_2_x = data.carMotionData[1].worldPositionX;
    var car_2_y = data.carMotionData[1].worldPositionY;
    var car_2_z = data.carMotionData[1].worldPositionZ;
    var car_3_x = data.carMotionData[2].worldPositionX;
    var car_3_y = data.carMotionData[2].worldPositionY;
    var car_3_z = data.carMotionData[2].worldPositionZ;
    var car_4_x = data.carMotionData[3].worldPositionX;
    var car_4_y = data.carMotionData[3].worldPositionY;
    var car_4_z = data.carMotionData[3].worldPositionZ;
    var car_5_x = data.carMotionData[4].worldPositionX;
    var car_5_y = data.carMotionData[4].worldPositionY;
    var car_5_z = data.carMotionData[4].worldPositionZ;
    var car_6_x = data.carMotionData[5].worldPositionX;
    var car_6_y = data.carMotionData[5].worldPositionY;
    var car_6_z = data.carMotionData[5].worldPositionZ;
    var car_7_x = data.carMotionData[6].worldPositionX;
    var car_7_y = data.carMotionData[6].worldPositionY;
    var car_7_z = data.carMotionData[6].worldPositionZ;
    var car_8_x = data.carMotionData[7].worldPositionX;
    var car_8_y = data.carMotionData[7].worldPositionY;
    var car_8_z = data.carMotionData[7].worldPositionZ;
    var car_9_x = data.carMotionData[8].worldPositionX;
    var car_9_y = data.carMotionData[8].worldPositionY;
    var car_9_z = data.carMotionData[8].worldPositionZ;
    var car_10_x = data.carMotionData[9].worldPositionX;
    var car_10_y = data.carMotionData[9].worldPositionY;
    var car_10_z = data.carMotionData[9].worldPositionZ;
    var car_11_x = data.carMotionData[10].worldPositionX;
    var car_11_y = data.carMotionData[10].worldPositionY;
    var car_11_z = data.carMotionData[10].worldPositionZ;
    var car_12_x = data.carMotionData[11].worldPositionX;
    var car_12_y = data.carMotionData[11].worldPositionY;
    var car_12_z = data.carMotionData[11].worldPositionZ;
    var car_13_x = data.carMotionData[12].worldPositionX;
    var car_13_y = data.carMotionData[12].worldPositionY;
    var car_13_z = data.carMotionData[12].worldPositionZ;
    var car_14_x = data.carMotionData[13].worldPositionX;
    var car_14_y = data.carMotionData[13].worldPositionY;
    var car_14_z = data.carMotionData[13].worldPositionZ;
    var car_15_x = data.carMotionData[14].worldPositionX;
    var car_15_y = data.carMotionData[14].worldPositionY;
    var car_15_z = data.carMotionData[14].worldPositionZ;
    var car_16_x = data.carMotionData[15].worldPositionX;
    var car_16_y = data.carMotionData[15].worldPositionY;
    var car_16_z = data.carMotionData[15].worldPositionZ;
    var car_17_x = data.carMotionData[16].worldPositionX;
    var car_17_y = data.carMotionData[16].worldPositionY;
    var car_17_z = data.carMotionData[16].worldPositionZ;
    var car_18_x = data.carMotionData[17].worldPositionX;
    var car_18_y = data.carMotionData[17].worldPositionY;
    var car_18_z = data.carMotionData[17].worldPositionZ;
    var car_19_x = data.carMotionData[18].worldPositionX;
    var car_19_y = data.carMotionData[18].worldPositionY;
    var car_19_z = data.carMotionData[18].worldPositionZ;
    var car_20_x = data.carMotionData[19].worldPositionX;
    var car_20_y = data.carMotionData[19].worldPositionY;
    var car_20_z = data.carMotionData[19].worldPositionZ;


    // Clear the map each time so we have a moving square representing our cars, not leaving behind
    // trails of previously drawn car positions
    clearMap(ctx);

    // Call the drawCar function for each car using its X, Y, and Z positions, if it is a filled color
    // square or just a border colored square, and the color in which to color with
    drawCar(ctx, car_1_x/3, car_1_y/3, car_1_z/3, "stroke", "green");
    drawCar(ctx, car_2_x/3, car_2_y/3, car_2_z/3, "stroke", "grey");
    drawCar(ctx, car_3_x/3, car_3_y/3, car_3_z/3, "stroke", "yellow");
    drawCar(ctx, car_4_x/3, car_4_y/3, car_4_z/3, "stroke", "black");
    drawCar(ctx, car_5_x/3, car_5_y/3, car_5_z/3, "stroke", "brown");
    drawCar(ctx, car_6_x/3, car_6_y/3, car_6_z/3, "stroke", "red");
    drawCar(ctx, car_7_x/3, car_7_y/3, car_7_z/3, "stroke", "blue");
    drawCar(ctx, car_8_x/3, car_8_y/3, car_8_z/3, "stroke", "orange");
    drawCar(ctx, car_9_x/3, car_9_y/3, car_9_z/3, "stroke", "purple");
    drawCar(ctx, car_10_x/3, car_10_y/3, car_10_z/3, "stroke", "pink");
    drawCar(ctx, car_11_x/3, car_11_y/3, car_11_z/3, "fill", "green");
    drawCar(ctx, car_12_x/3, car_12_y/3, car_12_z/3, "fill", "grey");
    drawCar(ctx, car_13_x/3, car_13_y/3, car_13_z/3, "fill", "yellow");
    drawCar(ctx, car_14_x/3, car_14_y/3, car_14_z/3, "fill", "black");
    drawCar(ctx, car_15_x/3, car_15_y/3, car_15_z/3, "fill", "brown");
    drawCar(ctx, car_16_x/3, car_16_y/3, car_16_z/3, "fill", "red");
    drawCar(ctx, car_17_x/3, car_17_y/3, car_17_z/3, "fill", "blue");
    drawCar(ctx, car_18_x/3, car_18_y/3, car_18_z/3, "fill", "orange");
    drawCar(ctx, car_19_x/3, car_19_y/3, car_19_z/3, "fill", "purple");
    drawCar(ctx, car_20_x/3, car_20_y/3, car_20_z/3, "fill", "pink");


    function drawCar(ctx, x, y, z, type, color) {
      // Set the thickness of the square boarder
      ctx.lineWidth = "4";

      // If square is a boarder color or a solid color, draw accordingly
      if (type === "stroke"){
        ctx.strokeStyle = color;
        ctx.beginPath();
        ctx.rect(x+15, z-15, 30, 30);
        ctx.stroke();
      } else {
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.fillRect(x+15, z-15, 30, 30);
      }
    }

    // Function that clears the map by overlaying a clearRect on top of the whole canvas area.
    // Needs to set its coordinates from (0,0) which is dead center, to the top left corner
    // in order to 'clear' our canvas area.
    function clearMap(ctx) {
      ctx.clearRect(0-(canvas_width/2), 0-(canvas_height/2), canvas.width, canvas.height);
    }

  }


  // If we receive a packet with the packetId of 2, which is the id for the lap_data packet
  if (data.header.packetId == 2){
    // Sets up array to hold current car standings
    var current_leaderboard = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];
    var similar_leaderboars = true;

    // Loops through car_position_elements and sets the innerHTML of those elements to the position
    // the corresponding car is in the current race
    for (i = 0, len = (data.lapData).length; i < len; i++) {
      var cars_lap_data = data.lapData[i].carPosition
      car_position_elements[i].innerHTML = JSON.stringify(cars_lap_data, null);
      current_leaderboard[cars_lap_data-1] = i

      // If previous leaderboard does not match up with current leaderboard, then make sure we set our boolean so
      if (current_leaderboard[cars_lap_data-1] != previous_leaderboard[cars_lap_data-1]){
        similar_leaderboars = false;
      }
    }

    // If our boolean for similar leaderboards is false, then update the previous leaderboard, and the standings in the webpage
    if (similar_leaderboars == false){
      previous_leaderboard = current_leaderboard;


      let car_elements = []
      let car_position_container = document.querySelector('.grid-container')
      // Add each row to the array
      car_position_container.querySelectorAll('.car').forEach(el => car_elements.push(el))
      // Clear the container
      car_position_container.innerHTML = ''
      // Sort the array from highest to lowest
      car_elements.sort((a, b) => a.querySelector('.position').textContent - b.querySelector('.position').textContent)
      // Put the elements back into the container
      car_elements.forEach(e => car_position_container.appendChild(e))

    }
  }
}
