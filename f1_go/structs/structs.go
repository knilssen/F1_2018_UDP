package structs

type PacketHeader struct {
    M_packetFormat                uint16                  // 2018
    M_packetVersion               uint8                   // Version of this packet type, all start from 1
    M_packetId                    uint8                   // Identifier for the packet type, see below
    M_sessionUID                  uint64                  // Unique identifier for the session
    M_sessionTime                 float32                 // Session timestamp
    M_frameIdentifier             uint32                  // Identifier for the frame the data was retrieved on
    M_playerCarIndex              uint8                   // Index of player's car in the array
}

// MOTION PACKET:
// The motion packet gives physics data for all the cars being driven.
// There is additional data for the car being driven with the goal of being able to drive a motion platform setup.
// Frequency: Rate as specified in menus
// Size: 1341 bytes
type CarMotionData struct {
    M_worldPositionX              float32                  // World space X position
    M_worldPositionY              float32                  // World space Y position
    M_worldPositionZ              float32                  // World space Z position
    M_worldVelocityX              float32                  // Velocity in world space X
    M_worldVelocityY              float32                  // Velocity in world space Y
    M_worldVelocityZ              float32                  // Velocity in world space Z
    M_worldForwardDirX            int16                    // World space forward X direction (normalised)
    M_worldForwardDirY            int16                    // World space forward Y direction (normalised)
    M_worldForwardDirZ            int16                    // World space forward Z direction (normalised)
    M_worldRightDirX              int16                    // World space right X direction (normalised)
    M_worldRightDirY              int16                    // World space right Y direction (normalised)
    M_worldRightDirZ              int16                    // World space right Z direction (normalised)
    M_gForceLateral               float32                  // Lateral G-Force component
    M_gForceLongitudinal          float32                  // Longitudinal G-Force component
    M_gForceVertical              float32                  // Vertical G-Force component
    M_yaw                         float32                  // Yaw angle in radians
    M_pitch                       float32                  // Pitch angle in radians
    M_roll                        float32                  // Roll angle in radians
}
type PacketMotionData struct {
    M_header  PacketHeader                                 // Header

    M_carMotionData[20]           CarMotionData            // Data for all cars on track

    // Extra player car ONLY data
    M_suspensionPosition[4]       float32                  // Note: All wheel arrays have the following order:
    M_suspensionVelocity[4]       float32                  // RL, RR, FL, FR
    M_suspensionAcceleration[4]   float32                  // RL, RR, FL, FR
    M_wheelSpeed[4]               float32                  // Speed of each wheel
    M_wheelSlip[4]                float32                  // Slip ratio for each wheel
    M_localVelocityX              float32                  // Velocity in local space
    M_localVelocityY              float32                  // Velocity in local space
    M_localVelocityZ              float32                  // Velocity in local space
    M_angularVelocityX            float32                  // Angular velocity x-component
    M_angularVelocityY            float32                  // Angular velocity y-component
    M_angularVelocityZ            float32                  // Angular velocity z-component
    M_angularAccelerationX        float32                  // Angular velocity x-component
    M_angularAccelerationY        float32                  // Angular velocity y-component
    M_angularAccelerationZ        float32                  // Angular velocity z-component
    M_frontWheelsAngle            float32                  // Current front wheels angle in radians
}

// SESSION PACKET:
// The session packet includes details about the current session in progress.
// Frequency: 2 per second
// Size: 147 bytes
type MarshalZone struct {
    M_zoneStart                   float32                  // Fraction (0..1) of way through the lap the marshal zone starts
    M_zoneFlag                    int8                     // -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
}
type PacketSessionData struct {
    M_header                      PacketHeader             // Header

    M_weather                     uint8                    // Weather - 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy rain, 5 = storm
    M_trackTemperature            int8	        	       // Track temp. in degrees celsius
    M_airTemperature              int8	                   // Air temp. in degrees celsius
    M_totalLaps                   uint8                    // Total number of laps in this race
    M_trackLength                 uint16                   // Track length in metre
    M_sessionType                 uint8                    // 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2, 12 = Time Trial
    M_trackId                     int8                 	   // -1 for unknown, 0-21 for tracks, see appendix
    M_era                         uint8                    // Era, 0 = modern, 1 = classic
    M_sessionTimeLeft             uint16             	   // Time left in session in seconds
    M_sessionDuration             uint16                   // Session duration in seconds
    M_pitSpeedLimit               uint8                    // Pit speed limit in kilometres per hour
    M_gamePaused                  uint8                    // Whether the game is paused
    M_isSpectating                uint8                	   // Whether the player is spectating
    M_spectatorCarIndex           uint8            	       // Index of the car being spectated
    M_sliProNativeSupport         uint8          	       // SLI Pro support, 0 = inactive, 1 = active
    M_numMarshalZones             uint8                    // Number of marshal zones to follow
    M_marshalZones[21]            MarshalZone              // List of marshal zones – max 21
    M_safetyCarStatus             uint8                    // 0 = no safety car, 1 = full safety car, 2 = virtual safety car
    M_networkGame                 uint8                    // 0 = offline, 1 = online
}

