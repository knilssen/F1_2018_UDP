#
#
# Takes the structs required for the udp data and turns them into json objects to
# pass through our websocket to the webpage for viewing
#
# Author: Kristian Nilssen

import json


def MotionData(packet):
    players_car = packet.m_header.m_playerCarIndex
    motion_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'carMotionData': {
        'worldPositionX': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldPositionX),
        'worldPositionY': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldPositionY),
        'worldPositionZ': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldPositionZ),
        'worldVelocityX': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldVelocityX),
        'worldVelocityY': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldVelocityY),
        'worldVelocityZ': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldVelocityZ),
        'worldForwardDirX': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldForwardDirX),
        'worldForwardDirY': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldForwardDirY),
        'worldForwardDirZ': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldForwardDirZ),
        'worldRightDirX': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldRightDirX),
        'worldRightDirY': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldRightDirY),
        'worldRightDirZ': "{:.2f}".format(packet.m_carMotionData[players_car].m_worldRightDirZ),
        'gForceLateral': "{:.2f}".format(packet.m_carMotionData[players_car].m_gForceLateral),
        'gForceLongitudinal': "{:.2f}".format(packet.m_carMotionData[players_car].m_gForceLongitudinal),
        'gForceVertical': "{:.2f}".format(packet.m_carMotionData[players_car].m_gForceVertical),
        'yaw': "{:.2f}".format(packet.m_carMotionData[players_car].m_yaw),
        'pitch': "{:.2f}".format(packet.m_carMotionData[players_car].m_pitch),
        'roll': "{:.2f}".format(packet.m_carMotionData[players_car].m_roll)
    },
    'suspensionPosition':{
        'RL': "{:.2f}".format(packet.m_suspensionPosition[0]),
        'RR': "{:.2f}".format(packet.m_suspensionPosition[1]),
        'FL': "{:.2f}".format(packet.m_suspensionPosition[2]),
        'FR': "{:.2f}".format(packet.m_suspensionPosition[3])
    },
    'suspensionVelocity':{
        'RL': "{:.2f}".format(packet.m_suspensionVelocity[0]),
        'RR': "{:.2f}".format(packet.m_suspensionVelocity[1]),
        'FL': "{:.2f}".format(packet.m_suspensionVelocity[2]),
        'FR': "{:.2f}".format(packet.m_suspensionVelocity[3])
    },
    'suspensionAcceleration':{
        'RL': "{:.2f}".format(packet.m_suspensionAcceleration[0]),
        'RR': "{:.2f}".format(packet.m_suspensionAcceleration[1]),
        'FL': "{:.2f}".format(packet.m_suspensionAcceleration[2]),
        'FR': "{:.2f}".format(packet.m_suspensionAcceleration[3])
    },
    'wheelSpeed':{
        'RL': "{:.2f}".format(packet.m_wheelSpeed[0]),
        'RR': "{:.2f}".format(packet.m_wheelSpeed[1]),
        'FL': "{:.2f}".format(packet.m_wheelSpeed[2]),
        'FR': "{:.2f}".format(packet.m_wheelSpeed[3])
    },
    'wheelSlip':{
        'RL': "{:.2f}".format(packet.m_wheelSlip[0]),
        'RR': "{:.2f}".format(packet.m_wheelSlip[1]),
        'FL': "{:.2f}".format(packet.m_wheelSlip[2]),
        'FR': "{:.2f}".format(packet.m_wheelSlip[3])
    },
    'localVelocityX': "{:.2f}".format(packet.m_localVelocityX),
    'localVelocityY':"{:.2f}".format( packet.m_localVelocityY),
    'localVelocityZ': "{:.2f}".format(packet.m_localVelocityZ),
    'angularVelocityX': "{:.2f}".format(packet.m_angularVelocityX),
    'angularVelocityY': "{:.2f}".format(packet.m_angularVelocityY),
    'angularVelocityZ': "{:.2f}".format(packet.m_angularVelocityZ),
    'angularAccelerationX': "{:.2f}".format(packet.m_angularAccelerationX),
    'angularAccelerationY': "{:.2f}".format(packet.m_angularAccelerationY),
    'angularAccelerationZ': "{:.2f}".format(packet.m_angularAccelerationZ),
    'frontWheelsAngle': "{:.2f}".format(packet.m_frontWheelsAngle)
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
    'marshalZones': 'N/A',
    'safetyCarStatus': safety_car_types[packet.m_safetyCarStatus], # 0 = no safety car, 1 = full safety car, 2 = virtual safety car
    'networkGame': network_game_types[packet.m_networkGame] # 0 = offline, 1 = online
    }

    return session_data_json


