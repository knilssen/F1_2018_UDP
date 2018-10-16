#
#
# Takes the structs required for the udp data and turns them into json objects to
# pass through our websocket to the webpage for viewing
#
# To increase efficiancy, we can only grab the data from our car like line 25 ->
#           'worldPositionX': packet.m_carMotionData[0].m_worldPositionX,
#          Would look like:
#           'worldPositionX': packet.m_carMotionData[packet.m_header.m_playerCarIndex].m_worldPositionX,
#
#

import json



def MotionData(packet):
    motion_data_json = {
    'packetFormat': packet.m_header.m_packetFormat,
    'packetVersion': packet.m_header.m_packetVersion,
    'packetId': packet.m_header.m_packetId,
    'sessionUID': packet.m_header.m_sessionUID,
    'sessionTime': packet.m_header.m_sessionTime,
    'frameIdentifier': packet.m_header.m_frameIdentifier,
    'playerCarIndex': packet.m_header.m_playerCarIndex,
    'carMotionData': [
        {
            'worldPositionX': packet.m_carMotionData[0].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[0].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[0].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[0].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[0].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[0].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[0].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[0].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[0].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[0].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[0].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[0].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[0].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[0].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[0].m_gForceVertical,
            'yaw': packet.m_carMotionData[0].m_yaw,
            'pitch': packet.m_carMotionData[0].m_pitch,
            'roll': packet.m_carMotionData[0].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[1].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[1].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[1].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[1].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[1].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[1].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[1].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[1].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[1].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[1].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[1].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[1].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[1].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[1].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[1].m_gForceVertical,
            'yaw': packet.m_carMotionData[1].m_yaw,
            'pitch': packet.m_carMotionData[1].m_pitch,
            'roll': packet.m_carMotionData[1].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[2].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[2].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[2].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[2].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[2].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[2].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[2].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[2].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[2].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[2].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[2].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[2].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[2].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[2].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[2].m_gForceVertical,
            'yaw': packet.m_carMotionData[2].m_yaw,
            'pitch': packet.m_carMotionData[2].m_pitch,
            'roll': packet.m_carMotionData[2].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[3].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[3].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[3].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[3].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[3].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[3].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[3].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[3].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[3].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[3].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[3].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[3].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[3].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[3].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[3].m_gForceVertical,
            'yaw': packet.m_carMotionData[3].m_yaw,
            'pitch': packet.m_carMotionData[3].m_pitch,
            'roll': packet.m_carMotionData[3].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[4].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[4].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[4].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[4].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[4].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[4].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[4].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[4].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[4].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[4].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[4].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[4].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[4].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[4].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[4].m_gForceVertical,
            'yaw': packet.m_carMotionData[4].m_yaw,
            'pitch': packet.m_carMotionData[4].m_pitch,
            'roll': packet.m_carMotionData[4].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[5].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[5].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[5].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[5].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[5].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[5].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[5].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[5].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[5].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[5].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[5].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[5].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[5].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[5].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[5].m_gForceVertical,
            'yaw': packet.m_carMotionData[5].m_yaw,
            'pitch': packet.m_carMotionData[5].m_pitch,
            'roll': packet.m_carMotionData[5].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[6].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[6].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[6].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[6].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[6].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[6].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[6].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[6].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[6].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[6].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[6].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[6].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[6].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[6].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[6].m_gForceVertical,
            'yaw': packet.m_carMotionData[6].m_yaw,
            'pitch': packet.m_carMotionData[6].m_pitch,
            'roll': packet.m_carMotionData[6].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[7].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[7].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[7].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[7].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[7].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[7].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[7].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[7].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[7].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[7].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[7].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[7].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[7].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[7].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[7].m_gForceVertical,
            'yaw': packet.m_carMotionData[7].m_yaw,
            'pitch': packet.m_carMotionData[7].m_pitch,
            'roll': packet.m_carMotionData[7].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[8].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[8].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[8].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[8].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[8].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[8].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[8].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[8].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[8].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[8].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[8].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[8].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[8].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[8].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[8].m_gForceVertical,
            'yaw': packet.m_carMotionData[8].m_yaw,
            'pitch': packet.m_carMotionData[8].m_pitch,
            'roll': packet.m_carMotionData[8].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[9].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[9].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[9].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[9].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[9].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[9].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[9].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[9].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[9].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[9].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[9].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[9].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[9].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[9].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[9].m_gForceVertical,
            'yaw': packet.m_carMotionData[9].m_yaw,
            'pitch': packet.m_carMotionData[9].m_pitch,
            'roll': packet.m_carMotionData[9].m_roll,
        },
        {
            'worldPositionX': packet.m_carMotionData[10].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[10].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[10].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[10].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[10].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[10].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[10].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[10].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[10].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[10].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[10].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[10].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[10].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[10].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[10].m_gForceVertical,
            'yaw': packet.m_carMotionData[10].m_yaw,
            'pitch': packet.m_carMotionData[10].m_pitch,
            'roll': packet.m_carMotionData[10].m_roll,
        },
        {
            'worldPositionX': packet.m_carMotionData[11].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[11].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[11].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[11].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[11].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[11].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[11].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[11].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[11].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[11].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[11].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[11].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[11].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[11].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[11].m_gForceVertical,
            'yaw': packet.m_carMotionData[11].m_yaw,
            'pitch': packet.m_carMotionData[11].m_pitch,
            'roll': packet.m_carMotionData[11].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[12].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[12].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[12].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[12].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[12].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[12].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[12].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[12].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[12].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[12].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[12].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[12].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[12].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[12].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[12].m_gForceVertical,
            'yaw': packet.m_carMotionData[12].m_yaw,
            'pitch': packet.m_carMotionData[12].m_pitch,
            'roll': packet.m_carMotionData[12].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[13].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[13].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[13].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[13].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[13].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[13].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[13].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[13].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[13].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[13].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[13].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[13].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[13].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[13].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[13].m_gForceVertical,
            'yaw': packet.m_carMotionData[13].m_yaw,
            'pitch': packet.m_carMotionData[13].m_pitch,
            'roll': packet.m_carMotionData[13].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[14].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[14].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[14].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[14].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[14].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[14].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[14].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[14].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[14].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[14].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[14].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[14].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[14].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[14].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[14].m_gForceVertical,
            'yaw': packet.m_carMotionData[14].m_yaw,
            'pitch': packet.m_carMotionData[14].m_pitch,
            'roll': packet.m_carMotionData[14].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[15].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[15].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[15].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[15].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[15].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[15].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[15].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[15].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[15].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[15].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[15].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[15].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[15].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[15].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[15].m_gForceVertical,
            'yaw': packet.m_carMotionData[15].m_yaw,
            'pitch': packet.m_carMotionData[15].m_pitch,
            'roll': packet.m_carMotionData[15].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[16].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[16].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[16].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[16].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[16].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[16].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[16].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[16].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[16].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[16].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[16].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[16].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[16].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[16].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[16].m_gForceVertical,
            'yaw': packet.m_carMotionData[16].m_yaw,
            'pitch': packet.m_carMotionData[16].m_pitch,
            'roll': packet.m_carMotionData[16].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[17].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[17].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[17].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[17].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[17].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[17].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[17].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[17].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[17].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[17].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[17].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[17].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[17].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[17].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[17].m_gForceVertical,
            'yaw': packet.m_carMotionData[17].m_yaw,
            'pitch': packet.m_carMotionData[17].m_pitch,
            'roll': packet.m_carMotionData[17].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[18].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[18].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[18].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[18].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[18].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[18].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[18].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[18].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[18].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[18].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[18].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[18].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[18].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[18].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[18].m_gForceVertical,
            'yaw': packet.m_carMotionData[18].m_yaw,
            'pitch': packet.m_carMotionData[18].m_pitch,
            'roll': packet.m_carMotionData[18].m_roll
        },
        {
            'worldPositionX': packet.m_carMotionData[19].m_worldPositionX,
            'worldPositionY': packet.m_carMotionData[19].m_worldPositionY,
            'worldPositionZ': packet.m_carMotionData[19].m_worldPositionZ,
            'worldVelocityX': packet.m_carMotionData[19].m_worldVelocityX,
            'worldVelocityY': packet.m_carMotionData[19].m_worldVelocityY,
            'worldVelocityZ': packet.m_carMotionData[19].m_worldVelocityZ,
            'worldForwardDirX': packet.m_carMotionData[19].m_worldForwardDirX,
            'worldForwardDirY': packet.m_carMotionData[19].m_worldForwardDirY,
            'worldForwardDirZ': packet.m_carMotionData[19].m_worldForwardDirZ,
            'worldRightDirX': packet.m_carMotionData[19].m_worldRightDirX,
            'worldRightDirY': packet.m_carMotionData[19].m_worldRightDirY,
            'worldRightDirZ': packet.m_carMotionData[19].m_worldRightDirZ,
            'gForceLateral': packet.m_carMotionData[19].m_gForceLateral,
            'gForceLongitudinal': packet.m_carMotionData[19].m_gForceLongitudinal,
            'gForceVertical': packet.m_carMotionData[19].m_gForceVertical,
            'yaw': packet.m_carMotionData[19].m_yaw,
            'pitch': packet.m_carMotionData[19].m_pitch,
            'roll': packet.m_carMotionData[19].m_roll
        }
    ],
    'suspensionPosition':{
        'RL': packet.m_suspensionPosition[0],
        'RR': packet.m_suspensionPosition[1],
        'FL': packet.m_suspensionPosition[2],
        'FR': packet.m_suspensionPosition[3]
    },
    'suspensionVelocity':{
        'RL': packet.m_suspensionVelocity[0],
        'RR': packet.m_suspensionVelocity[1],
        'FL': packet.m_suspensionVelocity[2],
        'FR': packet.m_suspensionVelocity[3]
    },
    'suspensionAcceleration':{
        'RL': packet.m_suspensionAcceleration[0],
        'RR': packet.m_suspensionAcceleration[1],
        'FL': packet.m_suspensionAcceleration[2],
        'FR': packet.m_suspensionAcceleration[3]
    },
    'wheelSpeed':{
        'RL': packet.m_wheelSpeed[0],
        'RR': packet.m_wheelSpeed[1],
        'FL': packet.m_wheelSpeed[2],
        'FR': packet.m_wheelSpeed[3]
    },
    'wheelSlip':{
        'RL': packet.m_wheelSlip[0],
        'RR': packet.m_wheelSlip[1],
        'FL': packet.m_wheelSlip[2],
        'FR': packet.m_wheelSlip[3]
    },
    'localVelocityX': packet.m_localVelocityX,
    'localVelocityY': packet.m_localVelocityY,
    'localVelocityZ': packet.m_localVelocityZ,
    'angularVelocityX': packet.m_angularVelocityX,
    'angularVelocityY': packet.m_angularVelocityY,
    'angularVelocityZ': packet.m_angularVelocityZ,
    'angularAccelerationX': packet.m_angularAccelerationX,
    'angularAccelerationY': packet.m_angularAccelerationY,
    'angularAccelerationZ': packet.m_angularAccelerationZ,
    'frontWheelsAngle': packet.m_frontWheelsAngle
    }

    return motion_data_json