// LAP DATA PACKET:
// The lap data packet gives details of all the cars in the session.
// Frequency: Rate as specified in menus
// Size: 841 bytes
type LapData struct {
    M_lastLapTime                 float32                  // Last lap time in seconds
    M_currentLapTime              float32                  // Current time around the lap in seconds
    M_bestLapTime                 float32                  // Best lap time of the session in seconds
    M_sector1Time                 float32                  // Sector 1 time in seconds
    M_sector2Time                 float32                  // Sector 2 time in seconds
    M_lapDistance                 float32                  // Distance vehicle is around current lap in metres – could be negative if line hasn’t been crossed yet
    M_totalDistance               float32                  // Total distance travelled in session in metres – could be negative if line hasn’t been crossed yet
    M_safetyCarDelta              float32                  // Delta in seconds for safety car
    M_carPosition                 uint8                    // Car race position
    M_currentLapNum               uint8                    // Current lap number
    M_pitStatus                   uint8                    // 0 = none, 1 = pitting, 2 = in pit area
    M_sector                      uint8                    // 0 = sector1, 1 = sector2, 2 = sector3
    M_currentLapInvalid           uint8                    // Current lap invalid - 0 = valid, 1 = invalid
    M_penalties                   uint8                    // Accumulated time penalties in seconds to be added
    M_gridPosition                uint8                    // Grid position the vehicle started the race in
    M_driverStatus                uint8                    // Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap, 3 = out lap, 4 = on track
    M_resultStatus                uint8                    // Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = disqualified, 5 = not classified, 6 = retired
}
type PacketLapData struct {
    M_header                      PacketHeader             // Header

    M_lapData[20]                 LapData                  // Lap data for all cars on track
}

// EVENT PACKET:
// This packet gives details of events that happen during the course of the race.
// Frequency: When the event occurs
// Size: 25 bytes
type PacketEventData struct {
    M_header                      PacketHeader             // Header

    M_eventStringCode[4]          uint8                    // Event string code, see above
}

// PARTICIPANTS PACKET:
// This is a list of participants in the race. If the vehicle is controlled by AI, then the name will be the driver name.
// If this is a multiplayer game, the names will be the Steam Id on PC, or the LAN name if appropriate.
// On Xbox One, the names will always be the driver name, on PS4 the name will be the LAN name if playing a LAN game, otherwise it will be the driver name.
// Frequency: Every 5 seconds
// Size: 1082 bytes
type ParticipantData struct {
    M_aiControlled                uint8                    // Whether the vehicle is AI (1) or Human (0) controlled
    M_driverId                    uint8                    // Driver id - see appendix
    M_teamId                      uint8                    // Team id - see appendix
    M_raceNumber                  uint8                    // Race number of the car
    M_nationality                 uint8                    // Nationality of the driver
    M_name[48]                    string                   // Name of participant in UTF-8 format – null terminated, Will be truncated with … (U+2026) if too long
}
type PacketParticipantsData struct {
    M_header                      PacketHeader             // Header

    M_numCars                     uint8                    // Number of cars in the data
    M_participants[20]            ParticipantData
}

// CAR SETUPS PACKET:
// This packet details the car setups for each vehicle in the session.
// Note that in multiplayer games, other player cars will appear as blank, you will only be able to see your car setup and AI cars.
// Frequency: Every 5 seconds
// Size: 841 bytes
type CarSetupData struct {
    M_frontWing                   uint8                    // Front wing aero
    M_rearWing                    uint8                    // Rear wing aero
    M_onThrottle                  uint8                    // Differential adjustment on throttle (percentage)
    M_offThrottle                 uint8                    // Differential adjustment off throttle (percentage)
    M_frontCamber                 float32                  // Front camber angle (suspension geometry)
    M_rearCamber                  float32                  // Rear camber angle (suspension geometry)
    M_frontToe                    float32                  // Front toe angle (suspension geometry)
    M_rearToe                     float32                  // Rear toe angle (suspension geometry)
    M_frontSuspension             uint8                    // Front suspension
    M_rearSuspension              uint8                    // Rear suspension
    M_frontAntiRollBar            uint8                    // Front anti-roll bar
    M_rearAntiRollBar             uint8                    // Front anti-roll bar
    M_frontSuspensionHeight       uint8                    // Front ride height
    M_rearSuspensionHeight        uint8                    // Rear ride height
    M_brakePressure               uint8                    // Brake pressure (percentage)
    M_brakeBias                   uint8                    // Brake bias (percentage)
    M_frontTyrePressure           float32                  // Front tyre pressure (PSI)
    M_rearTyrePressure            float32                  // Rear tyre pressure (PSI)
    M_ballast                     uint8                    // Ballast
    M_fuelLoad                    float32                  // Fuel load
}
type PacketCarSetupData struct {
    M_header                      PacketHeader             // Header

    M_carSetups[20]               CarSetupData
}