def LapData(packet):
    # pit_status_types = ['none', 'pitting', 'in pit area']
    # sector_types = ['sector1', 'sector2', 'sector3']
    # current_lap_invalid_types = ['valid', 'invalid']
    # driver_status_types = ['in garage', 'flying lap', 'in lap', 'out lap', 'on track']
    # result_status_types = ['invalid', 'inactive', 'active', 'finished', 'disqualified', 'not classified', 'retired']
    players_car = packet.m_header.m_playerCarIndex
    lap_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'lapData': {
        'lastLapTime': packet.m_lapData[players_car].m_lastLapTime,
        'currentLapTime': packet.m_lapData[players_car].m_currentLapTime,
        'bestLapTime': packet.m_lapData[players_car].m_bestLapTime,
        'sector1Time': packet.m_lapData[players_car].m_sector1Time,
        'sector2Time': packet.m_lapData[players_car].m_sector2Time,
        'lapDistance': packet.m_lapData[players_car].m_lapDistance,
        'totalDistance': packet.m_lapData[players_car].m_totalDistance,
        'safetyCarDelta': packet.m_lapData[players_car].m_safetyCarDelta,
        'carPosition': packet.m_lapData[players_car].m_carPosition,
        'currentLapNum': packet.m_lapData[players_car].m_currentLapNum,
        'pitStatus': packet.m_lapData[players_car].m_pitStatus, # 0 = none, 1 = pitting, 2 = in pit area
        'sector': packet.m_lapData[players_car].m_sector, # 0 = sector1, 1 = sector2, 2 = sector3
        'currentLapInvalid': packet.m_lapData[players_car].m_currentLapInvalid, # Current lap invalid - 0 = valid, 1 = invalid
        'penalties': packet.m_lapData[players_car].m_penalties,
        'gridPosition': packet.m_lapData[players_car].m_gridPosition,
        'driverStatus': packet.m_lapData[players_car].m_driverStatus, # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
        'resultStatus': packet.m_lapData[players_car].m_resultStatus, # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
    },
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
    'eventStringCode': ''.join(packet.m_eventStringCode)
    }

    return event_data_json