def SessionData(packet):
    weather_types = ['clear', 'light cloud', 'overcast', 'light rain', 'heavy rain', 'storm']
    session_types = ['unknown', 'P1', 'P2', 'P3', 'Short P', 'Q1', 'Q2', 'Q3', 'Short Q', 'OSQ', 'R', 'R2', 'Time Trial']
    track_types = ['Melbourne', 'Paul Ricard', 'Shanghai', 'Sakhir (Bahrain)', 'Catalunya', 'Monaco', 'Montreal', 'Silverstone', 'Hockenheim', 'Hungaroring',
                    'Spa', 'Monza', 'Singapore', 'Suzuka', 'Abu Dhabi', 'Texas', 'Brazil', 'Austria', 'Sochi', 'Mexico', 'Baku (Azerbaijan)', 'Sakhir Short',
                    'Silverstone Short', 'Texas Short', 'Suzuka Short']
    era_types = ['modern', 'classic']
    SLI_pro_support_type = ['inactive', 'active']
    zone_flag_types = ['none', 'green', 'blue', 'yellow', 'red']
    safety_car_types = ['no safety car', 'full safety car', 'virtual safety car']
    network_game_types = ['offline', 'online']

    session_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'weather': packet.m_weather,     # Weather - 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy rain, 5 = storm
    'trackTemperature': packet.m_trackTemperature,
    'airTemperature': packet.m_airTemperature,
    'totalLaps': packet.m_totalLaps,
    'trackLength': packet.m_trackLength,
    'sessionType': packet.m_sessionType, # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2, 12 = Time Trial
    'trackId': packet.m_trackId,  # -1 for unknown, 0-21 for tracks, see appendix
    'era': packet.m_era, # Era, 0 = modern, 1 = classic
    'sessionTimeLeft': packet.m_sessionTimeLeft,
    'sessionDuration': packet.m_sessionDuration,
    'pitSpeedLimit': packet.m_pitSpeedLimit,
    'gamePaused': packet.m_gamePaused,
    'isSpectating': packet.m_isSpectating,
    'spectatorCarIndex': packet.m_spectatorCarIndex,
    'sliProNativeSupport': packet.m_sliProNativeSupport,  # SLI Pro support, 0 = inactive, 1 = active
    'numMarshalZones': packet.m_numMarshalZones,
    'marshalZones': [
        {
            'zoneStart': packet.m_marshalZones[0].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[0].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[1].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[1].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[2].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[2].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[3].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[3].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[4].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[4].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[5].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[5].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[6].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[6].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[7].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[7].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[8].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[8].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[9].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[9].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[10].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[10].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[11].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[11].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[12].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[12].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[13].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[13].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[14].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[14].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[15].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[15].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[16].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[16].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[17].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[17].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[18].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[18].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[19].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[19].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        },
        {
            'zoneStart': packet.m_marshalZones[20].m_zoneStart,
            'zoneFlag': packet.m_marshalZones[20].m_zoneFlag, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        }
    ],
    'safetyCarStatus': safety_car_types[packet.m_safetyCarStatus], # 0 = no safety car, 1 = full safety car, 2 = virtual safety car
    'networkGame': network_game_types[packet.m_networkGame] # 0 = offline, 1 = online
    }

    return session_data_json


