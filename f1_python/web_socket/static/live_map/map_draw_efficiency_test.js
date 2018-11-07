// connect to websocket
var ws = new WebSocket('ws://localhost:9090/ws');

// Get Header html elements
var header_elements_dictionary = {};
var header_container = document.querySelector('.header_container');
header_container.querySelectorAll('span').forEach(el => header_elements_dictionary[el.id] = el);

// Get car X, Y, and Z html elements
// Store them in a dictionary for later use
var car_coordinate_elements_dictionary = {};
var cars_container = document.querySelector('.grid-container');
cars_container.querySelectorAll('.car').forEach(el => (car_coordinate_elements_dictionary[el.id] = {}, el.querySelectorAll('.car_coordinates').forEach(el_two => car_coordinate_elements_dictionary[el.id][el_two.id] = el_two)));

// Get car position elements
// Store them in a dictionary for later use
var car_position_elements_dictionary = {};
cars_container.querySelectorAll('.car').forEach(el => (car_position_elements_dictionary[el.id] = {}, el.querySelectorAll('.position').forEach(el_two => car_position_elements_dictionary[el.id] = el_two)));

// Create an array that holds the colors we will use to draw the cars in
var car_color = ["green","olive","yellow","black","brown","red","blue","orange","purple","pink", "lightgreen","lightgrey","lightyellow","darkgrey","cyan","darkred","lightblue","darkkhaki","plum","lightpink"];

// Create a dictionary that holds the car positions data for easy iterating when drawing the car objects
var car_position_dictionary = {};

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

// Make an array of null variables for previous_leaderboard, since the first packet will be different, it will
// Update this array and populate it
var previous_leaderboard = [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null];


// Function is called when live_map_tornado recieves a packet and sends it via the websocket
ws.onmessage = function(event){
  var data =  JSON.parse(event.data);

  // Load the header data of the most recent recieved packet to the webpage
  for (header_item in header_elements_dictionary){
    header_elements_dictionary[header_item].innerHTML = JSON.stringify(data.header[header_item], null);
  }

  // If we receive a packet with the packetId of 0, which is the id for the motion_data packet
  if (data.header.packetId == 0){
    // Loop through our car_coordinate_elements_dictionary and using that set each of the x, y, z elements to their
    // actual position in the game
    for (let x=0; x < 20; x++){
      let car_name        = "Car"+(x+1).toString();
      let car_name_coord  = "car_"+(x+1).toString();
      let car_coord_x     = car_name_coord + "_pos_x";
      let car_coord_y     = car_name_coord + "_pos_y";
      let car_coord_z     = car_name_coord + "_pos_z";
      car_coordinate_elements_dictionary[car_name][car_coord_x].innerHTML = JSON.stringify(data.carMotionData[x].worldPositionX.toFixed(2), null);
      car_coordinate_elements_dictionary[car_name][car_coord_y].innerHTML = JSON.stringify(data.carMotionData[x].worldPositionY.toFixed(2), null);
      car_coordinate_elements_dictionary[car_name][car_coord_z].innerHTML = JSON.stringify(data.carMotionData[x].worldPositionZ.toFixed(2), null);
    };

    // Add all cars and their positional coordinates to the car_position_dictionary
    for (let x=0; x < 20; x++){
      car_position_dictionary[x] = {};
      car_position_dictionary[x]["x"]       = data.carMotionData[x].worldPositionX;
      car_position_dictionary[x]["y"]       = data.carMotionData[x].worldPositionY;
      car_position_dictionary[x]["z"]       = data.carMotionData[x].worldPositionZ;
      car_position_dictionary[x]["color"]   = car_color[x];
    }

    // Clear the map each time so we have a moving square representing our cars, not leaving behind
    // trails of previously drawn car positions
    // clearMap(ctx);
    ctx.clearRect(0-(canvas_width/2), 0-(canvas_height/2), canvas.width, canvas.height);

    // Set the lineWidth for the squars boarders
    ctx.lineWidth = "4";

    // Loop through the cars, and when done with defining the objects to draw, draw them to the canvas.
    // This step will greatly improve efficiancy due to only "drawing" once with all the cars vs drawing
    // For each car we have.
    // We are also definiing the draw object of the same color at the same time to improve efficiancy, this
    // is more efficiant becuase each time we change the strokeStyle color we have to change the canvas.
    for (let x=0; x<20; x++) {
      ctx.beginPath();
      // ctx.strokeStyle = car_position_dictionary[x]["color"];
      ctx.fillStyle = car_position_dictionary[x]["color"];
      // Define the drawing of the boardered car object, we divide by three to fit the map to the screen
      // ctx.rect(((car_position_dictionary[x]["x"])+15)/3, ((car_position_dictionary[x]["z"])-15)/3, 30, 30);
      // Define the drawing of the solid car object, we divide by three to fit the map to the screen
      ctx.fillRect(((car_position_dictionary[x]["x"])+15)/3, ((car_position_dictionary[x]["z"])-15)/3, 30, 30);
      // Since we are
      ctx.stroke();
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
      var cars_lap_data   = data.lapData[i].carPosition;
      let car_name        = "Car"+(i+1).toString();
      car_position_elements_dictionary[car_name].innerHTML = JSON.stringify(cars_lap_data, null);
      current_leaderboard[cars_lap_data-1] = i

      // If previous leaderboard does not match up with current leaderboard, then make sure we set our boolean so
      if (current_leaderboard[cars_lap_data-1] != previous_leaderboard[cars_lap_data-1]){
        similar_leaderboars = false;
      }
    }

    // If our boolean for similar leaderboards is false, then update the previous leaderboard, and the standings in the webpage
    if (similar_leaderboars == false){

      // set the previous_leaderboard to the current one since we now have a change
      previous_leaderboard = current_leaderboard;

      let car_elements = [];
      let car_position_container = document.querySelector('.grid-container');
      // Add each row to the array
      car_position_container.querySelectorAll('.car').forEach(el => car_elements.push(el));
      // Clear the container
      car_position_container.innerHTML = '';
      // Sort the array from highest to lowest
      car_elements.sort((a, b) => a.querySelector('.position').textContent - b.querySelector('.position').textContent);
      // Put the elements back into the container
      car_elements.forEach(e => car_position_container.appendChild(e));
    }
  }
}