// CAR TELEMETRY PACKET:
// This packet details telemetry for all the cars in the race.
// It details various values that would be recorded on the car such as speed, throttle application, DRS etc.
// Frequency: Rate as specified in menus
// Size: 1085 bytes
type CarTelemetryData struct {
    M_speed                       uint16                   // Speed of car in kilometres per hour
    M_throttle                    uint8                    // Amount of throttle applied (0 to 100)
    M_steer                       int8                     // Steering (-100 (full lock left) to 100 (full lock right))
    M_brake                       uint8                    // Amount of brake applied (0 to 100)
    M_clutch                      uint8                    // Amount of clutch applied (0 to 100)
    M_gear                        int8                     // Gear selected (1-8, N=0, R=-1)
    M_engineRPM                   uint16                   // Engine RPM
    M_drs                         uint8                    // 0 = off, 1 = on
    M_revLightsPercent            uint8                    // Rev lights indicator (percentage)
    M_brakesTemperature[4]        uint16                   // Brakes temperature (celsius)
    M_tyresSurfaceTemperature[4]  uint16                   // Tyres surface temperature (celsius)
    M_tyresInnerTemperature[4]    uint16                   // Tyres inner temperature (celsius)
    M_engineTemperature           uint16                   // Engine temperature (celsius)
    M_tyresPressure[4]            float32                  // Tyres pressure (PSI)
}
type PacketCarTelemetryData struct {
    M_header                      PacketHeader             // Header

    M_carTelemetryData[20]        CarTelemetryData

    M_buttonStatus                uint32                   // Bit flags specifying which buttons are being pressed currently - see appendices
}

// CAR STATUS PACKET:
// This packet details car statuses for all the cars in the race. It includes values such as the damage readings on the car.
// Frequency: 2 per second
// Size: 1061 bytes
type CarStatusData struct {
    M_tractionControl             uint8                    // 0 (off) - 2 (high)
    M_antiLockBrakes              uint8                    // 0 (off) - 1 (on)
    M_fuelMix                     uint8                    // Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    M_frontBrakeBias              uint8                    // Front brake bias (percentage)
    M_pitLimiterStatus            uint8                    // Pit limiter status - 0 = off, 1 = on
    M_fuelInTank                  float32                  // Current fuel mass
    M_fuelCapacity                float32                  // Fuel capacity
    M_maxRPM                      uint16                   // Cars max RPM, point of rev limiter
    M_idleRPM                     uint16                   // Cars idle RPM
    M_maxGears                    uint8                    // Maximum number of gears
    M_drsAlloweds                 uint8                    // 0 = not allowed, 1 = allowed, -1 = unknown
    M_tyresWear[4]                uint8                    // Tyre wear percentage
    M_tyreCompound                uint8                    // Modern - 0 = hyper soft, 1 = ultra soft, 2 = super soft, 3 = soft, 4 = medium, 5 = hard, 6 = super hard, 7 = inter, 8 = wet, Classic - 0-6 = dry, 7-8 = wet
    M_tyresDamage[4]              uint8                    // Tyre damage (percentage)
    M_frontLeftWingDamage         uint8                    // Front left wing damage (percentage)
    M_frontRightWingDamage        uint8                    // Front right wing damage (percentage)
    M_rearWingDamage              uint8                    // Rear wing damage (percentage)
    M_engineDamage                uint8                    // Engine damage (percentage)
    M_gearBoxDamage               uint8                    // Gear box damage (percentage)
    M_exhaustDamage               uint8                    // Exhaust damage (percentage)
    M_vehicleFiaFlags             int8                     // -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    M_ersStoreEnergy              float32                  // ERS energy store in Joules
    M_ersDeployMode               uint8                    // ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high, 4 = overtake, 5 = hotlap
    M_ersHarvestedThisLapMGUK     float32                  // ERS energy harvested this lap by MGU-K
    M_ersHarvestedThisLapMGUH     float32                  // ERS energy harvested this lap by MGU-H
    M_ersDeployedThisLap          float32                  // ERS energy deployed this lap
}
type PacketCarStatusData struct {
    M_header                      PacketHeader             // Header

    M_carStatusData[20]           CarStatusData
}