def LapData(packet):
    pit_status_types = ['none', 'pitting', 'in pit area']
    sector_types = ['sector1', 'sector2', 'sector3']
    current_lap_invalid_types = ['valid', 'invalid']
    driver_status_types = ['in garage', 'flying lap', 'in lap', 'out lap', 'on track']
    result_status_types = ['invalid', 'inactive', 'active', 'finished', 'disqualified', 'not classified', 'retired']

    lap_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'lapData': [
        {
        'lastLapTime': packet.m_lapData[0].m_lastLapTime,
        'currentLapTime': packet.m_lapData[0].m_currentLapTime,
        'bestLapTime': packet.m_lapData[0].m_bestLapTime,
        'sector1Time': packet.m_lapData[0].m_sector1Time,
        'sector2Time': packet.m_lapData[0].m_sector2Time,
        'lapDistance': packet.m_lapData[0].m_lapDistance,
        'totalDistance': packet.m_lapData[0].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[0].m_safetyCarDelta,
        'carPosition': packet.m_lapData[0].m_carPosition,
        'currentLapNum': packet.m_lapData[0].m_currentLapNum,
        'pitStatus': packet.m_lapData[0].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[0].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[0].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[0].m_penalties,
        'gridPosition': packet.m_lapData[0].m_gridPosition,
        'driverStatus': packet.m_lapData[0].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[0].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[1].m_lastLapTime,
        'currentLapTime': packet.m_lapData[1].m_currentLapTime,
        'bestLapTime': packet.m_lapData[1].m_bestLapTime,
        'sector1Time': packet.m_lapData[1].m_sector1Time,
        'sector2Time': packet.m_lapData[1].m_sector2Time,
        'lapDistance': packet.m_lapData[1].m_lapDistance,
        'totalDistance': packet.m_lapData[1].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[1].m_safetyCarDelta,
        'carPosition': packet.m_lapData[1].m_carPosition,
        'currentLapNum': packet.m_lapData[1].m_currentLapNum,
        'pitStatus': packet.m_lapData[1].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[1].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[1].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[1].m_penalties,
        'gridPosition': packet.m_lapData[1].m_gridPosition,
        'driverStatus': packet.m_lapData[1].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[1].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[2].m_lastLapTime,
        'currentLapTime': packet.m_lapData[2].m_currentLapTime,
        'bestLapTime': packet.m_lapData[2].m_bestLapTime,
        'sector1Time': packet.m_lapData[2].m_sector1Time,
        'sector2Time': packet.m_lapData[2].m_sector2Time,
        'lapDistance': packet.m_lapData[2].m_lapDistance,
        'totalDistance': packet.m_lapData[2].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[2].m_safetyCarDelta,
        'carPosition': packet.m_lapData[2].m_carPosition,
        'currentLapNum': packet.m_lapData[2].m_currentLapNum,
        'pitStatus': packet.m_lapData[2].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[2].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[2].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[2].m_penalties,
        'gridPosition': packet.m_lapData[2].m_gridPosition,
        'driverStatus': packet.m_lapData[2].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[2].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[3].m_lastLapTime,
        'currentLapTime': packet.m_lapData[3].m_currentLapTime,
        'bestLapTime': packet.m_lapData[3].m_bestLapTime,
        'sector1Time': packet.m_lapData[3].m_sector1Time,
        'sector2Time': packet.m_lapData[3].m_sector2Time,
        'lapDistance': packet.m_lapData[3].m_lapDistance,
        'totalDistance': packet.m_lapData[3].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[3].m_safetyCarDelta,
        'carPosition': packet.m_lapData[3].m_carPosition,
        'currentLapNum': packet.m_lapData[3].m_currentLapNum,
        'pitStatus': packet.m_lapData[3].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[3].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[3].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[3].m_penalties,
        'gridPosition': packet.m_lapData[3].m_gridPosition,
        'driverStatus': packet.m_lapData[3].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[3].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[4].m_lastLapTime,
        'currentLapTime': packet.m_lapData[4].m_currentLapTime,
        'bestLapTime': packet.m_lapData[4].m_bestLapTime,
        'sector1Time': packet.m_lapData[4].m_sector1Time,
        'sector2Time': packet.m_lapData[4].m_sector2Time,
        'lapDistance': packet.m_lapData[4].m_lapDistance,
        'totalDistance': packet.m_lapData[4].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[4].m_safetyCarDelta,
        'carPosition': packet.m_lapData[4].m_carPosition,
        'currentLapNum': packet.m_lapData[4].m_currentLapNum,
        'pitStatus': packet.m_lapData[4].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[4].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[4].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[4].m_penalties,
        'gridPosition': packet.m_lapData[4].m_gridPosition,
        'driverStatus': packet.m_lapData[4].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[4].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[5].m_lastLapTime,
        'currentLapTime': packet.m_lapData[5].m_currentLapTime,
        'bestLapTime': packet.m_lapData[5].m_bestLapTime,
        'sector1Time': packet.m_lapData[5].m_sector1Time,
        'sector2Time': packet.m_lapData[5].m_sector2Time,
        'lapDistance': packet.m_lapData[5].m_lapDistance,
        'totalDistance': packet.m_lapData[5].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[5].m_safetyCarDelta,
        'carPosition': packet.m_lapData[5].m_carPosition,
        'currentLapNum': packet.m_lapData[5].m_currentLapNum,
        'pitStatus': packet.m_lapData[5].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[5].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[5].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[5].m_penalties,
        'gridPosition': packet.m_lapData[5].m_gridPosition,
        'driverStatus': packet.m_lapData[5].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[5].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[6].m_lastLapTime,
        'currentLapTime': packet.m_lapData[6].m_currentLapTime,
        'bestLapTime': packet.m_lapData[6].m_bestLapTime,
        'sector1Time': packet.m_lapData[6].m_sector1Time,
        'sector2Time': packet.m_lapData[6].m_sector2Time,
        'lapDistance': packet.m_lapData[6].m_lapDistance,
        'totalDistance': packet.m_lapData[6].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[6].m_safetyCarDelta,
        'carPosition': packet.m_lapData[6].m_carPosition,
        'currentLapNum': packet.m_lapData[6].m_currentLapNum,
        'pitStatus': packet.m_lapData[6].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[6].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[6].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[6].m_penalties,
        'gridPosition': packet.m_lapData[6].m_gridPosition,
        'driverStatus': packet.m_lapData[6].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[6].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[7].m_lastLapTime,
        'currentLapTime': packet.m_lapData[7].m_currentLapTime,
        'bestLapTime': packet.m_lapData[7].m_bestLapTime,
        'sector1Time': packet.m_lapData[7].m_sector1Time,
        'sector2Time': packet.m_lapData[7].m_sector2Time,
        'lapDistance': packet.m_lapData[7].m_lapDistance,
        'totalDistance': packet.m_lapData[7].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[7].m_safetyCarDelta,
        'carPosition': packet.m_lapData[7].m_carPosition,
        'currentLapNum': packet.m_lapData[7].m_currentLapNum,
        'pitStatus': packet.m_lapData[7].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[7].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[7].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[7].m_penalties,
        'gridPosition': packet.m_lapData[7].m_gridPosition,
        'driverStatus': packet.m_lapData[7].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[7].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[8].m_lastLapTime,
        'currentLapTime': packet.m_lapData[8].m_currentLapTime,
        'bestLapTime': packet.m_lapData[8].m_bestLapTime,
        'sector1Time': packet.m_lapData[8].m_sector1Time,
        'sector2Time': packet.m_lapData[8].m_sector2Time,
        'lapDistance': packet.m_lapData[8].m_lapDistance,
        'totalDistance': packet.m_lapData[8].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[8].m_safetyCarDelta,
        'carPosition': packet.m_lapData[8].m_carPosition,
        'currentLapNum': packet.m_lapData[8].m_currentLapNum,
        'pitStatus': packet.m_lapData[8].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[8].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[8].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[8].m_penalties,
        'gridPosition': packet.m_lapData[8].m_gridPosition,
        'driverStatus': packet.m_lapData[8].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[8].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[9].m_lastLapTime,
        'currentLapTime': packet.m_lapData[9].m_currentLapTime,
        'bestLapTime': packet.m_lapData[9].m_bestLapTime,
        'sector1Time': packet.m_lapData[9].m_sector1Time,
        'sector2Time': packet.m_lapData[9].m_sector2Time,
        'lapDistance': packet.m_lapData[9].m_lapDistance,
        'totalDistance': packet.m_lapData[9].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[9].m_safetyCarDelta,
        'carPosition': packet.m_lapData[9].m_carPosition,
        'currentLapNum': packet.m_lapData[9].m_currentLapNum,
        'pitStatus': packet.m_lapData[9].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[9].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[9].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[9].m_penalties,
        'gridPosition': packet.m_lapData[9].m_gridPosition,
        'driverStatus': packet.m_lapData[9].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[9].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[10].m_lastLapTime,
        'currentLapTime': packet.m_lapData[10].m_currentLapTime,
        'bestLapTime': packet.m_lapData[10].m_bestLapTime,
        'sector1Time': packet.m_lapData[10].m_sector1Time,
        'sector2Time': packet.m_lapData[10].m_sector2Time,
        'lapDistance': packet.m_lapData[10].m_lapDistance,
        'totalDistance': packet.m_lapData[10].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[10].m_safetyCarDelta,
        'carPosition': packet.m_lapData[10].m_carPosition,
        'currentLapNum': packet.m_lapData[10].m_currentLapNum,
        'pitStatus': packet.m_lapData[10].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[10].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[10].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[10].m_penalties,
        'gridPosition': packet.m_lapData[10].m_gridPosition,
        'driverStatus': packet.m_lapData[10].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[10].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[11].m_lastLapTime,
        'currentLapTime': packet.m_lapData[11].m_currentLapTime,
        'bestLapTime': packet.m_lapData[11].m_bestLapTime,
        'sector1Time': packet.m_lapData[11].m_sector1Time,
        'sector2Time': packet.m_lapData[11].m_sector2Time,
        'lapDistance': packet.m_lapData[11].m_lapDistance,
        'totalDistance': packet.m_lapData[11].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[11].m_safetyCarDelta,
        'carPosition': packet.m_lapData[11].m_carPosition,
        'currentLapNum': packet.m_lapData[11].m_currentLapNum,
        'pitStatus': packet.m_lapData[11].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[11].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[11].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[11].m_penalties,
        'gridPosition': packet.m_lapData[11].m_gridPosition,
        'driverStatus': packet.m_lapData[11].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[11].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[12].m_lastLapTime,
        'currentLapTime': packet.m_lapData[12].m_currentLapTime,
        'bestLapTime': packet.m_lapData[12].m_bestLapTime,
        'sector1Time': packet.m_lapData[12].m_sector1Time,
        'sector2Time': packet.m_lapData[12].m_sector2Time,
        'lapDistance': packet.m_lapData[12].m_lapDistance,
        'totalDistance': packet.m_lapData[12].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[12].m_safetyCarDelta,
        'carPosition': packet.m_lapData[12].m_carPosition,
        'currentLapNum': packet.m_lapData[12].m_currentLapNum,
        'pitStatus': packet.m_lapData[12].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[12].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[12].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[12].m_penalties,
        'gridPosition': packet.m_lapData[12].m_gridPosition,
        'driverStatus': packet.m_lapData[12].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[12].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[13].m_lastLapTime,
        'currentLapTime': packet.m_lapData[13].m_currentLapTime,
        'bestLapTime': packet.m_lapData[13].m_bestLapTime,
        'sector1Time': packet.m_lapData[13].m_sector1Time,
        'sector2Time': packet.m_lapData[13].m_sector2Time,
        'lapDistance': packet.m_lapData[13].m_lapDistance,
        'totalDistance': packet.m_lapData[13].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[13].m_safetyCarDelta,
        'carPosition': packet.m_lapData[13].m_carPosition,
        'currentLapNum': packet.m_lapData[13].m_currentLapNum,
        'pitStatus': packet.m_lapData[13].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[13].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[13].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[13].m_penalties,
        'gridPosition': packet.m_lapData[13].m_gridPosition,
        'driverStatus': packet.m_lapData[13].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[13].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[14].m_lastLapTime,
        'currentLapTime': packet.m_lapData[14].m_currentLapTime,
        'bestLapTime': packet.m_lapData[14].m_bestLapTime,
        'sector1Time': packet.m_lapData[14].m_sector1Time,
        'sector2Time': packet.m_lapData[14].m_sector2Time,
        'lapDistance': packet.m_lapData[14].m_lapDistance,
        'totalDistance': packet.m_lapData[14].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[14].m_safetyCarDelta,
        'carPosition': packet.m_lapData[14].m_carPosition,
        'currentLapNum': packet.m_lapData[14].m_currentLapNum,
        'pitStatus': packet.m_lapData[14].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[14].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[14].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[14].m_penalties,
        'gridPosition': packet.m_lapData[14].m_gridPosition,
        'driverStatus': packet.m_lapData[14].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[14].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[15].m_lastLapTime,
        'currentLapTime': packet.m_lapData[15].m_currentLapTime,
        'bestLapTime': packet.m_lapData[15].m_bestLapTime,
        'sector1Time': packet.m_lapData[15].m_sector1Time,
        'sector2Time': packet.m_lapData[15].m_sector2Time,
        'lapDistance': packet.m_lapData[15].m_lapDistance,
        'totalDistance': packet.m_lapData[15].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[15].m_safetyCarDelta,
        'carPosition': packet.m_lapData[15].m_carPosition,
        'currentLapNum': packet.m_lapData[15].m_currentLapNum,
        'pitStatus': packet.m_lapData[15].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[15].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[15].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[15].m_penalties,
        'gridPosition': packet.m_lapData[15].m_gridPosition,
        'driverStatus': packet.m_lapData[15].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[15].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[16].m_lastLapTime,
        'currentLapTime': packet.m_lapData[16].m_currentLapTime,
        'bestLapTime': packet.m_lapData[16].m_bestLapTime,
        'sector1Time': packet.m_lapData[16].m_sector1Time,
        'sector2Time': packet.m_lapData[16].m_sector2Time,
        'lapDistance': packet.m_lapData[16].m_lapDistance,
        'totalDistance': packet.m_lapData[16].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[16].m_safetyCarDelta,
        'carPosition': packet.m_lapData[16].m_carPosition,
        'currentLapNum': packet.m_lapData[16].m_currentLapNum,
        'pitStatus': packet.m_lapData[16].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[16].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[16].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[16].m_penalties,
        'gridPosition': packet.m_lapData[16].m_gridPosition,
        'driverStatus': packet.m_lapData[16].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[16].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[17].m_lastLapTime,
        'currentLapTime': packet.m_lapData[17].m_currentLapTime,
        'bestLapTime': packet.m_lapData[17].m_bestLapTime,
        'sector1Time': packet.m_lapData[17].m_sector1Time,
        'sector2Time': packet.m_lapData[17].m_sector2Time,
        'lapDistance': packet.m_lapData[17].m_lapDistance,
        'totalDistance': packet.m_lapData[17].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[17].m_safetyCarDelta,
        'carPosition': packet.m_lapData[17].m_carPosition,
        'currentLapNum': packet.m_lapData[17].m_currentLapNum,
        'pitStatus': packet.m_lapData[17].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[17].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[17].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[17].m_penalties,
        'gridPosition': packet.m_lapData[17].m_gridPosition,
        'driverStatus': packet.m_lapData[17].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[17].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[18].m_lastLapTime,
        'currentLapTime': packet.m_lapData[18].m_currentLapTime,
        'bestLapTime': packet.m_lapData[18].m_bestLapTime,
        'sector1Time': packet.m_lapData[18].m_sector1Time,
        'sector2Time': packet.m_lapData[18].m_sector2Time,
        'lapDistance': packet.m_lapData[18].m_lapDistance,
        'totalDistance': packet.m_lapData[18].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[18].m_safetyCarDelta,
        'carPosition': packet.m_lapData[18].m_carPosition,
        'currentLapNum': packet.m_lapData[18].m_currentLapNum,
        'pitStatus': packet.m_lapData[18].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[18].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[18].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[18].m_penalties,
        'gridPosition': packet.m_lapData[18].m_gridPosition,
        'driverStatus': packet.m_lapData[18].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[18].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        },
        {
        'lastLapTime': packet.m_lapData[19].m_lastLapTime,
        'currentLapTime': packet.m_lapData[19].m_currentLapTime,
        'bestLapTime': packet.m_lapData[19].m_bestLapTime,
        'sector1Time': packet.m_lapData[19].m_sector1Time,
        'sector2Time': packet.m_lapData[19].m_sector2Time,
        'lapDistance': packet.m_lapData[19].m_lapDistance,
        'totalDistance': packet.m_lapData[19].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[19].m_safetyCarDelta,
        'carPosition': packet.m_lapData[19].m_carPosition,
        'currentLapNum': packet.m_lapData[19].m_currentLapNum,
        'pitStatus': packet.m_lapData[19].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[19].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[19].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[19].m_penalties,
        'gridPosition': packet.m_lapData[19].m_gridPosition,
        'driverStatus': packet.m_lapData[19].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[19].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
        }
    ]
    }

    return lap_data_json


def EventData(packet):
    event_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'eventStringCode': str(packet.m_eventStringCode[0]) + str(packet.m_eventStringCode[1]) + str(packet.m_eventStringCode[2]) + str(packet.m_eventStringCode[3])
    }

    return event_data_json


