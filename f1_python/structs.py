# coding: utf-8
"""
UDP telemetry packet structures
"""

import ctypes


# MOTION PACKETs

class PacketHeader(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the UDP packet header
    """
    _pack_ = 1
    _fields_ = [
        ('m_packetFormat',              ctypes.c_uint16),       # 2018
        ('m_packetVersion',             ctypes.c_uint8),        # Version of this packet type, all start from 1
        ('m_packetId',                  ctypes.c_uint8),        # Identifier for the packet type, see below
        ('m_sessionUID',                ctypes.c_uint64),       # Unique identifier for the session
        ('m_sessionTime',               ctypes.c_float),        # Session timestamp
        ('m_frameIdentifier',           ctypes.c_uint),         # Identifier for the frame the data was retrieved on
        ('m_playerCarIndex',            ctypes.c_uint8),        # Index of player's car in the array
    ]

class CarMotionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_worldPositionX',            ctypes.c_float),        # World space X position
        ('m_worldPositionY',            ctypes.c_float),        # World space Y position
        ('m_worldPositionZ',            ctypes.c_float),        # World space Z position
        ('m_worldVelocityX',            ctypes.c_float),        # Velocity in world space X
        ('m_worldVelocityY',            ctypes.c_float),        # Velocity in world space Y
        ('m_worldVelocityZ',            ctypes.c_float),        # Velocity in world space Z
        ('m_worldForwardDirX',          ctypes.c_int16),        # World space forward X direction (normalised)
        ('m_worldForwardDirY',          ctypes.c_int16),        # World space forward Y direction (normalised)
        ('m_worldForwardDirZ',          ctypes.c_int16),        # World space forward Z direction (normalised)
        ('m_worldRightDirX',            ctypes.c_int16),        # World space right X direction (normalised)
        ('m_worldRightDirY',            ctypes.c_int16),        # World space right Y direction (normalised)
        ('m_worldRightDirZ',            ctypes.c_int16),        # World space right Z direction (normalised)
        ('m_gForceLateral',             ctypes.c_float),        # Lateral G-Force component
        ('m_gForceLongitudinal',        ctypes.c_float),        # Longitudinal G-Force component
        ('m_gForceVertical',            ctypes.c_float),        # Vertical G-Force component
        ('m_yaw',                       ctypes.c_float),        # Yaw angle in radians
        ('m_pitch',                     ctypes.c_float),        # Pitch angle in radians
        ('m_roll',                      ctypes.c_float),        # Roll angle in radians
    ]

# 'worldPositionX'
# 'worldPositionY'
# 'worldPositionZ'
# 'worldVelocityX'
# 'worldVelocityY'
# 'worldVelocityZ'
# 'worldForwardDirX'
# 'worldForwardDirY'
# 'worldForwardDirZ'
# 'worldRightDirX'
# 'worldRightDirY'
# 'worldRightDirZ'
# 'gForceLateral'
# 'gForceLongitudinal'
# 'gForceVertical'
# 'yaw'
# 'pitch'
# 'roll'

class PacketMotionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),          # Header
        ('m_carMotionData',             CarMotionData * 20),    # Data for all cars on track
                                                                # Extra player car ONLY data
        ('m_suspensionPosition',        ctypes.c_float * 4),    # Note: All wheel arrays have the following order:
        ('m_suspensionVelocity',        ctypes.c_float * 4),    # RL, RR, FL, FR
        ('m_suspensionAcceleration',    ctypes.c_float * 4),    # RL, RR, FL, FR
        ('m_wheelSpeed',                ctypes.c_float * 4),    # Speed of each wheel
        ('m_wheelSlip',                 ctypes.c_float * 4),    # Slip ratio for each wheel
        ('m_localVelocityX',            ctypes.c_float),        # Velocity in local space
        ('m_localVelocityY',            ctypes.c_float),        # Velocity in local space
        ('m_localVelocityZ',            ctypes.c_float),        # Velocity in local space
        ('m_angularVelocityX',          ctypes.c_float),        # Angular velocity x-component
        ('m_angularVelocityY',          ctypes.c_float),        # Angular velocity y-component
        ('m_angularVelocityZ',          ctypes.c_float),        # Angular velocity z-component
        ('m_angularAccelerationX',      ctypes.c_float),        # Angular velocity x-component
        ('m_angularAccelerationY',      ctypes.c_float),        # Angular velocity y-component
        ('m_angularAccelerationZ',      ctypes.c_float),        # Angular velocity z-component
        ('m_frontWheelsAngle',          ctypes.c_float),        # Current front wheels angle in radians
    ]






# SESSION PACKET

class MarshalZone(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_zoneStart',                 ctypes.c_float),        # Fraction (0..1) of way through the lap the marshal zone starts
        ('m_zoneFlag',                  ctypes.c_int8)          # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    ]

class PacketSessionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),           # Header
        ('m_weather',                   ctypes.c_uint8),         # Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                                	             # 3 = light rain, 4 = heavy rain, 5 = storm
        ('m_trackTemperature',          ctypes.c_int8),          # Track temp. in degrees celsius
        ('m_airTemperature',            ctypes.c_int8),          # Air temp. in degrees celsius
        ('m_totalLaps',                 ctypes.c_uint8),         # Total number of laps in this race
        ('m_trackLength',               ctypes.c_uint16),        # Track length in metres
        ('m_sessionType',               ctypes.c_uint8),         # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
                                                                 # 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
                                                                 # 10 = R, 11 = R2, 12 = Time Trial

        ('m_trackId',                   ctypes.c_int8),          # -1 for unknown, 0-21 for tracks, see appendix
        ('m_era',                       ctypes.c_uint8),         # Era, 0 = modern, 1 = classic
        ('m_sessionTimeLeft',           ctypes.c_uint16),        # Time left in session in seconds
        ('m_sessionDuration',           ctypes.c_uint16),        # Session duration in seconds
        ('m_pitSpeedLimit',             ctypes.c_uint8),         # Pit speed limit in kilometres per hour
        ('m_gamePaused',                ctypes.c_uint8),         # Whether the game is paused
        ('m_isSpectating',              ctypes.c_uint8),         # Whether the player is spectating
        ('m_spectatorCarIndex',         ctypes.c_uint8),         # Index of the car being spectated
        ('m_sliProNativeSupport',       ctypes.c_uint8),         # SLI Pro support, 0 = inactive, 1 = active
        ('m_numMarshalZones',           ctypes.c_uint8),         # Number of marshal zones to follow
        ('m_marshalZones',              MarshalZone * 21),       # List of marshal zones – max 21
        ('m_safetyCarStatus',           ctypes.c_uint8),         # 0 = no safety car, 1 = full safety car
                                                                 # 2 = virtual safety car


        ('m_networkGame',               ctypes.c_uint8),         # 0 = offline, 1 = online
    ]



# LAP DATA PACKET

class LapData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_lastLapTime',               ctypes.c_float),         # Last lap time in seconds
        ('m_currentLapTime',            ctypes.c_float),         # Current time around the lap in seconds
        ('m_bestLapTime',               ctypes.c_float),         # Best lap time of the session in seconds
        ('m_sector1Time',               ctypes.c_float),         # Sector 1 time in seconds
        ('m_sector2Time',               ctypes.c_float),         # Sector 2 time in seconds
        ('m_lapDistance',               ctypes.c_float),         # Distance vehicle is around current lap in metres – could
                                                                 # be negative if line hasn’t been crossed yet


        ('m_totalDistance',             ctypes.c_float),         # Total distance travelled in session in metres – could
                                                                 # be negative if line hasn’t been crossed yet

        ('m_safetyCarDelta',            ctypes.c_float),         # Delta in seconds for safety car
        ('m_carPosition',               ctypes.c_uint8),         # Car race position
        ('m_currentLapNum',             ctypes.c_uint8),         # Current lap number
        ('m_pitStatus',                 ctypes.c_uint8),         # 0 = none, 1 = pitting, 2 = in pit area
        ('m_sector',                    ctypes.c_uint8),         # 0 = sector1, 1 = sector2, 2 = sector3
        ('m_currentLapInvalid',         ctypes.c_uint8),         # Current lap invalid - 0 = valid, 1 = invalid
        ('m_penalties',                 ctypes.c_uint8),         # Accumulated time penalties in seconds to be added
        ('m_gridPosition',              ctypes.c_uint8),         # Grid position the vehicle started the race in
        ('m_driverStatus',              ctypes.c_uint8),         # Status of driver - 0 = in garage, 1 = flying lap
                                                                 # 2 = in lap, 3 = out lap, 4 = on track

        ('m_resultStatus',              ctypes.c_uint8),         # Result status - 0 = invalid, 1 = inactive, 2 = active
                                                                 # 3 = finished, 4 = disqualified, 5 = not classified
                                                                 # 6 = retired

    ]

class PacketLapData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),           # Header

        ('m_lapData',                   LapData * 20),           # Lap data for all cars on track
    ]




# EVENT PACKET

class PacketEventData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),           # Header

        ('m_eventStringCode',           ctypes.c_char * 4),     # Event string code, see above
    ]




# PARTICIPANTS PACKET

class ParticipantData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_aiControlled',              ctypes.c_uint8),         # Whether the vehicle is AI (1) or Human (0) controlled
        ('m_driverId',                  ctypes.c_uint8),         # Driver id - see appendix
        ('m_teamId',                    ctypes.c_uint8),         # Team id - see appendix
        ('m_raceNumber',                ctypes.c_uint8),         # Race number of the car
        ('m_nationality',               ctypes.c_uint8),         # Nationality of the driver
        ('m_name',                      ctypes.c_char),          # Name of participant in UTF-8 format – null terminated
                                                                 # Will be truncated with … (U+2026) if too long
    ]

class PacketParticipantsData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),           # Header
        ('m_numCars',                   ctypes.c_uint8),                  # Number of cars in the data
        ('m_participants',              ParticipantData * 20),
    ]



# CAR SETUPS PACKET

class CarSetupData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_frontWing',                 ctypes.c_uint8),         # Front wing aero
        ('m_rearWing',                  ctypes.c_uint8),         # Rear wing aero
        ('m_onThrottle',                ctypes.c_uint8),         # Differential adjustment on throttle (percentage)
        ('m_offThrottle',               ctypes.c_uint8),         # Differential adjustment off throttle (percentage)
        ('m_frontCamber',               ctypes.c_float),         # Front camber angle (suspension geometry)
        ('m_rearCamber',                ctypes.c_float),         # Rear camber angle (suspension geometry)
        ('m_frontToe',                  ctypes.c_float),         # Front toe angle (suspension geometry)
        ('m_rearToe',                   ctypes.c_float),         # Rear toe angle (suspension geometry)
        ('m_frontSuspension',           ctypes.c_uint8),         # Front suspension
        ('m_rearSuspension',            ctypes.c_uint8),         # Rear suspension
        ('m_frontAntiRollBar',          ctypes.c_uint8),         # Front anti-roll bar
        ('m_rearAntiRollBar',           ctypes.c_uint8),         # Front anti-roll bar
        ('m_frontSuspensionHeight',     ctypes.c_uint8),         # Front ride height
        ('m_rearSuspensionHeight',      ctypes.c_uint8),         # Rear ride height
        ('m_brakePressure',             ctypes.c_uint8),         # Brake pressure (percentage)
        ('m_brakeBias',                 ctypes.c_uint8),         # Brake bias (percentage)
        ('m_frontTyrePressure',         ctypes.c_float),         # Front tyre pressure (PSI)
        ('m_rearTyrePressure',          ctypes.c_float),         # Rear tyre pressure (PSI)
        ('m_ballast',                   ctypes.c_uint8),         # Ballast
        ('m_fuelLoad',                  ctypes.c_float),         # Fuel load
    ]


class PacketCarSetupData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),           # Header
        ('m_carSetups',                 CarSetupData * 20),
    ]




# CAR TELEMETRY PACKET

class CarTelemetryData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_speed',                     ctypes.c_uint16),       # Speed of car in kilometres per hour
        ('m_throttle',                  ctypes.c_uint8),        # Amount of throttle applied (0 to 100)
        ('m_steer',                     ctypes.c_int8),         # Steering (-100 (full lock left) to 100 (full lock right))
        ('m_brake',                     ctypes.c_uint8),        # Amount of brake applied (0 to 100)
        ('m_clutch',                    ctypes.c_uint8),        # Amount of clutch applied (0 to 100)
        ('m_gear',                      ctypes.c_int8),         # Gear selected (1-8, N=0, R=-1)
        ('m_engineRPM',                 ctypes.c_uint16),       # Engine RPM
        ('m_drs',                       ctypes.c_uint8),        # 0 = off, 1 = on
        ('m_revLightsPercent',          ctypes.c_uint8),        # Rev lights indicator (percentage)
        ('m_brakesTemperature',         ctypes.c_uint16 * 4),   # Brakes temperature (celsius)
        ('m_tyresSurfaceTemperature',   ctypes.c_uint16 * 4),   # Tyres surface temperature (celsius)
        ('m_tyresInnerTemperature',     ctypes.c_uint16 * 4),   # Tyres inner temperature (celsius)
        ('m_engineTemperature',         ctypes.c_uint16),       # Engine temperature (celsius)
        ('m_tyresPressure',             ctypes.c_float * 4),    # Tyres pressure (PSI)
    ]

class PacketCarTelemetryData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),          # Header
        ('m_carTelemetryData',          CarTelemetryData * 20),
        ('m_buttonStatus',              ctypes.c_uint32),       # Bit flags specifying which buttons are being
                                                                # pressed currently - see appendices
    ]




# CAR STATUS PACKET

class CarStatusData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_tractionControl',           ctypes.c_uint8),        # 0 (off) - 2 (high)
        ('m_antiLockBrakes',            ctypes.c_uint8),        # 0 (off) - 1 (on)
        ('m_fuelMix',                   ctypes.c_uint8),        # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ('m_frontBrakeBias',            ctypes.c_uint8),        # Front brake bias (percentage)
        ('m_pitLimiterStatus',          ctypes.c_uint8),        # Pit limiter status - 0 = off, 1 = on
        ('m_fuelInTank',                ctypes.c_float),        # Current fuel mass
        ('m_fuelCapacity',              ctypes.c_float),        # Fuel capacity
        ('m_maxRPM',                    ctypes.c_uint16),       # Cars max RPM, point of rev limiter
        ('m_idleRPM',                   ctypes.c_uint16),       # Cars idle RPM
        ('m_maxGears',                  ctypes.c_uint8),        # Maximum number of gears
        ('m_drsAllowed',                ctypes.c_uint8),        # 0 = not allowed, 1 = allowed, -1 = unknown
        ('m_tyresWear',                 ctypes.c_uint8 * 4),        # Tyre wear percentage
        ('m_tyreCompound',              ctypes.c_uint8),        # Modern - 0 = hyper soft, 1 = ultra soft
                                                                # 2 = super soft, 3 = soft, 4 = medium, 5 = hard
                                                                # 6 = super hard, 7 = inter, 8 = wet
                                                                # Classic - 0-6 = dry, 7-8 = wet
        ('m_tyresDamage',               ctypes.c_uint8 * 4),    # Tyre damage (percentage)
        ('m_frontLeftWingDamage',       ctypes.c_uint8),        # Front left wing damage (percentage)
        ('m_frontRightWingDamage',      ctypes.c_uint8),        # Front right wing damage (percentage)
        ('m_rearWingDamage',            ctypes.c_uint8),        # Rear wing damage (percentage)
        ('m_engineDamage',              ctypes.c_uint8),        # Engine damage (percentage)
        ('m_gearBoxDamage',             ctypes.c_uint8),        # Gear box damage (percentage)
        ('m_exhaustDamage',             ctypes.c_uint8),        # Exhaust damage (percentage)
        ('m_vehicleFiaFlags',           ctypes.c_int8),         # -1 = invalid/unknown, 0 = none, 1 = green
                                                                # 2 = blue, 3 = yellow, 4 = red

        ('m_ersStoreEnergy',            ctypes.c_float),        # ERS energy store in Joules
        ('m_ersDeployMode',             ctypes.c_uint8),        # ERS deployment mode, 0 = none, 1 = low, 2 = medium
                                                                # 3 = high, 4 = overtake, 5 = hotlap

        ('m_ersHarvestedThisLapMGUK',   ctypes.c_float),        # ERS energy harvested this lap by MGU-K
        ('m_ersHarvestedThisLapMGUH',   ctypes.c_float),        # ERS energy harvested this lap by MGU-H
        ('m_ersDeployedThisLap',        ctypes.c_float),        # ERS energy deployed this lap
    ]

class PacketCarStatusData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',                    PacketHeader),          # Header
        ('m_carStatusData',             CarStatusData * 20 ),
    ]
