// connect to websocket
var ws = new WebSocket('ws://localhost:9090/ws');

// Header
var packetFormat = document.getElementById('packetFormat');
var packetVersion = document.getElementById('packetVersion');
var packetId = document.getElementById('packetId');
var sessionUID = document.getElementById('sessionUID');
var sessionTime = document.getElementById('sessionTime');
var frameIdentifier = document.getElementById('frameIdentifier');
var playerCarIndex = document.getElementById('playerCarIndex');
var pos_x = document.getElementById('pos_x');
var pos_y = document.getElementById('pos_y');
var pos_z = document.getElementById('pos_z');

var canvas = document.getElementById("packet_canvas");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var ctx = canvas.getContext("2d");
var canvas_height = canvas.height;
var canvas_width = canvas.width;
ctx.translate(canvas_width/2, canvas_height/2);
console.log(canvas_width/2, canvas_height/2)


ws.onmessage = function(event){
  var data =  JSON.parse(event.data);
  // console.log(data, JSON.parse(data))
  // var span = document.getElementById('packet');
  // span.innerHTML = JSON.stringify(data.header, null, 2);

  packetFormat.innerHTML = JSON.stringify(data.header.packetFormat, null);
  packetVersion.innerHTML = JSON.stringify(data.header.packetVersion, null);
  packetId.innerHTML = JSON.stringify(data.header.packetId, null);
  sessionUID.innerHTML = JSON.stringify(data.header.sessionUID, null);
  sessionTime.innerHTML = JSON.stringify(data.header.sessionTime, null);
  frameIdentifier.innerHTML = JSON.stringify(data.header.frameIdentifier, null);
  playerCarIndex.innerHTML = JSON.stringify(data.header.playerCarIndex, null);



  if (data.header.packetId == 0){

    pos_x.innerHTML = JSON.stringify(data.carMotionData.worldPositionX, null);
    pos_y.innerHTML = JSON.stringify(data.carMotionData.worldPositionY, null);
    pos_z.innerHTML = JSON.stringify(data.carMotionData.worldPositionZ, null);

    var x = data.carMotionData.worldPositionX;
    var y = data.carMotionData.worldPositionY;
    var z = data.carMotionData.worldPositionZ;

    drawCar(ctx, x/3, y/3, z/3);

    function drawCar(ctx, x, y, z) {
      // console.log('drawingcar');
      // ctx.beginPath();
      ctx.clearRect(0-(canvas_width/2), 0-(canvas_height/2), canvas.width, canvas.height);
      // ctx.stroke();

      ctx.lineWidth = "4";
      ctx.strokeStyle = "green";
      ctx.beginPath();
      ctx.rect(x+15, z-15, 30, 30);
      ctx.stroke();
    }

  }
}