def ParticipantData(packet):
    # ai_controlled_types = ['Human', 'AI']
    # driver_id_types = ['Carlos Sainz', '', 'Daniel Ricciardo', 'Fernando Alonso', '', '', 'Kimi Raikkonen', 'Lewis Hamilton', 'Marcus Ericsson', 'Max Verstappen',
    #                     'Nico Hulkenburg', 'Kevin Magnussen', 'Romain Grosjean', 'Sebastian Vettel', 'Sergio Perez', 'Valtteri Bottas', '', 'Esteban Ocon', 'Stoffel Vandoorne',
    #                     'Lance Stroll', 'Arron Barnes', 'Martin Giles', 'Alex Murray', 'Lucas Roth', 'Igor Correria', 'Sophie Levasseur', 'Jonas Schiffer', 'Alain Forest', 'Jay Letourneau',
    #                     'Esto Saari', 'Yasar Atiyeh', 'Callisto Calabresi', 'Naota Izum', 'Howard Clarke', 'Wilheim Kaufmann', 'Marie Laursen', 'Flavio Nieves', 'Peter Belousov',
    #                     'Klimek Michalski', 'Santiago Moreno', 'Benjamin Coppens', 'Noah Visser', 'Gert Waldmuller', 'Julian Quesada', 'Daniel Jones', '', '', '', '', '', '', '', '', '',
    #                     '', '', '', '', 'Charles Leclerc', 'Pierre Gasly', 'Brendon Hartley', 'Sergey Siroktin', '', '', '', '', '', '', '', 'Ruben Meijer', 'Rashid Nair', 'Jack Tremblay']
    # team_id_types = ['Mercedes', 'Ferrari', 'Red Bull', 'Williams', 'Force India', 'Renault', 'Toro Rosso', 'Haas', 'McLaren', 'Sauber', 'McLaren 1988', 'McLaren 1991',
    #                 'Williams 1992', 'Ferrari 1995', 'Williams 1996', 'McLaren 1998', 'Ferrari 2002', 'Ferrari 2004', 'Renault 2006', 'Ferrari 2007', 'McLaren 2008', 'Red Bull 2008',
    #                 'Ferrari 1976', '', '', '', '', '', '', '', '', '', '', '', 'McLaren 1976', 'Lotus 1972', 'Ferrari 1979', 'McLaren 1982', 'Williams 2003', 'Brawn 2009', 'Lotus 1978']
    # nationality_types = ['American', 'Argentinean', 'Australian', 'Austrian', 'Azerbaijani', 'Bahraini', 'Belgian', 'Bolivian', 'Brazilian', 'British', 'Bulgarian', 'Camaroonian', 'Canadian',
    #                     'Chilean', 'Chinese', 'Columbian', 'Costa Rican', 'Croatian', 'Cypriot', 'Czech', 'Danish', 'Dutch', 'Ecuadorian', 'English', 'Emirian', 'Estonian', 'Finnish', 'French',
    #                     'German', 'Ghanian', 'Greek', 'Guatamalan', 'Honduran', 'Hong Konger', 'Hungarian', 'Icelander', 'Indian', 'Indonesian', 'Irish', 'Israeli', 'Italian', 'Jamacian',
    #                     'Japanese', 'Jordanian', 'Kuwati', 'Latvian', 'Lebanese', 'Lithuanian', 'Luxembourger', 'Malasaysian', 'Maltese', 'Mexican', 'Monegasque', 'New Zelander',
    #                     'Nicuraguan', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Panamanian', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian',
    #                     'Russian', 'Salvadoran', 'Saudi', 'Scottish', 'Serbian', 'Singaporean', 'Slovakian', 'Slovenien', 'South Korea', 'South African', 'Spanish', 'Swedish', 'Swiss',
    #                     'Taiwanese', 'Thai', 'Turkish', 'Uruguayan', 'Ukrainian', 'Venezuelan', 'Welsh']
    players_car = packet.m_header.m_playerCarIndex
    participant_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'numCars': packet.m_numCars,
    'participants':{
        'aiControlled': packet.m_participants[players_car].m_aiControlled, # Whether the vehicle is AI (1) or Human (0) controlled
        'driverId': packet.m_participants[players_car].m_driverId, # Driver id - see appendix
        'teamId': packet.m_participants[players_car].m_teamId, # Team id - see appendix
        'raceNumber': packet.m_participants[players_car].m_raceNumber,
        'nationality': packet.m_participants[players_car].m_nationality, # Nationality of the driver - see appendix
        'name': packet.m_participants[players_car].m_name
    },
    }

    return participant_data_json


def CarSetupData(packet):
    players_car = packet.m_header.m_playerCarIndex
    setup_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'carSetups': {
        'frontWing': packet.m_carSetups[players_car].m_frontWing,
        'rearWing': packet.m_carSetups[players_car].m_rearWing,
        'onThrottle': packet.m_carSetups[players_car].m_onThrottle,
        'offThrottle': packet.m_carSetups[players_car].m_offThrottle,
        'frontCamber': packet.m_carSetups[players_car].m_frontCamber,
        'rearCamber': packet.m_carSetups[players_car].m_rearCamber,
        'frontToe': packet.m_carSetups[players_car].m_frontToe,
        'rearToe': packet.m_carSetups[players_car].m_rearToe,
        'frontSuspension': packet.m_carSetups[players_car].m_frontSuspension,
        'rearSuspension': packet.m_carSetups[players_car].m_rearSuspension,
        'frontAntiRollBar': packet.m_carSetups[players_car].m_frontAntiRollBar,
        'rearAntiRollBar': packet.m_carSetups[players_car].m_rearAntiRollBar,
        'frontSuspensionHeight': packet.m_carSetups[players_car].m_frontSuspensionHeight,
        'rearSuspensionHeight': packet.m_carSetups[players_car].m_rearSuspensionHeight,
        'brakePressure': packet.m_carSetups[players_car].m_brakePressure,
        'brakeBias': packet.m_carSetups[players_car].m_brakeBias,
        'frontTyrePressure': packet.m_carSetups[players_car].m_frontTyrePressure,
        'rearTyrePressure': packet.m_carSetups[players_car].m_rearTyrePressure,
        'ballast': packet.m_carSetups[players_car].m_ballast,
        'fuelLoad': packet.m_carSetups[players_car].m_fuelLoad
    },
    }

    return setup_data_json