def ParticipantData(packet):
    ai_controlled_types = ['Human', 'AI']
    driver_id_types = ['Carlos Sainz', '', 'Daniel Ricciardo', 'Fernando Alonso', '', '', 'Kimi Raikkonen', 'Lewis Hamilton', 'Marcus Ericsson', 'Max Verstappen',
                        'Nico Hulkenburg', 'Kevin Magnussen', 'Romain Grosjean', 'Sebastian Vettel', 'Sergio Perez', 'Valtteri Bottas', '', 'Esteban Ocon', 'Stoffel Vandoorne',
                        'Lance Stroll', 'Arron Barnes', 'Martin Giles', 'Alex Murray', 'Lucas Roth', 'Igor Correria', 'Sophie Levasseur', 'Jonas Schiffer', 'Alain Forest', 'Jay Letourneau',
                        'Esto Saari', 'Yasar Atiyeh', 'Callisto Calabresi', 'Naota Izum', 'Howard Clarke', 'Wilheim Kaufmann', 'Marie Laursen', 'Flavio Nieves', 'Peter Belousov',
                        'Klimek Michalski', 'Santiago Moreno', 'Benjamin Coppens', 'Noah Visser', 'Gert Waldmuller', 'Julian Quesada', 'Daniel Jones', '', '', '', '', '', '', '', '', '',
                        '', '', '', '', 'Charles Leclerc', 'Pierre Gasly', 'Brendon Hartley', 'Sergey Siroktin', '', '', '', '', '', '', '', 'Ruben Meijer', 'Rashid Nair', 'Jack Tremblay']
    team_id_types = ['Mercedes', 'Ferrari', 'Red Bull', 'Williams', 'Force India', 'Renault', 'Toro Rosso', 'Haas', 'McLaren', 'Sauber', 'McLaren 1988', 'McLaren 1991',
                    'Williams 1992', 'Ferrari 1995', 'Williams 1996', 'McLaren 1998', 'Ferrari 2002', 'Ferrari 2004', 'Renault 2006', 'Ferrari 2007', 'McLaren 2008', 'Red Bull 2008',
                    'Ferrari 1976', '', '', '', '', '', '', '', '', '', '', '', 'McLaren 1976', 'Lotus 1972', 'Ferrari 1979', 'McLaren 1982', 'Williams 2003', 'Brawn 2009', 'Lotus 1978']
    nationality_types = ['American', 'Argentinean', 'Australian', 'Austrian', 'Azerbaijani', 'Bahraini', 'Belgian', 'Bolivian', 'Brazilian', 'British', 'Bulgarian', 'Camaroonian', 'Canadian',
                        'Chilean', 'Chinese', 'Columbian', 'Costa Rican', 'Croatian', 'Cypriot', 'Czech', 'Danish', 'Dutch', 'Ecuadorian', 'English', 'Emirian', 'Estonian', 'Finnish', 'French',
                        'German', 'Ghanian', 'Greek', 'Guatamalan', 'Honduran', 'Hong Konger', 'Hungarian', 'Icelander', 'Indian', 'Indonesian', 'Irish', 'Israeli', 'Italian', 'Jamacian',
                        'Japanese', 'Jordanian', 'Kuwati', 'Latvian', 'Lebanese', 'Lithuanian', 'Luxembourger', 'Malasaysian', 'Maltese', 'Mexican', 'Monegasque', 'New Zelander',
                        'Nicuraguan', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Panamanian', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian',
                        'Russian', 'Salvadoran', 'Saudi', 'Scottish', 'Serbian', 'Singaporean', 'Slovakian', 'Slovenien', 'South Korea', 'South African', 'Spanish', 'Swedish', 'Swiss',
                        'Taiwanese', 'Thai', 'Turkish', 'Uruguayan', 'Ukrainian', 'Venezuelan', 'Welsh']

    participant_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'numCars': packet.m_numCars,
    'participants':[
        {
            'aiControlled': packet.m_participants[0].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[0].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[0].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[0].m_raceNumber,
            'nationality': packet.m_participants[0].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[0].m_name
        },
        {
            'aiControlled': packet.m_participants[1].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[1].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[1].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[1].m_raceNumber,
            'nationality': packet.m_participants[1].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[1].m_name
        },
        {
            'aiControlled': packet.m_participants[2].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[2].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[2].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[2].m_raceNumber,
            'nationality': packet.m_participants[2].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[2].m_name
        },
        {
            'aiControlled': packet.m_participants[3].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[3].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[3].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[3].m_raceNumber,
            'nationality': packet.m_participants[3].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[3].m_name
        },
        {
            'aiControlled': packet.m_participants[4].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[4].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[4].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[4].m_raceNumber,
            'nationality': packet.m_participants[4].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[4].m_name
        },
        {
            'aiControlled': packet.m_participants[5].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[5].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[5].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[5].m_raceNumber,
            'nationality': packet.m_participants[5].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[5].m_name
        },
        {
            'aiControlled': packet.m_participants[6].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[6].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[6].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[6].m_raceNumber,
            'nationality': packet.m_participants[6].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[6].m_name
        },
        {
            'aiControlled': packet.m_participants[7].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[7].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[7].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[7].m_raceNumber,
            'nationality': packet.m_participants[7].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[7].m_name
        },
        {
            'aiControlled': packet.m_participants[8].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[8].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[8].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[8].m_raceNumber,
            'nationality': packet.m_participants[8].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[8].m_name
        },
        {
            'aiControlled': packet.m_participants[9].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[9].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[9].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[9].m_raceNumber,
            'nationality': packet.m_participants[9].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[9].m_name
        },
        {
            'aiControlled': packet.m_participants[10].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[10].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[10].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[10].m_raceNumber,
            'nationality': packet.m_participants[10].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[10].m_name
        },
        {
            'aiControlled': packet.m_participants[11].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[11].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[11].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[11].m_raceNumber,
            'nationality': packet.m_participants[11].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[11].m_name
        },
        {
            'aiControlled': packet.m_participants[12].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[12].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[12].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[12].m_raceNumber,
            'nationality': packet.m_participants[12].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[12].m_name
        },
        {
            'aiControlled': packet.m_participants[13].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[13].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[13].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[13].m_raceNumber,
            'nationality': packet.m_participants[13].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[13].m_name
        },
        {
            'aiControlled': packet.m_participants[14].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[14].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[14].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[14].m_raceNumber,
            'nationality': packet.m_participants[14].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[14].m_name
        },
        {
            'aiControlled': packet.m_participants[15].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[15].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[15].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[15].m_raceNumber,
            'nationality': packet.m_participants[15].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[15].m_name
        },
        {
            'aiControlled': packet.m_participants[16].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[16].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[16].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[16].m_raceNumber,
            'nationality': packet.m_participants[16].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[16].m_name
        },
        {
            'aiControlled': packet.m_participants[17].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[17].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[17].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[17].m_raceNumber,
            'nationality': packet.m_participants[17].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[17].m_name
        },
        {
            'aiControlled': packet.m_participants[18].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[18].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[18].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[18].m_raceNumber,
            'nationality': packet.m_participants[18].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[18].m_name
        },
        {
            'aiControlled': packet.m_participants[19].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
            'driverId': packet.m_participants[19].m_driverId, # Driver id - see appendix
            'teamId': packet.m_participants[19].m_teamId, # Team id - see appendix
            'raceNumber': packet.m_participants[19].m_raceNumber,
            'nationality': packet.m_participants[19].m_nationality, # Nationality of the driver - see appendix
            'name': packet.m_participants[19].m_name
        }
    ]
    }

    return participant_data_json



