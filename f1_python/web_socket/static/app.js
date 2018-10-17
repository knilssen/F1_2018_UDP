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
// Telemetry
var speed = document.getElementById('speed');
var throttle = document.getElementById('throttle');
var steer = document.getElementById('steer');
var brake = document.getElementById('brake');
var clutch = document.getElementById('clutch');
var gear = document.getElementById('gear');
var engineRPM = document.getElementById('engineRPM');
var drs = document.getElementById('drs');
var revLightsPercent = document.getElementById('revLightsPercent');
var engineTemperature = document.getElementById('engineTemperature');
var brakesTemperatureRL = document.getElementById('brakesTemperatureRL');
var brakesTemperatureRR = document.getElementById('brakesTemperatureRR');
var brakesTemperatureFL = document.getElementById('brakesTemperatureFL');
var brakesTemperatureFR = document.getElementById('brakesTemperatureFR');
var tyresSurfaceTemperatureRL = document.getElementById('tyresSurfaceTemperatureRL');
var tyresSurfaceTemperatureRR = document.getElementById('tyresSurfaceTemperatureRR');
var tyresSurfaceTemperatureFL = document.getElementById('tyresSurfaceTemperatureFL');
var tyresSurfaceTemperatureFR = document.getElementById('tyresSurfaceTemperatureFR');
var tyresInnerTemperatureRL = document.getElementById('tyresInnerTemperatureRL');
var tyresInnerTemperatureRR = document.getElementById('tyresInnerTemperatureRR');
var tyresInnerTemperatureFL = document.getElementById('tyresInnerTemperatureFL');
var tyresInnerTemperatureFR = document.getElementById('tyresInnerTemperatureFR');
var tyresPressureRL = document.getElementById('tyresPressureRL');
var tyresPressureRR = document.getElementById('tyresPressureRR');
var tyresPressureFL = document.getElementById('tyresPressureFL');
var tyresPressureFR = document.getElementById('tyresPressureFR');
var buttonStatus = document.getElementById('buttonStatus');
// Motion Data
var worldPositionX = document.getElementById('worldPositionX');
var worldPositionY = document.getElementById('worldPositionY');
var worldPositionZ = document.getElementById('worldPositionZ');
var worldVelocityX = document.getElementById('worldVelocityX');
var worldVelocityY = document.getElementById('worldVelocityY');
var worldVelocityZ = document.getElementById('worldVelocityZ');
var worldForwardDirX = document.getElementById('worldForwardDirX');
var worldForwardDirY = document.getElementById('worldForwardDirY');
var worldForwardDirZ = document.getElementById('worldForwardDirZ');
var worldRightDirX = document.getElementById('worldRightDirX');
var worldRightDirY = document.getElementById('worldRightDirY');
var worldRightDirZ = document.getElementById('worldRightDirZ');
var gForceLateral = document.getElementById('gForceLateral');
var gForceLongitudinal = document.getElementById('gForceLongitudinal');
var gForceVertical = document.getElementById('gForceVertical');
var yaw = document.getElementById('yaw');
var pitch = document.getElementById('pitch');
var roll = document.getElementById('roll');
var suspensionPositionRL = document.getElementById('suspensionPositionRL');
var suspensionPositionRR = document.getElementById('suspensionPositionRR');
var suspensionPositionFL = document.getElementById('suspensionPositionFL');
var suspensionPositionFR = document.getElementById('suspensionPositionFR');
var suspensionVelocityRL = document.getElementById('suspensionVelocityRL');
var suspensionVelocityRR = document.getElementById('suspensionVelocityRR');
var suspensionVelocityFL = document.getElementById('suspensionVelocityFL');
var suspensionVelocityFR = document.getElementById('suspensionVelocityFR');
var suspensionAccelerationRL = document.getElementById('suspensionAccelerationRL');
var suspensionAccelerationRR = document.getElementById('suspensionAccelerationRR');
var suspensionAccelerationFL = document.getElementById('suspensionAccelerationFL');
var suspensionAccelerationFR = document.getElementById('suspensionAccelerationFR');
var wheelSpeedRL = document.getElementById('wheelSpeedRL');
var wheelSpeedRR = document.getElementById('wheelSpeedRR');
var wheelSpeedFL = document.getElementById('wheelSpeedFL');
var wheelSpeedFR = document.getElementById('wheelSpeedFR');
var wheelSlipRL = document.getElementById('wheelSlipRL');
var wheelSlipRR = document.getElementById('wheelSlipRR');
var wheelSlipFL = document.getElementById('wheelSlipFL');
var wheelSlipFR = document.getElementById('wheelSlipFR');
var localVelocityX = document.getElementById('localVelocityX');
var localVelocityY = document.getElementById('localVelocityY');
var localVelocityZ = document.getElementById('localVelocityZ');
var angularVelocityX = document.getElementById('angularVelocityX');
var angularVelocityY = document.getElementById('angularVelocityY');
var angularVelocityZ = document.getElementById('angularVelocityZ');
var angularAccelerationX = document.getElementById('angularAccelerationX');
var angularAccelerationY = document.getElementById('angularAccelerationY');
var angularAccelerationZ = document.getElementById('angularAccelerationZ');
var frontWheelsAngle = document.getElementById('frontWheelsAngle');