def CarTelemetryData(packet):
    # drs_types = ['off', 'on']
    # button_status_types = {'0x0001': 'Cross or A', '0x0002': 'Triangle or Y', '0x0004': 'Circle or B', '0x0008': 'Square or X', '0x0010': 'D-pad Left', '0x0020': 'D-pad Right',
    #                         '0x0040': 'D-pad Up', '0x0080': 'D-pad Down', '0x0100': 'Options or Menu', '0x0200': 'L1 or LB', '0x0400': 'R2 or RB', '0x0800': 'L2 or LT',
    #                         '0x1000': 'R2 or RT', '0x2000': 'Left Stick Click', '0x4000': 'Right Stick Click'}
    players_car = packet.m_header.m_playerCarIndex
    telemetry_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'carTelemetryData':{
        'speed': packet.m_carTelemetryData[players_car].m_speed,
        'throttle': packet.m_carTelemetryData[players_car].m_throttle,
        'steer': packet.m_carTelemetryData[players_car].m_steer,
        'brake': packet.m_carTelemetryData[players_car].m_brake,
        'clutch': packet.m_carTelemetryData[players_car].m_clutch,
        'gear': packet.m_carTelemetryData[players_car].m_gear,
        'engineRPM': packet.m_carTelemetryData[players_car].m_engineRPM,
        'drs': packet.m_carTelemetryData[players_car].m_drs,
        'revLightsPercent': packet.m_carTelemetryData[players_car].m_revLightsPercent,
        'brakesTemperature':{
            'RL': packet.m_carTelemetryData[players_car].m_brakesTemperature[0],
            'RR': packet.m_carTelemetryData[players_car].m_brakesTemperature[1],
            'FL': packet.m_carTelemetryData[players_car].m_brakesTemperature[2],
            'FR': packet.m_carTelemetryData[players_car].m_brakesTemperature[3]
        },
        'tyresSurfaceTemperature':{
            'RL': packet.m_carTelemetryData[players_car].m_tyresSurfaceTemperature[0],
            'RR': packet.m_carTelemetryData[players_car].m_tyresSurfaceTemperature[1],
            'FL': packet.m_carTelemetryData[players_car].m_tyresSurfaceTemperature[2],
            'FR': packet.m_carTelemetryData[players_car].m_tyresSurfaceTemperature[3]
        },
        'tyresInnerTemperature':{
            'RL': packet.m_carTelemetryData[players_car].m_tyresInnerTemperature[0],
            'RR': packet.m_carTelemetryData[players_car].m_tyresInnerTemperature[1],
            'FL': packet.m_carTelemetryData[players_car].m_tyresInnerTemperature[2],
            'FR': packet.m_carTelemetryData[players_car].m_tyresInnerTemperature[3]
        },
        'engineTemperature': packet.m_carTelemetryData[players_car].m_engineTemperature,
        'tyresPressure':{
            'RL': packet.m_carTelemetryData[players_car].m_tyresPressure[0],
            'RR': packet.m_carTelemetryData[players_car].m_tyresPressure[1],
            'FL': packet.m_carTelemetryData[players_car].m_tyresPressure[2],
            'FR': packet.m_carTelemetryData[players_car].m_tyresPressure[3]
        }
    },
    'buttonStatus': 'N/A'
    # 'buttonStatus': button_status_types[packet.m_buttonStatus]
    }

    return telemetry_data_json


