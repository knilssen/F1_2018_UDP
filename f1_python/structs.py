# coding: utf-8
"""
UDP telemetry packet structures
"""

import ctypes



class PacketHeader(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the UDP packet header
    """
    _pack_ = 1
    _fields_ = [
        ('m_packetFormat',    ctypes.c_uint16),   # 2018
        ('m_packetVersion',    ctypes.c_uint8),  # Version of this packet type, all start from 1
        ('m_packetId',    ctypes.c_uint8),       # Identifier for the packet type, see below
        ('m_sessionUID',    ctypes.c_uint64),     # Unique identifier for the session
        ('m_sessionTime',    ctypes.c_float),   # Session timestamp
        ('m_frameIdentifier',    ctypes.c_uint),# Identifier for the frame the data was retrieved on
        ('m_playerCarIndex',    ctypes.c_uint8), # Index of player's car in the array
    ]

class CarMotionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_worldPositionX',    ctypes.c_float),    # World space X position
        ('m_worldPositionY',    ctypes.c_float),    # World space Y position
        ('m_worldPositionZ',    ctypes.c_float),    # World space Z position
        ('m_worldVelocityX',    ctypes.c_float),    # Velocity in world space X
        ('m_worldVelocityY',    ctypes.c_float),    # Velocity in world space Y
        ('m_worldVelocityZ',    ctypes.c_float),    # Velocity in world space Z
        ('m_worldForwardDirX',    ctypes.c_int16),     # World space forward X direction (normalised)
        ('m_worldForwardDirY',    ctypes.c_int16),     # World space forward Y direction (normalised)
        ('m_worldForwardDirZ',    ctypes.c_int16),     # World space forward Z direction (normalised)
        ('m_worldRightDirX',    ctypes.c_int16),     # World space right X direction (normalised)
        ('m_worldRightDirY',    ctypes.c_int16),     # World space right Y direction (normalised)
        ('m_worldRightDirZ',    ctypes.c_int16),     # World space right Z direction (normalised)
        ('m_gForceLateral',    ctypes.c_float),    # Lateral G-Force component
        ('m_gForceLongitudinal',    ctypes.c_float),    # Longitudinal G-Force component
        ('m_gForceVertical',    ctypes.c_float),    # Vertical G-Force component
        ('m_yaw',    ctypes.c_float),    # Yaw angle in radians
        ('m_pitch',    ctypes.c_float),    # Pitch angle in radians
        ('m_roll',    ctypes.c_float),    # Roll angle in radians
    ]


class PacketMotionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',    PacketHeader),                 # Header
        ('m_carMotionData',     CarMotionData * 20),        # Data for all cars on track
        # Extra player car ONLY data
        ('m_suspensionPosition',    ctypes.c_float * 4),    # Note: All wheel arrays have the following order:
        ('m_suspensionVelocity',    ctypes.c_float * 4),    # RL, RR, FL, FR
        ('m_suspensionAcceleration',    ctypes.c_float * 4),    # RL, RR, FL, FR
        ('m_wheelSpeed',    ctypes.c_float * 4),            # Speed of each wheel
        ('m_wheelSlip',    ctypes.c_float * 4),             # Slip ratio for each wheel
        ('m_localVelocityX',    ctypes.c_float),            # Velocity in local space
        ('m_localVelocityY',    ctypes.c_float),            # Velocity in local space
        ('m_localVelocityZ',    ctypes.c_float),            # Velocity in local space
        ('m_angularVelocityX',    ctypes.c_float),          # Angular velocity x-component
        ('m_angularVelocityY',    ctypes.c_float),          # Angular velocity y-component
        ('m_angularVelocityZ',    ctypes.c_float),          # Angular velocity z-component
        ('m_angularAccelerationX',    ctypes.c_float),      # Angular velocity x-component
        ('m_angularAccelerationY',    ctypes.c_float),      # Angular velocity y-component
        ('m_angularAccelerationZ',    ctypes.c_float),      # Angular velocity z-component
        ('m_frontWheelsAngle',    ctypes.c_float),          # Current front wheels angle in radians
    ]








class MarshalZone(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_zoneStart', ctypes.c_float),   # Fraction (0..1) of way through the lap the marshal zone starts
        ('m_zoneFlag', ctypes.c_int8)    # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    ]

class PacketSessionData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2018 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('m_header',    PacketHeader),                 # Header
        ('m_weather', ctypes.c_uint8),                # Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                                	# 3 = light rain, 4 = heavy rain, 5 = storm
        ('m_trackTemperature', ctypes.c_int8),        # Track temp. in degrees celsius
        ('m_airTemperature', ctypes.c_int8),          # Air temp. in degrees celsius
        ('m_totalLaps', ctypes.c_uint8),              # Total number of laps in this race
        ('m_trackLength', ctypes.c_uint16),           # Track length in metres
        ('m_sessionType', ctypes.c_uint8),            # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
                                                	# 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
                                                	# 10 = R, 11 = R2, 12 = Time Trial

        ('m_trackId', ctypes.c_int8),                 # -1 for unknown, 0-21 for tracks, see appendix
        ('m_era', ctypes.c_uint8),                    # Era, 0 = modern, 1 = classic
        ('m_sessionTimeLeft', ctypes.c_uint16),       # Time left in session in seconds
        ('m_sessionDuration', ctypes.c_uint16),       # Session duration in seconds
        ('m_pitSpeedLimit', ctypes.c_uint8),          # Pit speed limit in kilometres per hour
        ('m_gamePaused', ctypes.c_uint8),             # Whether the game is paused
        ('m_isSpectating', ctypes.c_uint8),           # Whether the player is spectating
        ('m_spectatorCarIndex', ctypes.c_uint8),      # Index of the car being spectated
        ('m_sliProNativeSupport', ctypes.c_uint8),    # SLI Pro support, 0 = inactive, 1 = active
        ('m_numMarshalZones', ctypes.c_uint8),        # Number of marshal zones to follow
        ('m_marshalZones', MarshalZone * 21),       # List of marshal zones – max 21
        ('m_safetyCarStatus', ctypes.c_uint8),        # 0 = no safety car, 1 = full safety car
                                                    # 2 = virtual safety car


        ('m_networkGame', ctypes.c_uint8),           # 0 = offline, 1 = online
    ]