def CarSetupData(packet):
    setup_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'carSetups': [
        {
            'frontWing': packet.m_carSetups[0].m_frontWing,
            'rearWing': packet.m_carSetups[0].m_rearWing,
            'onThrottle': packet.m_carSetups[0].m_onThrottle,
            'offThrottle': packet.m_carSetups[0].m_offThrottle,
            'frontCamber': packet.m_carSetups[0].m_frontCamber,
            'rearCamber': packet.m_carSetups[0].m_rearCamber,
            'frontToe': packet.m_carSetups[0].m_frontToe,
            'rearToe': packet.m_carSetups[0].m_rearToe,
            'frontSuspension': packet.m_carSetups[0].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[0].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[0].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[0].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[0].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[0].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[0].m_brakePressure,
            'brakeBias': packet.m_carSetups[0].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[0].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[0].m_rearTyrePressure,
            'ballast': packet.m_carSetups[0].m_ballast,
            'fuelLoad': packet.m_carSetups[0].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[1].m_frontWing,
            'rearWing': packet.m_carSetups[1].m_rearWing,
            'onThrottle': packet.m_carSetups[1].m_onThrottle,
            'offThrottle': packet.m_carSetups[1].m_offThrottle,
            'frontCamber': packet.m_carSetups[1].m_frontCamber,
            'rearCamber': packet.m_carSetups[1].m_rearCamber,
            'frontToe': packet.m_carSetups[1].m_frontToe,
            'rearToe': packet.m_carSetups[1].m_rearToe,
            'frontSuspension': packet.m_carSetups[1].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[1].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[1].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[1].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[1].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[1].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[1].m_brakePressure,
            'brakeBias': packet.m_carSetups[1].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[1].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[1].m_rearTyrePressure,
            'ballast': packet.m_carSetups[1].m_ballast,
            'fuelLoad': packet.m_carSetups[1].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[2].m_frontWing,
            'rearWing': packet.m_carSetups[2].m_rearWing,
            'onThrottle': packet.m_carSetups[2].m_onThrottle,
            'offThrottle': packet.m_carSetups[2].m_offThrottle,
            'frontCamber': packet.m_carSetups[2].m_frontCamber,
            'rearCamber': packet.m_carSetups[2].m_rearCamber,
            'frontToe': packet.m_carSetups[2].m_frontToe,
            'rearToe': packet.m_carSetups[2].m_rearToe,
            'frontSuspension': packet.m_carSetups[2].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[2].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[2].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[2].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[2].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[2].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[2].m_brakePressure,
            'brakeBias': packet.m_carSetups[2].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[2].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[2].m_rearTyrePressure,
            'ballast': packet.m_carSetups[2].m_ballast,
            'fuelLoad': packet.m_carSetups[2].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[3].m_frontWing,
            'rearWing': packet.m_carSetups[3].m_rearWing,
            'onThrottle': packet.m_carSetups[3].m_onThrottle,
            'offThrottle': packet.m_carSetups[3].m_offThrottle,
            'frontCamber': packet.m_carSetups[3].m_frontCamber,
            'rearCamber': packet.m_carSetups[3].m_rearCamber,
            'frontToe': packet.m_carSetups[3].m_frontToe,
            'rearToe': packet.m_carSetups[3].m_rearToe,
            'frontSuspension': packet.m_carSetups[3].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[3].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[3].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[3].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[3].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[3].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[3].m_brakePressure,
            'brakeBias': packet.m_carSetups[3].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[3].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[3].m_rearTyrePressure,
            'ballast': packet.m_carSetups[3].m_ballast,
            'fuelLoad': packet.m_carSetups[3].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[4].m_frontWing,
            'rearWing': packet.m_carSetups[4].m_rearWing,
            'onThrottle': packet.m_carSetups[4].m_onThrottle,
            'offThrottle': packet.m_carSetups[4].m_offThrottle,
            'frontCamber': packet.m_carSetups[4].m_frontCamber,
            'rearCamber': packet.m_carSetups[4].m_rearCamber,
            'frontToe': packet.m_carSetups[4].m_frontToe,
            'rearToe': packet.m_carSetups[4].m_rearToe,
            'frontSuspension': packet.m_carSetups[4].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[4].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[4].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[4].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[4].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[4].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[4].m_brakePressure,
            'brakeBias': packet.m_carSetups[4].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[4].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[4].m_rearTyrePressure,
            'ballast': packet.m_carSetups[4].m_ballast,
            'fuelLoad': packet.m_carSetups[4].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[5].m_frontWing,
            'rearWing': packet.m_carSetups[5].m_rearWing,
            'onThrottle': packet.m_carSetups[5].m_onThrottle,
            'offThrottle': packet.m_carSetups[5].m_offThrottle,
            'frontCamber': packet.m_carSetups[5].m_frontCamber,
            'rearCamber': packet.m_carSetups[5].m_rearCamber,
            'frontToe': packet.m_carSetups[5].m_frontToe,
            'rearToe': packet.m_carSetups[5].m_rearToe,
            'frontSuspension': packet.m_carSetups[5].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[5].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[5].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[5].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[5].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[5].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[5].m_brakePressure,
            'brakeBias': packet.m_carSetups[5].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[5].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[5].m_rearTyrePressure,
            'ballast': packet.m_carSetups[5].m_ballast,
            'fuelLoad': packet.m_carSetups[5].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[6].m_frontWing,
            'rearWing': packet.m_carSetups[6].m_rearWing,
            'onThrottle': packet.m_carSetups[6].m_onThrottle,
            'offThrottle': packet.m_carSetups[6].m_offThrottle,
            'frontCamber': packet.m_carSetups[6].m_frontCamber,
            'rearCamber': packet.m_carSetups[6].m_rearCamber,
            'frontToe': packet.m_carSetups[6].m_frontToe,
            'rearToe': packet.m_carSetups[6].m_rearToe,
            'frontSuspension': packet.m_carSetups[6].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[6].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[6].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[6].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[6].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[6].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[6].m_brakePressure,
            'brakeBias': packet.m_carSetups[6].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[6].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[6].m_rearTyrePressure,
            'ballast': packet.m_carSetups[6].m_ballast,
            'fuelLoad': packet.m_carSetups[6].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[7].m_frontWing,
            'rearWing': packet.m_carSetups[7].m_rearWing,
            'onThrottle': packet.m_carSetups[7].m_onThrottle,
            'offThrottle': packet.m_carSetups[7].m_offThrottle,
            'frontCamber': packet.m_carSetups[7].m_frontCamber,
            'rearCamber': packet.m_carSetups[7].m_rearCamber,
            'frontToe': packet.m_carSetups[7].m_frontToe,
            'rearToe': packet.m_carSetups[7].m_rearToe,
            'frontSuspension': packet.m_carSetups[7].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[7].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[7].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[7].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[7].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[7].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[7].m_brakePressure,
            'brakeBias': packet.m_carSetups[7].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[7].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[7].m_rearTyrePressure,
            'ballast': packet.m_carSetups[7].m_ballast,
            'fuelLoad': packet.m_carSetups[7].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[8].m_frontWing,
            'rearWing': packet.m_carSetups[8].m_rearWing,
            'onThrottle': packet.m_carSetups[8].m_onThrottle,
            'offThrottle': packet.m_carSetups[8].m_offThrottle,
            'frontCamber': packet.m_carSetups[8].m_frontCamber,
            'rearCamber': packet.m_carSetups[8].m_rearCamber,
            'frontToe': packet.m_carSetups[8].m_frontToe,
            'rearToe': packet.m_carSetups[8].m_rearToe,
            'frontSuspension': packet.m_carSetups[8].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[8].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[8].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[8].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[8].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[8].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[8].m_brakePressure,
            'brakeBias': packet.m_carSetups[8].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[8].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[8].m_rearTyrePressure,
            'ballast': packet.m_carSetups[8].m_ballast,
            'fuelLoad': packet.m_carSetups[8].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[9].m_frontWing,
            'rearWing': packet.m_carSetups[9].m_rearWing,
            'onThrottle': packet.m_carSetups[9].m_onThrottle,
            'offThrottle': packet.m_carSetups[9].m_offThrottle,
            'frontCamber': packet.m_carSetups[9].m_frontCamber,
            'rearCamber': packet.m_carSetups[9].m_rearCamber,
            'frontToe': packet.m_carSetups[9].m_frontToe,
            'rearToe': packet.m_carSetups[9].m_rearToe,
            'frontSuspension': packet.m_carSetups[9].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[9].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[9].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[9].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[9].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[9].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[9].m_brakePressure,
            'brakeBias': packet.m_carSetups[9].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[9].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[9].m_rearTyrePressure,
            'ballast': packet.m_carSetups[9].m_ballast,
            'fuelLoad': packet.m_carSetups[9].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[10].m_frontWing,
            'rearWing': packet.m_carSetups[10].m_rearWing,
            'onThrottle': packet.m_carSetups[10].m_onThrottle,
            'offThrottle': packet.m_carSetups[10].m_offThrottle,
            'frontCamber': packet.m_carSetups[10].m_frontCamber,
            'rearCamber': packet.m_carSetups[10].m_rearCamber,
            'frontToe': packet.m_carSetups[10].m_frontToe,
            'rearToe': packet.m_carSetups[10].m_rearToe,
            'frontSuspension': packet.m_carSetups[10].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[10].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[10].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[10].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[10].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[10].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[10].m_brakePressure,
            'brakeBias': packet.m_carSetups[10].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[10].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[10].m_rearTyrePressure,
            'ballast': packet.m_carSetups[10].m_ballast,
            'fuelLoad': packet.m_carSetups[10].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[11].m_frontWing,
            'rearWing': packet.m_carSetups[11].m_rearWing,
            'onThrottle': packet.m_carSetups[11].m_onThrottle,
            'offThrottle': packet.m_carSetups[11].m_offThrottle,
            'frontCamber': packet.m_carSetups[11].m_frontCamber,
            'rearCamber': packet.m_carSetups[11].m_rearCamber,
            'frontToe': packet.m_carSetups[11].m_frontToe,
            'rearToe': packet.m_carSetups[11].m_rearToe,
            'frontSuspension': packet.m_carSetups[11].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[11].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[11].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[11].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[11].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[11].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[11].m_brakePressure,
            'brakeBias': packet.m_carSetups[11].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[11].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[11].m_rearTyrePressure,
            'ballast': packet.m_carSetups[11].m_ballast,
            'fuelLoad': packet.m_carSetups[11].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[12].m_frontWing,
            'rearWing': packet.m_carSetups[12].m_rearWing,
            'onThrottle': packet.m_carSetups[12].m_onThrottle,
            'offThrottle': packet.m_carSetups[12].m_offThrottle,
            'frontCamber': packet.m_carSetups[12].m_frontCamber,
            'rearCamber': packet.m_carSetups[12].m_rearCamber,
            'frontToe': packet.m_carSetups[12].m_frontToe,
            'rearToe': packet.m_carSetups[12].m_rearToe,
            'frontSuspension': packet.m_carSetups[12].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[12].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[12].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[12].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[12].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[12].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[12].m_brakePressure,
            'brakeBias': packet.m_carSetups[12].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[12].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[12].m_rearTyrePressure,
            'ballast': packet.m_carSetups[12].m_ballast,
            'fuelLoad': packet.m_carSetups[12].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[13].m_frontWing,
            'rearWing': packet.m_carSetups[13].m_rearWing,
            'onThrottle': packet.m_carSetups[13].m_onThrottle,
            'offThrottle': packet.m_carSetups[13].m_offThrottle,
            'frontCamber': packet.m_carSetups[13].m_frontCamber,
            'rearCamber': packet.m_carSetups[13].m_rearCamber,
            'frontToe': packet.m_carSetups[13].m_frontToe,
            'rearToe': packet.m_carSetups[13].m_rearToe,
            'frontSuspension': packet.m_carSetups[13].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[13].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[13].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[13].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[13].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[13].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[13].m_brakePressure,
            'brakeBias': packet.m_carSetups[13].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[13].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[13].m_rearTyrePressure,
            'ballast': packet.m_carSetups[13].m_ballast,
            'fuelLoad': packet.m_carSetups[13].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[14].m_frontWing,
            'rearWing': packet.m_carSetups[14].m_rearWing,
            'onThrottle': packet.m_carSetups[14].m_onThrottle,
            'offThrottle': packet.m_carSetups[14].m_offThrottle,
            'frontCamber': packet.m_carSetups[14].m_frontCamber,
            'rearCamber': packet.m_carSetups[14].m_rearCamber,
            'frontToe': packet.m_carSetups[14].m_frontToe,
            'rearToe': packet.m_carSetups[14].m_rearToe,
            'frontSuspension': packet.m_carSetups[14].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[14].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[14].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[14].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[14].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[14].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[14].m_brakePressure,
            'brakeBias': packet.m_carSetups[14].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[14].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[14].m_rearTyrePressure,
            'ballast': packet.m_carSetups[14].m_ballast,
            'fuelLoad': packet.m_carSetups[14].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[15].m_frontWing,
            'rearWing': packet.m_carSetups[15].m_rearWing,
            'onThrottle': packet.m_carSetups[15].m_onThrottle,
            'offThrottle': packet.m_carSetups[15].m_offThrottle,
            'frontCamber': packet.m_carSetups[15].m_frontCamber,
            'rearCamber': packet.m_carSetups[15].m_rearCamber,
            'frontToe': packet.m_carSetups[15].m_frontToe,
            'rearToe': packet.m_carSetups[15].m_rearToe,
            'frontSuspension': packet.m_carSetups[15].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[15].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[15].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[15].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[15].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[15].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[15].m_brakePressure,
            'brakeBias': packet.m_carSetups[15].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[15].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[15].m_rearTyrePressure,
            'ballast': packet.m_carSetups[15].m_ballast,
            'fuelLoad': packet.m_carSetups[15].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[16].m_frontWing,
            'rearWing': packet.m_carSetups[16].m_rearWing,
            'onThrottle': packet.m_carSetups[16].m_onThrottle,
            'offThrottle': packet.m_carSetups[16].m_offThrottle,
            'frontCamber': packet.m_carSetups[16].m_frontCamber,
            'rearCamber': packet.m_carSetups[16].m_rearCamber,
            'frontToe': packet.m_carSetups[16].m_frontToe,
            'rearToe': packet.m_carSetups[16].m_rearToe,
            'frontSuspension': packet.m_carSetups[16].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[16].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[16].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[16].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[16].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[16].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[16].m_brakePressure,
            'brakeBias': packet.m_carSetups[16].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[16].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[16].m_rearTyrePressure,
            'ballast': packet.m_carSetups[16].m_ballast,
            'fuelLoad': packet.m_carSetups[16].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[17].m_frontWing,
            'rearWing': packet.m_carSetups[17].m_rearWing,
            'onThrottle': packet.m_carSetups[17].m_onThrottle,
            'offThrottle': packet.m_carSetups[17].m_offThrottle,
            'frontCamber': packet.m_carSetups[17].m_frontCamber,
            'rearCamber': packet.m_carSetups[17].m_rearCamber,
            'frontToe': packet.m_carSetups[17].m_frontToe,
            'rearToe': packet.m_carSetups[17].m_rearToe,
            'frontSuspension': packet.m_carSetups[17].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[17].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[17].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[17].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[17].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[17].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[17].m_brakePressure,
            'brakeBias': packet.m_carSetups[17].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[17].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[17].m_rearTyrePressure,
            'ballast': packet.m_carSetups[17].m_ballast,
            'fuelLoad': packet.m_carSetups[17].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[18].m_frontWing,
            'rearWing': packet.m_carSetups[18].m_rearWing,
            'onThrottle': packet.m_carSetups[18].m_onThrottle,
            'offThrottle': packet.m_carSetups[18].m_offThrottle,
            'frontCamber': packet.m_carSetups[18].m_frontCamber,
            'rearCamber': packet.m_carSetups[18].m_rearCamber,
            'frontToe': packet.m_carSetups[18].m_frontToe,
            'rearToe': packet.m_carSetups[18].m_rearToe,
            'frontSuspension': packet.m_carSetups[18].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[18].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[18].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[18].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[18].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[18].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[18].m_brakePressure,
            'brakeBias': packet.m_carSetups[18].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[18].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[18].m_rearTyrePressure,
            'ballast': packet.m_carSetups[18].m_ballast,
            'fuelLoad': packet.m_carSetups[18].m_fuelLoad
        },
        {
            'frontWing': packet.m_carSetups[19].m_frontWing,
            'rearWing': packet.m_carSetups[19].m_rearWing,
            'onThrottle': packet.m_carSetups[19].m_onThrottle,
            'offThrottle': packet.m_carSetups[19].m_offThrottle,
            'frontCamber': packet.m_carSetups[19].m_frontCamber,
            'rearCamber': packet.m_carSetups[19].m_rearCamber,
            'frontToe': packet.m_carSetups[19].m_frontToe,
            'rearToe': packet.m_carSetups[19].m_rearToe,
            'frontSuspension': packet.m_carSetups[19].m_frontSuspension,
            'rearSuspension': packet.m_carSetups[19].m_rearSuspension,
            'frontAntiRollBar': packet.m_carSetups[19].m_frontAntiRollBar,
            'rearAntiRollBar': packet.m_carSetups[19].m_rearAntiRollBar,
            'frontSuspensionHeight': packet.m_carSetups[19].m_frontSuspensionHeight,
            'rearSuspensionHeight': packet.m_carSetups[19].m_rearSuspensionHeight,
            'brakePressure': packet.m_carSetups[19].m_brakePressure,
            'brakeBias': packet.m_carSetups[19].m_brakeBias,
            'frontTyrePressure': packet.m_carSetups[19].m_frontTyrePressure,
            'rearTyrePressure': packet.m_carSetups[19].m_rearTyrePressure,
            'ballast': packet.m_carSetups[19].m_ballast,
            'fuelLoad': packet.m_carSetups[19].m_fuelLoad
        }
    ]
    }

    return setup_data_json