def PacketCarStatusData(packet):
    # traction_control_types = ['off', '', 'high']
    # anti_lock_brakes_type = ['off', 'on']
    # fuel_mix_types = ['lean', 'standard', 'rich', 'max']
    # pit_limiter_types = ['off', 'on']
    # drs_allowed_types = ['not allowed', 'allowed']
    # tyre_compound_types = ['hyper soft', 'ultra soft', 'super soft', 'soft', 'medium', 'hard', 'super hard', 'inter', 'wet']
    # vehicle_fia_flags_types = ['none', 'green', 'blue', 'yellow', 'red']
    # ers_deploy_mode_types = ['none', 'low', 'medium', 'high', 'overtake', 'hotlap']
    players_car = packet.m_header.m_playerCarIndex
    status_data_json = {
    'header': {
        'packetFormat': packet.m_header.m_packetFormat,
        'packetVersion': packet.m_header.m_packetVersion,
        'packetId': packet.m_header.m_packetId,
        'sessionUID': packet.m_header.m_sessionUID,
        'sessionTime': packet.m_header.m_sessionTime,
        'frameIdentifier': packet.m_header.m_frameIdentifier,
        'playerCarIndex': players_car
    },
    'carStatusData':{
        'tractionControl': packet.m_carStatusData[players_car].m_tractionControl, # 0 (off) - 2 (high)
        'antiLockBrakes': packet.m_carStatusData[players_car].m_antiLockBrakes, # 0 (off) - 1 (on)
        'fuelMix': packet.m_carStatusData[players_car].m_fuelMix, # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        'frontBrakeBias': packet.m_carStatusData[players_car].m_frontBrakeBias,
        'pitLimiterStatus': packet.m_carStatusData[players_car].m_pitLimiterStatus, # Pit limiter status - 0 = off, 1 = on
        'fuelInTank': packet.m_carStatusData[players_car].m_fuelInTank,
        'fuelCapacity': packet.m_carStatusData[players_car].m_fuelCapacity,
        'maxRPM': packet.m_carStatusData[players_car].m_maxRPM,
        'idleRPM': packet.m_carStatusData[players_car].m_idleRPM,
        'maxGears': packet.m_carStatusData[players_car].m_maxGears,
        'drsAllowed': packet.m_carStatusData[players_car].m_drsAllowed, # 0 = not allowed, 1 = allowed, -1 = unknown
        # 'tyresWear': packet.m_carStatusData[players_car].m_tyresWear,
        'tyresWear':{
            'RL': packet.m_carStatusData[players_car].m_tyresWear[0],
            'RR': packet.m_carStatusData[players_car].m_tyresWear[1],
            'FL': packet.m_carStatusData[players_car].m_tyresWear[2],
            'FR': packet.m_carStatusData[players_car].m_tyresWear[3]
        },
        'tyreCompound': packet.m_carStatusData[players_car].m_tyreCompound, # Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet,  Classic - 0-6 = dry, 7-8 = wet
        'tyresDamage':{
            'RL': packet.m_carStatusData[players_car].m_tyresDamage[0],
            'RR': packet.m_carStatusData[players_car].m_tyresDamage[1],
            'FL': packet.m_carStatusData[players_car].m_tyresDamage[2],
            'FR': packet.m_carStatusData[players_car].m_tyresDamage[3]
        },
        'frontLeftWingDamage': packet.m_carStatusData[players_car].m_frontLeftWingDamage,
        'frontRightWingDamage': packet.m_carStatusData[players_car].m_frontRightWingDamage,
        'rearWingDamage': packet.m_carStatusData[players_car].m_rearWingDamage,
        'engineDamage': packet.m_carStatusData[players_car].m_engineDamage,
        'gearBoxDamage': packet.m_carStatusData[players_car].m_gearBoxDamage,
        'exhaustDamage': packet.m_carStatusData[players_car].m_exhaustDamage,
        'vehicleFiaFlags': packet.m_carStatusData[players_car].m_vehicleFiaFlags, # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        'ersStoreEnergy': packet.m_carStatusData[players_car].m_ersStoreEnergy,
        'ersDeployMode': packet.m_carStatusData[players_car].m_ersDeployMode, # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
        'ersHarvestedThisLapMGUK': packet.m_carStatusData[players_car].m_ersHarvestedThisLapMGUK,
        'ersHarvestedThisLapMGUH': packet.m_carStatusData[players_car].m_ersHarvestedThisLapMGUH,
        'ersDeployedThisLap': packet.m_carStatusData[players_car].m_ersDeployedThisLap
    },
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