// when a new message has been received
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

   var players_car = data.header.packetId

   switch(players_car) {
     case 0:
       worldPositionX.innerHTML = JSON.stringify(data.carMotionData[players_car].worldPositionX, null);
       worldPositionY.innerHTML = JSON.stringify(data.carMotionData[players_car].worldPositionY, null);
       worldPositionZ.innerHTML = JSON.stringify(data.carMotionData[players_car].worldPositionZ, null);
       worldVelocityX.innerHTML = JSON.stringify(data.carMotionData[players_car].worldVelocityX, null);
       worldVelocityY.innerHTML = JSON.stringify(data.carMotionData[players_car].worldVelocityY, null);
       worldVelocityZ.innerHTML = JSON.stringify(data.carMotionData[players_car].worldVelocityZ, null);
       worldForwardDirX.innerHTML = JSON.stringify(data.carMotionData[players_car].worldForwardDirX, null);
       worldForwardDirY.innerHTML = JSON.stringify(data.carMotionData[players_car].worldForwardDirY, null);
       worldForwardDirZ.innerHTML = JSON.stringify(data.carMotionData[players_car].worldForwardDirZ, null);
       worldRightDirX.innerHTML = JSON.stringify(data.carMotionData[players_car].worldRightDirX, null);
       worldRightDirY.innerHTML = JSON.stringify(data.carMotionData[players_car].worldRightDirY, null);
       worldRightDirZ.innerHTML = JSON.stringify(data.carMotionData[players_car].worldRightDirZ, null);
       gForceLateral.innerHTML = JSON.stringify(data.carMotionData[players_car].gForceLateral, null);
       gForceLongitudinal.innerHTML = JSON.stringify(data.carMotionData[players_car].gForceLongitudinal, null);
       gForceVertical.innerHTML = JSON.stringify(data.carMotionData[players_car].gForceVertical, null);
       yaw.innerHTML = JSON.stringify(data.carMotionData[players_car].yaw, null);
       pitch.innerHTML = JSON.stringify(data.carMotionData[players_car].pitch, null);
       roll.innerHTML = JSON.stringify(data.carMotionData[players_car].roll, null);
       suspensionPositionRL.innerHTML = JSON.stringify(data.suspensionPosition.RL, null);
       suspensionPositionRR.innerHTML = JSON.stringify(data.suspensionPosition.RR, null);
       suspensionPositionFL.innerHTML = JSON.stringify(data.suspensionPosition.FL, null);
       suspensionPositionFR.innerHTML = JSON.stringify(data.suspensionPosition.FR, null);
       suspensionVelocityRL.innerHTML = JSON.stringify(data.suspensionVelocity.FL, null);
       suspensionVelocityRR.innerHTML = JSON.stringify(data.suspensionVelocity.RR, null);
       suspensionVelocityFL.innerHTML = JSON.stringify(data.suspensionVelocity.FL, null);
       suspensionVelocityFR.innerHTML = JSON.stringify(data.suspensionVelocity.FR, null);
       suspensionAccelerationRL.innerHTML = JSON.stringify(data.suspensionAcceleration.RL, null);
       suspensionAccelerationRR.innerHTML = JSON.stringify(data.suspensionAcceleration.RR, null);
       suspensionAccelerationFL.innerHTML = JSON.stringify(data.suspensionAcceleration.FL, null);
       suspensionAccelerationFR.innerHTML = JSON.stringify(data.suspensionAcceleration.FR, null);
       wheelSpeedRL.innerHTML = JSON.stringify(data.wheelSpeed.RL, null);
       wheelSpeedRR.innerHTML = JSON.stringify(data.wheelSpeed.RR, null);
       wheelSpeedFL.innerHTML = JSON.stringify(data.wheelSpeed.FL, null);
       wheelSpeedFR.innerHTML = JSON.stringify(data.wheelSpeed.FR, null);
       wheelSlipRL.innerHTML = JSON.stringify(data.wheelSlip.RL, null);
       wheelSlipRR.innerHTML = JSON.stringify(data.wheelSlip.RR, null);
       wheelSlipFL.innerHTML = JSON.stringify(data.wheelSlip.FL, null);
       wheelSlipFR.innerHTML = JSON.stringify(data.wheelSlip.FR, null);
       localVelocityX.innerHTML = JSON.stringify(data.localVelocityX, null);
       localVelocityY.innerHTML = JSON.stringify(data.localVelocityY, null);
       localVelocityZ.innerHTML = JSON.stringify(data.localVelocityZ, null);
       angularVelocityX.innerHTML = JSON.stringify(data.angularVelocityX, null);
       angularVelocityY.innerHTML = JSON.stringify(data.angularVelocityY, null);
       angularVelocityZ.innerHTML = JSON.stringify(data.angularVelocityZ, null);
       angularAccelerationX.innerHTML = JSON.stringify(data.angularAccelerationX, null);
       angularAccelerationY.innerHTML = JSON.stringify(data.angularAccelerationY, null);
       angularAccelerationZ.innerHTML = JSON.stringify(data.angularAccelerationZ, null);
       frontWheelsAngle.innerHTML = JSON.stringify(data.frontWheelsAngle, null);
      // break;
    // case 1:
    //   break;
    // case 2:
    //   break;
    // case 3:
    //   break;
    // case 4:
    //   break;
    // case 5:
    //   break;
    case 6:
      speed.innerHTML = JSON.stringify(data.carTelemetryData[players_car].speed, null);
      throttle.innerHTML = JSON.stringify(data.carTelemetryData[players_car].throttle, null);
      steer.innerHTML = JSON.stringify(data.carTelemetryData[players_car].steer, null);
      brake.innerHTML = JSON.stringify(data.carTelemetryData[players_car].brake, null);
      clutch.innerHTML = JSON.stringify(data.carTelemetryData[players_car].clutch, null);
      gear.innerHTML = JSON.stringify(data.carTelemetryData[players_car].gear, null);
      engineRPM.innerHTML = JSON.stringify(data.carTelemetryData[players_car].engineRPM, null);
      drs.innerHTML = JSON.stringify(data.carTelemetryData[players_car].drs, null);
      revLightsPercent.innerHTML = JSON.stringify(data.carTelemetryData[players_car].revLightsPercent, null);
      engineTemperature.innerHTML = JSON.stringify(data.carTelemetryData[players_car].engineTemperature, null);
      brakesTemperatureRL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].brakesTemperature.RL, null);
      brakesTemperatureRR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].brakesTemperature.RR, null);
      brakesTemperatureFL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].brakesTemperature.FL, null);
      brakesTemperatureFR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].brakesTemperature.FR, null);
      tyresSurfaceTemperatureRL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresSurfaceTemperature.RL, null);
      tyresSurfaceTemperatureRR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresSurfaceTemperature.RR, null);
      tyresSurfaceTemperatureFL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresSurfaceTemperature.FL, null);
      tyresSurfaceTemperatureFR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresSurfaceTemperature.FR, null);
      tyresInnerTemperatureRL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresInnerTemperature.RL, null);
      tyresInnerTemperatureRR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresInnerTemperature.RR, null);
      tyresInnerTemperatureFL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresInnerTemperature.FL, null);
      tyresInnerTemperatureFR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresInnerTemperature.FR, null);
      tyresPressureRL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresPressure.RL, null);
      tyresPressureRR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresPressure.RR, null);
      tyresPressureFL.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresPressure.FL, null);
      tyresPressureFR.innerHTML = JSON.stringify(data.carTelemetryData[players_car].tyresPressure.FR, null);
      buttonStatus.innerHTML = JSON.stringify(data.buttonStatus, null);
      // break;
    // case 7:
      // break;
    // default:
    //   break

  }
}