def CarTelemetryData(packet):
    drs_types = ['off', 'on']
    button_status_types = {'0x0001': 'Cross or A', '0x0002': 'Triangle or Y', '0x0004': 'Circle or B', '0x0008': 'Square or X', '0x0010': 'D-pad Left', '0x0020': 'D-pad Right',
                            '0x0040': 'D-pad Up', '0x0080': 'D-pad Down', '0x0100': 'Options or Menu', '0x0200': 'L1 or LB', '0x0400': 'R2 or RB', '0x0800': 'L2 or LT',
                            '0x1000': 'R2 or RT', '0x2000': 'Left Stick Click', '0x4000': 'Right Stick Click'}

    telemetry_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'carTelemetryData':[
        {
            'speed': packet.m_carTelemetryData[0].m_speed,
            'throttle': packet.m_carTelemetryData[0].m_throttle,
            'steer': packet.m_carTelemetryData[0].m_steer,
            'brake': packet.m_carTelemetryData[0].m_brake,
            'clutch': packet.m_carTelemetryData[0].m_clutch,
            'gear': packet.m_carTelemetryData[0].m_gear,
            'engineRPM': packet.m_carTelemetryData[0].m_engineRPM,
            'drs': packet.m_carTelemetryData[0].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[0].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[0].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[0].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[0].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[0].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[0].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[0].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[0].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[0].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[0].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[0].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[0].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[0].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[0].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[1].m_speed,
            'throttle': packet.m_carTelemetryData[1].m_throttle,
            'steer': packet.m_carTelemetryData[1].m_steer,
            'brake': packet.m_carTelemetryData[1].m_brake,
            'clutch': packet.m_carTelemetryData[1].m_clutch,
            'gear': packet.m_carTelemetryData[1].m_gear,
            'engineRPM': packet.m_carTelemetryData[1].m_engineRPM,
            'drs': packet.m_carTelemetryData[1].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[1].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[1].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[1].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[1].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[1].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[1].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[1].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[1].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[1].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[1].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[1].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[1].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[1].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[1].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[1].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[1].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[1].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[1].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[2].m_speed,
            'throttle': packet.m_carTelemetryData[2].m_throttle,
            'steer': packet.m_carTelemetryData[2].m_steer,
            'brake': packet.m_carTelemetryData[2].m_brake,
            'clutch': packet.m_carTelemetryData[2].m_clutch,
            'gear': packet.m_carTelemetryData[2].m_gear,
            'engineRPM': packet.m_carTelemetryData[2].m_engineRPM,
            'drs': packet.m_carTelemetryData[2].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[2].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[2].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[2].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[2].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[2].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[2].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[2].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[2].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[2].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[2].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[2].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[2].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[2].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[2].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[2].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[2].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[2].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[2].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[3].m_speed,
            'throttle': packet.m_carTelemetryData[3].m_throttle,
            'steer': packet.m_carTelemetryData[3].m_steer,
            'brake': packet.m_carTelemetryData[3].m_brake,
            'clutch': packet.m_carTelemetryData[3].m_clutch,
            'gear': packet.m_carTelemetryData[3].m_gear,
            'engineRPM': packet.m_carTelemetryData[3].m_engineRPM,
            'drs': packet.m_carTelemetryData[3].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[3].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[3].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[3].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[3].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[3].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[3].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[3].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[3].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[3].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[3].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[3].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[3].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[3].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[3].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[3].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[3].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[3].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[3].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[4].m_speed,
            'throttle': packet.m_carTelemetryData[4].m_throttle,
            'steer': packet.m_carTelemetryData[4].m_steer,
            'brake': packet.m_carTelemetryData[4].m_brake,
            'clutch': packet.m_carTelemetryData[4].m_clutch,
            'gear': packet.m_carTelemetryData[4].m_gear,
            'engineRPM': packet.m_carTelemetryData[4].m_engineRPM,
            'drs': packet.m_carTelemetryData[4].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[4].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[4].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[4].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[4].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[4].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[4].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[4].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[4].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[4].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[4].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[4].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[4].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[4].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[4].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[4].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[4].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[4].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[4].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[5].m_speed,
            'throttle': packet.m_carTelemetryData[5].m_throttle,
            'steer': packet.m_carTelemetryData[5].m_steer,
            'brake': packet.m_carTelemetryData[5].m_brake,
            'clutch': packet.m_carTelemetryData[5].m_clutch,
            'gear': packet.m_carTelemetryData[5].m_gear,
            'engineRPM': packet.m_carTelemetryData[5].m_engineRPM,
            'drs': packet.m_carTelemetryData[5].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[5].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[5].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[5].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[5].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[5].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[5].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[5].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[5].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[5].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[5].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[5].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[5].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[5].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[5].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[5].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[5].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[5].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[5].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[6].m_speed,
            'throttle': packet.m_carTelemetryData[6].m_throttle,
            'steer': packet.m_carTelemetryData[6].m_steer,
            'brake': packet.m_carTelemetryData[6].m_brake,
            'clutch': packet.m_carTelemetryData[6].m_clutch,
            'gear': packet.m_carTelemetryData[6].m_gear,
            'engineRPM': packet.m_carTelemetryData[6].m_engineRPM,
            'drs': packet.m_carTelemetryData[6].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[6].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[6].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[6].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[6].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[6].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[6].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[6].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[6].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[6].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[6].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[6].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[6].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[6].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[6].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[6].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[6].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[6].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[6].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[7 ].m_speed,
            'throttle': packet.m_carTelemetryData[7].m_throttle,
            'steer': packet.m_carTelemetryData[7].m_steer,
            'brake': packet.m_carTelemetryData[7].m_brake,
            'clutch': packet.m_carTelemetryData[7].m_clutch,
            'gear': packet.m_carTelemetryData[7].m_gear,
            'engineRPM': packet.m_carTelemetryData[7].m_engineRPM,
            'drs': packet.m_carTelemetryData[7].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[7].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[7].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[7].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[7].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[7].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[7].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[7].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[7].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[7].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[7].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[7].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[7].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[7].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[7].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[7].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[7].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[7].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[7].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[8].m_speed,
            'throttle': packet.m_carTelemetryData[8].m_throttle,
            'steer': packet.m_carTelemetryData[8].m_steer,
            'brake': packet.m_carTelemetryData[8].m_brake,
            'clutch': packet.m_carTelemetryData[8].m_clutch,
            'gear': packet.m_carTelemetryData[8].m_gear,
            'engineRPM': packet.m_carTelemetryData[8].m_engineRPM,
            'drs': packet.m_carTelemetryData[8].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[8].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[8].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[8].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[8].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[8].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[8].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[8].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[8].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[8].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[8].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[8].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[8].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[8].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[8].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[8].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[8].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[8].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[8].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[9].m_speed,
            'throttle': packet.m_carTelemetryData[9].m_throttle,
            'steer': packet.m_carTelemetryData[9].m_steer,
            'brake': packet.m_carTelemetryData[9].m_brake,
            'clutch': packet.m_carTelemetryData[9].m_clutch,
            'gear': packet.m_carTelemetryData[9].m_gear,
            'engineRPM': packet.m_carTelemetryData[9].m_engineRPM,
            'drs': packet.m_carTelemetryData[9].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[9].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[9].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[9].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[9].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[9].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[9].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[9].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[9].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[9].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[9].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[9].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[9].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[9].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[9].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[9].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[9].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[9].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[9].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[10].m_speed,
            'throttle': packet.m_carTelemetryData[10].m_throttle,
            'steer': packet.m_carTelemetryData[10].m_steer,
            'brake': packet.m_carTelemetryData[10].m_brake,
            'clutch': packet.m_carTelemetryData[10].m_clutch,
            'gear': packet.m_carTelemetryData[10].m_gear,
            'engineRPM': packet.m_carTelemetryData[10].m_engineRPM,
            'drs': packet.m_carTelemetryData[10].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[10].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[10].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[10].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[10].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[10].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[10].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[10].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[10].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[10].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[10].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[10].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[10].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[10].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[10].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[10].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[10].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[10].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[10].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[11].m_speed,
            'throttle': packet.m_carTelemetryData[11].m_throttle,
            'steer': packet.m_carTelemetryData[11].m_steer,
            'brake': packet.m_carTelemetryData[11].m_brake,
            'clutch': packet.m_carTelemetryData[11].m_clutch,
            'gear': packet.m_carTelemetryData[11].m_gear,
            'engineRPM': packet.m_carTelemetryData[11].m_engineRPM,
            'drs': packet.m_carTelemetryData[11].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[11].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[11].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[11].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[11].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[11].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[11].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[11].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[11].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[11].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[11].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[11].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[11].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[11].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[11].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[11].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[11].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[11].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[11].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[12].m_speed,
            'throttle': packet.m_carTelemetryData[12].m_throttle,
            'steer': packet.m_carTelemetryData[12].m_steer,
            'brake': packet.m_carTelemetryData[12].m_brake,
            'clutch': packet.m_carTelemetryData[12].m_clutch,
            'gear': packet.m_carTelemetryData[12].m_gear,
            'engineRPM': packet.m_carTelemetryData[12].m_engineRPM,
            'drs': packet.m_carTelemetryData[12].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[12].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[12].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[12].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[12].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[12].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[12].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[12].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[12].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[12].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[12].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[12].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[12].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[12].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[12].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[12].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[12].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[12].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[12].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[13].m_speed,
            'throttle': packet.m_carTelemetryData[13].m_throttle,
            'steer': packet.m_carTelemetryData[13].m_steer,
            'brake': packet.m_carTelemetryData[13].m_brake,
            'clutch': packet.m_carTelemetryData[13].m_clutch,
            'gear': packet.m_carTelemetryData[13].m_gear,
            'engineRPM': packet.m_carTelemetryData[13].m_engineRPM,
            'drs': packet.m_carTelemetryData[13].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[13].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[13].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[13].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[13].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[13].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[13].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[13].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[13].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[13].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[13].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[13].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[13].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[13].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[13].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[13].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[13].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[13].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[13].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[14].m_speed,
            'throttle': packet.m_carTelemetryData[14].m_throttle,
            'steer': packet.m_carTelemetryData[14].m_steer,
            'brake': packet.m_carTelemetryData[14].m_brake,
            'clutch': packet.m_carTelemetryData[14].m_clutch,
            'gear': packet.m_carTelemetryData[14].m_gear,
            'engineRPM': packet.m_carTelemetryData[14].m_engineRPM,
            'drs': packet.m_carTelemetryData[14].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[14].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[14].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[14].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[14].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[14].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[14].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[14].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[14].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[14].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[14].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[14].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[14].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[14].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[14].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[14].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[14].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[14].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[14].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[15].m_speed,
            'throttle': packet.m_carTelemetryData[15].m_throttle,
            'steer': packet.m_carTelemetryData[15].m_steer,
            'brake': packet.m_carTelemetryData[15].m_brake,
            'clutch': packet.m_carTelemetryData[15].m_clutch,
            'gear': packet.m_carTelemetryData[15].m_gear,
            'engineRPM': packet.m_carTelemetryData[15].m_engineRPM,
            'drs': packet.m_carTelemetryData[15].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[15].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[15].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[15].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[15].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[15].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[15].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[15].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[15].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[15].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[15].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[15].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[15].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[15].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[15].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[15].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[15].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[15].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[15].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[16].m_speed,
            'throttle': packet.m_carTelemetryData[16].m_throttle,
            'steer': packet.m_carTelemetryData[16].m_steer,
            'brake': packet.m_carTelemetryData[16].m_brake,
            'clutch': packet.m_carTelemetryData[16].m_clutch,
            'gear': packet.m_carTelemetryData[16].m_gear,
            'engineRPM': packet.m_carTelemetryData[16].m_engineRPM,
            'drs': packet.m_carTelemetryData[16].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[16].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[16].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[16].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[16].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[16].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[16].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[16].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[16].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[16].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[16].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[16].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[16].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[16].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[16].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[16].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[16].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[16].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[16].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[17].m_speed,
            'throttle': packet.m_carTelemetryData[17].m_throttle,
            'steer': packet.m_carTelemetryData[17].m_steer,
            'brake': packet.m_carTelemetryData[17].m_brake,
            'clutch': packet.m_carTelemetryData[17].m_clutch,
            'gear': packet.m_carTelemetryData[17].m_gear,
            'engineRPM': packet.m_carTelemetryData[17].m_engineRPM,
            'drs': packet.m_carTelemetryData[17].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[17].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[17].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[17].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[17].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[17].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[17].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[17].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[17].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[17].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[17].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[17].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[17].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[17].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[17].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[17].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[17].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[17].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[17].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[18].m_speed,
            'throttle': packet.m_carTelemetryData[18].m_throttle,
            'steer': packet.m_carTelemetryData[18].m_steer,
            'brake': packet.m_carTelemetryData[18].m_brake,
            'clutch': packet.m_carTelemetryData[18].m_clutch,
            'gear': packet.m_carTelemetryData[18].m_gear,
            'engineRPM': packet.m_carTelemetryData[18].m_engineRPM,
            'drs': packet.m_carTelemetryData[18].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[18].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[18].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[18].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[18].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[18].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[18].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[18].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[18].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[18].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[18].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[18].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[18].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[18].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[18].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[18].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[18].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[18].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[18].m_tyresPressure[3]
            }
        },
        {
            'speed': packet.m_carTelemetryData[19].m_speed,
            'throttle': packet.m_carTelemetryData[19].m_throttle,
            'steer': packet.m_carTelemetryData[19].m_steer,
            'brake': packet.m_carTelemetryData[19].m_brake,
            'clutch': packet.m_carTelemetryData[19].m_clutch,
            'gear': packet.m_carTelemetryData[19].m_gear,
            'engineRPM': packet.m_carTelemetryData[19].m_engineRPM,
            'drs': packet.m_carTelemetryData[19].m_drs,
            'revLightsPercent': packet.m_carTelemetryData[19].m_revLightsPercent,
            'brakesTemperature':{
                'RL': packet.m_carTelemetryData[19].m_brakesTemperature[0],
                'RR': packet.m_carTelemetryData[19].m_brakesTemperature[1],
                'FL': packet.m_carTelemetryData[19].m_brakesTemperature[2],
                'FR': packet.m_carTelemetryData[19].m_brakesTemperature[3]
            },
            'tyresSurfaceTemperature':{
                'RL': packet.m_carTelemetryData[19].m_tyresSurfaceTemperature[0],
                'RR': packet.m_carTelemetryData[19].m_tyresSurfaceTemperature[1],
                'FL': packet.m_carTelemetryData[19].m_tyresSurfaceTemperature[2],
                'FR': packet.m_carTelemetryData[19].m_tyresSurfaceTemperature[3]
            },
            'tyresInnerTemperature':{
                'RL': packet.m_carTelemetryData[19].m_tyresInnerTemperature[0],
                'RR': packet.m_carTelemetryData[19].m_tyresInnerTemperature[1],
                'FL': packet.m_carTelemetryData[19].m_tyresInnerTemperature[2],
                'FR': packet.m_carTelemetryData[19].m_tyresInnerTemperature[3]
            },
            'engineTemperature': packet.m_carTelemetryData[19].m_engineTemperature,
            'tyresPressure':{
                'RL': packet.m_carTelemetryData[19].m_tyresPressure[0],
                'RR': packet.m_carTelemetryData[19].m_tyresPressure[1],
                'FL': packet.m_carTelemetryData[19].m_tyresPressure[2],
                'FR': packet.m_carTelemetryData[19].m_tyresPressure[3]
            }
        }
    ],
    'buttonStatus': 'not implemented'
    # 'buttonStatus': button_status_types[packet.m_buttonStatus]
    }

    return telemetry_data_json



def PacketCarStatusData(packet):
    traction_control_types = ['off', '', 'high']
    anti_lock_brakes_type = ['off', 'on']
    fuel_mix_types = ['lean', 'standard', 'rich', 'max']
    pit_limiter_types = ['off', 'on']
    drs_allowed_types = ['not allowed', 'allowed']
    tyre_compound_types = ['hyper soft', 'ultra soft', 'super soft', 'soft', 'medium', 'hard', 'super hard', 'inter', 'wet']
    vehicle_fia_flags_types = ['none', 'green', 'blue', 'yellow', 'red']
    ers_deploy_mode_types = ['none', 'low', 'medium', 'high', 'overtake', 'hotlap']

    status_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': packet.m_header.m_playerCarIndex
    },
    'carStatusData':[
        {
            'tractionControl': packet.m_carStatusData[0].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[0].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[0].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[0].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[0].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[0].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[0].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[0].m_maxRPM,
            'idleRPM': packet.m_carStatusData[0].m_idleRPM,
            'maxGears': packet.m_carStatusData[0].m_maxGears,
            'drsAllowed': packet.m_carStatusData[0].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[0].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[0].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[0].m_tyresDamage[0],
                'RR': packet.m_carStatusData[0].m_tyresDamage[1],
                'FL': packet.m_carStatusData[0].m_tyresDamage[2],
                'FR': packet.m_carStatusData[0].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[0].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[0].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[0].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[0].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[0].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[0].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[0].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[0].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[0].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[0].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[0].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[0].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[1].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[1].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[1].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[1].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[1].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[1].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[1].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[1].m_maxRPM,
            'idleRPM': packet.m_carStatusData[1].m_idleRPM,
            'maxGears': packet.m_carStatusData[1].m_maxGears,
            'drsAllowed': packet.m_carStatusData[1].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[1].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[1].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[1].m_tyresDamage[0],
                'RR': packet.m_carStatusData[1].m_tyresDamage[1],
                'FL': packet.m_carStatusData[1].m_tyresDamage[2],
                'FR': packet.m_carStatusData[1].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[1].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[1].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[1].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[1].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[1].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[1].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[1].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[1].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[1].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[1].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[1].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[1].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[2].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[2].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[2].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[2].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[2].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[2].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[2].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[2].m_maxRPM,
            'idleRPM': packet.m_carStatusData[2].m_idleRPM,
            'maxGears': packet.m_carStatusData[2].m_maxGears,
            'drsAllowed': packet.m_carStatusData[2].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[2].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[2].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[2].m_tyresDamage[0],
                'RR': packet.m_carStatusData[2].m_tyresDamage[1],
                'FL': packet.m_carStatusData[2].m_tyresDamage[2],
                'FR': packet.m_carStatusData[2].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[2].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[2].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[2].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[2].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[2].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[2].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[2].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[2].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[2].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[2].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[2].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[2].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[3].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[3].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[3].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[3].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[3].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[3].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[3].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[3].m_maxRPM,
            'idleRPM': packet.m_carStatusData[3].m_idleRPM,
            'maxGears': packet.m_carStatusData[3].m_maxGears,
            'drsAllowed': packet.m_carStatusData[3].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[3].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[3].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[3].m_tyresDamage[0],
                'RR': packet.m_carStatusData[3].m_tyresDamage[1],
                'FL': packet.m_carStatusData[3].m_tyresDamage[2],
                'FR': packet.m_carStatusData[3].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[3].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[3].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[3].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[3].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[3].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[3].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[3].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[3].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[3].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[3].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[3].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[3].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[4].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[4].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[4].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[4].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[4].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[4].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[4].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[4].m_maxRPM,
            'idleRPM': packet.m_carStatusData[4].m_idleRPM,
            'maxGears': packet.m_carStatusData[4].m_maxGears,
            'drsAllowed': packet.m_carStatusData[4].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[4].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[4].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[4].m_tyresDamage[0],
                'RR': packet.m_carStatusData[4].m_tyresDamage[1],
                'FL': packet.m_carStatusData[4].m_tyresDamage[2],
                'FR': packet.m_carStatusData[4].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[4].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[4].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[4].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[4].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[4].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[4].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[4].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[4].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[4].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[4].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[4].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[4].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[5].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[5].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[5].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[5].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[5].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[5].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[5].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[5].m_maxRPM,
            'idleRPM': packet.m_carStatusData[5].m_idleRPM,
            'maxGears': packet.m_carStatusData[5].m_maxGears,
            'drsAllowed': packet.m_carStatusData[5].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[5].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[5].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[5].m_tyresDamage[0],
                'RR': packet.m_carStatusData[5].m_tyresDamage[1],
                'FL': packet.m_carStatusData[5].m_tyresDamage[2],
                'FR': packet.m_carStatusData[5].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[5].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[5].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[5].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[5].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[5].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[5].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[5].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[5].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[5].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[5].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[5].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[5].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[6].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[6].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[6].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[6].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[6].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[6].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[6].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[6].m_maxRPM,
            'idleRPM': packet.m_carStatusData[6].m_idleRPM,
            'maxGears': packet.m_carStatusData[6].m_maxGears,
            'drsAllowed': packet.m_carStatusData[6].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[6].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[6].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[6].m_tyresDamage[0],
                'RR': packet.m_carStatusData[6].m_tyresDamage[1],
                'FL': packet.m_carStatusData[6].m_tyresDamage[2],
                'FR': packet.m_carStatusData[6].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[6].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[6].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[6].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[6].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[6].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[6].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[6].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[6].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[6].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[6].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[6].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[6].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[7].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[7].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[7].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[7].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[7].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[7].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[7].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[7].m_maxRPM,
            'idleRPM': packet.m_carStatusData[7].m_idleRPM,
            'maxGears': packet.m_carStatusData[7].m_maxGears,
            'drsAllowed': packet.m_carStatusData[7].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[7].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[7].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[7].m_tyresDamage[0],
                'RR': packet.m_carStatusData[7].m_tyresDamage[1],
                'FL': packet.m_carStatusData[7].m_tyresDamage[2],
                'FR': packet.m_carStatusData[7].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[7].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[7].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[7].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[7].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[7].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[7].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[7].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[7].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[7].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[7].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[7].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[7].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[8].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[8].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[8].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[8].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[8].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[8].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[8].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[8].m_maxRPM,
            'idleRPM': packet.m_carStatusData[8].m_idleRPM,
            'maxGears': packet.m_carStatusData[8].m_maxGears,
            'drsAllowed': packet.m_carStatusData[8].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[8].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[8].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[8].m_tyresDamage[0],
                'RR': packet.m_carStatusData[8].m_tyresDamage[1],
                'FL': packet.m_carStatusData[8].m_tyresDamage[2],
                'FR': packet.m_carStatusData[8].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[8].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[8].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[8].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[8].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[8].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[8].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[8].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[8].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[8].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[8].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[8].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[8].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[9].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[9].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[9].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[9].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[9].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[9].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[9].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[9].m_maxRPM,
            'idleRPM': packet.m_carStatusData[9].m_idleRPM,
            'maxGears': packet.m_carStatusData[9].m_maxGears,
            'drsAllowed': packet.m_carStatusData[9].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[9].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[9].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[9].m_tyresDamage[0],
                'RR': packet.m_carStatusData[9].m_tyresDamage[1],
                'FL': packet.m_carStatusData[9].m_tyresDamage[2],
                'FR': packet.m_carStatusData[9].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[9].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[9].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[9].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[9].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[9].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[9].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[9].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[9].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[9].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[9].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[9].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[9].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[10].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[10].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[10].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[10].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[10].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[10].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[10].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[10].m_maxRPM,
            'idleRPM': packet.m_carStatusData[10].m_idleRPM,
            'maxGears': packet.m_carStatusData[10].m_maxGears,
            'drsAllowed': packet.m_carStatusData[10].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[10].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[10].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[10].m_tyresDamage[0],
                'RR': packet.m_carStatusData[10].m_tyresDamage[1],
                'FL': packet.m_carStatusData[10].m_tyresDamage[2],
                'FR': packet.m_carStatusData[10].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[10].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[10].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[10].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[10].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[10].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[10].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[10].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[10].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[10].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[10].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[10].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[10].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[11].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[11].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[11].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[11].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[11].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[11].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[11].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[11].m_maxRPM,
            'idleRPM': packet.m_carStatusData[11].m_idleRPM,
            'maxGears': packet.m_carStatusData[11].m_maxGears,
            'drsAllowed': packet.m_carStatusData[11].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[11].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[11].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[11].m_tyresDamage[0],
                'RR': packet.m_carStatusData[11].m_tyresDamage[1],
                'FL': packet.m_carStatusData[11].m_tyresDamage[2],
                'FR': packet.m_carStatusData[11].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[11].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[11].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[11].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[11].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[11].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[11].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[11].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[11].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[11].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[11].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[11].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[11].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[12].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[12].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[12].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[12].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[12].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[12].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[12].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[12].m_maxRPM,
            'idleRPM': packet.m_carStatusData[12].m_idleRPM,
            'maxGears': packet.m_carStatusData[12].m_maxGears,
            'drsAllowed': packet.m_carStatusData[12].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[12].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[12].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[12].m_tyresDamage[0],
                'RR': packet.m_carStatusData[12].m_tyresDamage[1],
                'FL': packet.m_carStatusData[12].m_tyresDamage[2],
                'FR': packet.m_carStatusData[12].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[12].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[12].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[12].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[12].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[12].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[12].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[12].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[12].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[12].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[12].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[12].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[12].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[13].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[13].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[13].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[13].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[13].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[13].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[13].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[13].m_maxRPM,
            'idleRPM': packet.m_carStatusData[13].m_idleRPM,
            'maxGears': packet.m_carStatusData[13].m_maxGears,
            'drsAllowed': packet.m_carStatusData[13].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[13].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[13].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[13].m_tyresDamage[0],
                'RR': packet.m_carStatusData[13].m_tyresDamage[1],
                'FL': packet.m_carStatusData[13].m_tyresDamage[2],
                'FR': packet.m_carStatusData[13].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[13].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[13].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[13].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[13].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[13].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[13].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[13].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[13].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[13].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[13].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[13].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[13].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[14].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[14].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[14].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[14].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[14].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[14].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[14].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[14].m_maxRPM,
            'idleRPM': packet.m_carStatusData[14].m_idleRPM,
            'maxGears': packet.m_carStatusData[14].m_maxGears,
            'drsAllowed': packet.m_carStatusData[14].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[14].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[14].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[14].m_tyresDamage[0],
                'RR': packet.m_carStatusData[14].m_tyresDamage[1],
                'FL': packet.m_carStatusData[14].m_tyresDamage[2],
                'FR': packet.m_carStatusData[14].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[14].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[14].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[14].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[14].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[14].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[14].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[14].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[14].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[14].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[14].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[14].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[14].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[15].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[15].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[15].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[15].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[15].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[15].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[15].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[15].m_maxRPM,
            'idleRPM': packet.m_carStatusData[15].m_idleRPM,
            'maxGears': packet.m_carStatusData[15].m_maxGears,
            'drsAllowed': packet.m_carStatusData[15].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[15].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[15].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[15].m_tyresDamage[0],
                'RR': packet.m_carStatusData[15].m_tyresDamage[1],
                'FL': packet.m_carStatusData[15].m_tyresDamage[2],
                'FR': packet.m_carStatusData[15].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[15].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[15].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[15].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[15].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[15].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[15].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[15].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[15].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[15].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[15].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[15].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[15].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[16].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[16].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[16].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[16].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[16].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[16].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[16].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[16].m_maxRPM,
            'idleRPM': packet.m_carStatusData[16].m_idleRPM,
            'maxGears': packet.m_carStatusData[16].m_maxGears,
            'drsAllowed': packet.m_carStatusData[16].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[16].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[16].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[16].m_tyresDamage[0],
                'RR': packet.m_carStatusData[16].m_tyresDamage[1],
                'FL': packet.m_carStatusData[16].m_tyresDamage[2],
                'FR': packet.m_carStatusData[16].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[16].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[16].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[16].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[16].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[16].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[16].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[16].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[16].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[16].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[16].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[16].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[16].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[17].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[17].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[17].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[17].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[17].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[17].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[17].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[17].m_maxRPM,
            'idleRPM': packet.m_carStatusData[17].m_idleRPM,
            'maxGears': packet.m_carStatusData[17].m_maxGears,
            'drsAllowed': packet.m_carStatusData[17].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[17].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[17].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[17].m_tyresDamage[0],
                'RR': packet.m_carStatusData[17].m_tyresDamage[1],
                'FL': packet.m_carStatusData[17].m_tyresDamage[2],
                'FR': packet.m_carStatusData[17].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[17].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[17].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[17].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[17].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[17].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[17].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[17].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[17].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[17].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[17].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[17].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[17].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[18].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[18].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[18].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[18].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[18].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[18].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[18].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[18].m_maxRPM,
            'idleRPM': packet.m_carStatusData[18].m_idleRPM,
            'maxGears': packet.m_carStatusData[18].m_maxGears,
            'drsAllowed': packet.m_carStatusData[18].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[18].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[18].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[18].m_tyresDamage[0],
                'RR': packet.m_carStatusData[18].m_tyresDamage[1],
                'FL': packet.m_carStatusData[18].m_tyresDamage[2],
                'FR': packet.m_carStatusData[18].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[18].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[18].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[18].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[18].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[18].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[18].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[18].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[18].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[18].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[18].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[18].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[18].m_ersDeployedThisLap
        },
        {
            'tractionControl': packet.m_carStatusData[19].m_tractionControl, # 0 (off) - 2 (high)
            'antiLockBrakes': packet.m_carStatusData[19].m_antiLockBrakes, # 0 (off) - 1 (on)
            'fuelMix': packet.m_carStatusData[19].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
            'frontBrakeBias': packet.m_carStatusData[19].m_frontBrakeBias,
            'pitLimiterStatus': packet.m_carStatusData[19].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
            'fuelInTank': packet.m_carStatusData[19].m_fuelInTank,
            'fuelCapacity': packet.m_carStatusData[19].m_fuelCapacity,
            'maxRPM': packet.m_carStatusData[19].m_maxRPM,
            'idleRPM': packet.m_carStatusData[19].m_idleRPM,
            'maxGears': packet.m_carStatusData[19].m_maxGears,
            'drsAllowed': packet.m_carStatusData[19].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
            'tyresWear': packet.m_carStatusData[19].m_tyresWear,
            'tyreCompound': packet.m_carStatusData[19].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
            'tyresDamage':{
                'RL': packet.m_carStatusData[19].m_tyresDamage[0],
                'RR': packet.m_carStatusData[19].m_tyresDamage[1],
                'FL': packet.m_carStatusData[19].m_tyresDamage[2],
                'FR': packet.m_carStatusData[19].m_tyresDamage[3]
            },
            'frontLeftWingDamage': packet.m_carStatusData[19].m_frontLeftWingDamage,
            'frontRightWingDamage': packet.m_carStatusData[19].m_frontRightWingDamage,
            'rearWingDamage': packet.m_carStatusData[19].m_rearWingDamage,
            'engineDamage': packet.m_carStatusData[19].m_engineDamage,
            'gearBoxDamage': packet.m_carStatusData[19].m_gearBoxDamage,
            'exhaustDamage': packet.m_carStatusData[19].m_exhaustDamage,
            'vehicleFiaFlags': packet.m_carStatusData[19].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
            'ersStoreEnergy': packet.m_carStatusData[19].m_ersStoreEnergy,
            'ersDeployMode': packet.m_carStatusData[19].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
            'ersHarvestedThisLapMGUK': packet.m_carStatusData[19].m_ersHarvestedThisLapMGUK,
            'ersHarvestedThisLapMGUH': packet.m_carStatusData[19].m_ersHarvestedThisLapMGUH,
            'ersDeployedThisLap': packet.m_carStatusData[19].m_ersDeployedThisLap
        }
    ]
    }

    return status_data_json



def structs(packet_name, packet):

    if packet_name == 'MotionData':
        return MotionData(packet)
    elif packet_name == 'SessionData':
        return SessionData(packet)
    elif packet_name == 'LapData':
        return LapData(packet)
    elif packet_name == 'EventData':
        return EventData(packet)
    elif packet_name == 'ParticipantData':
        return ParticipantData(packet)
    elif packet_name == 'CarSetupData':
        return CarSetupData(packet)
    elif packet_name == 'CarTelemetryData':
        return CarTelemetryData(packet)
    elif packet_name == 'PacketCarStatusData':
        return PacketCarStatusData(packet)

    else:
        print "ERROR, PACKET IS NOT WHAT IS EXPECTED!"
        return None
