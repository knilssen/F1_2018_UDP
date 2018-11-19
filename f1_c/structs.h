//
// UDP telemetry packet structures
//
// Author: Kristian Nilssen
//

// #include <stdint.h>
// #include <inttypes.h>

struct PacketHeader {
    uint16_t    m_packetFormat;         // 2018
    uint8_t     m_packetVersion;        // Version of this packet type, all start from 1
    uint8_t     m_packetId;             // Identifier for the packet type, see below
    uint64_t    m_sessionUID;           // Unique identifier for the session
    float       m_sessionTime;          // Session timestamp
    uint        m_frameIdentifier;      // Identifier for the frame the data was retrieved on
    uint8_t     m_playerCarIndex;       // Index of player's car in the array
}__attribute__((packed));

// MOTION PACKET:
// The motion packet gives physics data for all the cars being driven.
// There is additional data for the car being driven with the goal of being able to drive a motion platform setup.
// Frequency: Rate as specified in menus
// Size: 1341 bytes
struct CarMotionData {
    float         m_worldPositionX;           // World space X position
    float         m_worldPositionY;           // World space Y position
    float         m_worldPositionZ;           // World space Z position
    float         m_worldVelocityX;           // Velocity in world space X
    float         m_worldVelocityY;           // Velocity in world space Y
    float         m_worldVelocityZ;           // Velocity in world space Z
    int16_t       m_worldForwardDirX;         // World space forward X direction (normalised)
    int16_t       m_worldForwardDirY;         // World space forward Y direction (normalised)
    int16_t       m_worldForwardDirZ;         // World space forward Z direction (normalised)
    int16_t       m_worldRightDirX;           // World space right X direction (normalised)
    int16_t       m_worldRightDirY;           // World space right Y direction (normalised)
    int16_t       m_worldRightDirZ;           // World space right Z direction (normalised)
    float         m_gForceLateral;            // Lateral G-Force component
    float         m_gForceLongitudinal;       // Longitudinal G-Force component
    float         m_gForceVertical;           // Vertical G-Force component
    float         m_yaw;                      // Yaw angle in radians
    float         m_pitch;                    // Pitch angle in radians
    float         m_roll;                     // Roll angle in radians
}__attribute__((packed));
struct PacketMotionData {
    struct PacketHeader    m_header;               // Header

    struct CarMotionData   m_carMotionData[20];    // Data for all cars on track

    // Extra player car ONLY data
    float         m_suspensionPosition[4];       // Note: All wheel arrays have the following order:
    float         m_suspensionVelocity[4];       // RL, RR, FL, FR
    float         m_suspensionAcceleration[4];   // RL, RR, FL, FR
    float         m_wheelSpeed[4];               // Speed of each wheel
    float         m_wheelSlip[4];                // Slip ratio for each wheel
    float         m_localVelocityX;              // Velocity in local space
    float         m_localVelocityY;              // Velocity in local space
    float         m_localVelocityZ;              // Velocity in local space
    float         m_angularVelocityX;            // Angular velocity x-component
    float         m_angularVelocityY;            // Angular velocity y-component
    float         m_angularVelocityZ;            // Angular velocity z-component
    float         m_angularAccelerationX;        // Angular velocity x-component
    float         m_angularAccelerationY;        // Angular velocity y-component
    float         m_angularAccelerationZ;        // Angular velocity z-component
    float         m_frontWheelsAngle;            // Current front wheels angle in radians
}__attribute__((packed));

// SESSION PACKET:
// The session packet includes details about the current session in progress.
// Frequency: 2 per second
// Size: 147 bytes
struct MarshalZone {
    float  m_zoneStart;   // Fraction (0..1) of way through the lap the marshal zone starts
    int8_t   m_zoneFlag;    // -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
}__attribute__((packed));
struct PacketSessionData {
    struct PacketHeader    m_header;               	// Header

    uint8_t           m_weather;              	// Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                            	// 3 = light rain, 4 = heavy rain, 5 = storm
    int8_t	    m_trackTemperature;    	// Track temp. in degrees celsius
    int8_t	    m_airTemperature;      	// Air temp. in degrees celsius
    uint8_t           m_totalLaps;           	// Total number of laps in this race
    uint16_t          m_trackLength;           	// Track length in metres
    uint8_t           m_sessionType;         	// 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P
                                            	// 5 = Q1, 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ
                                            	// 10 = R, 11 = R2, 12 = Time Trial
    int8_t            m_trackId;         		// -1 for unknown, 0-21 for tracks, see appendix
    uint8_t           m_era;                  	// Era, 0 = modern, 1 = classic
    uint16_t          m_sessionTimeLeft;    	// Time left in session in seconds
    uint16_t          m_sessionDuration;     	// Session duration in seconds
    uint8_t           m_pitSpeedLimit;      	// Pit speed limit in kilometres per hour
    uint8_t           m_gamePaused;               // Whether the game is paused
    uint8_t           m_isSpectating;        	// Whether the player is spectating
    uint8_t           m_spectatorCarIndex;  	// Index of the car being spectated
    uint8_t           m_sliProNativeSupport;	// SLI Pro support, 0 = inactive, 1 = active
    uint8_t           m_numMarshalZones;         	// Number of marshal zones to follow
    struct MarshalZone     m_marshalZones[21];         // List of marshal zones – max 21
    uint8_t           m_safetyCarStatus;          // 0 = no safety car, 1 = full safety car
                                                // 2 = virtual safety car
    uint8_t          m_networkGame;              // 0 = offline, 1 = online
}__attribute__((packed));

// LAP DATA PACKET:
// The lap data packet gives details of all the cars in the session.
// Frequency: Rate as specified in menus
// Size: 841 bytes
struct LapData {
    float       m_lastLapTime;           // Last lap time in seconds
    float       m_currentLapTime;        // Current time around the lap in seconds
    float       m_bestLapTime;           // Best lap time of the session in seconds
    float       m_sector1Time;           // Sector 1 time in seconds
    float       m_sector2Time;           // Sector 2 time in seconds
    float       m_lapDistance;           // Distance vehicle is around current lap in metres – could
                                         // be negative if line hasn’t been crossed yet
    float       m_totalDistance;         // Total distance travelled in session in metres – could
                                         // be negative if line hasn’t been crossed yet
    float       m_safetyCarDelta;        // Delta in seconds for safety car
    uint8_t       m_carPosition;           // Car race position
    uint8_t       m_currentLapNum;         // Current lap number
    uint8_t       m_pitStatus;             // 0 = none, 1 = pitting, 2 = in pit area
    uint8_t       m_sector;                // 0 = sector1, 1 = sector2, 2 = sector3
    uint8_t       m_currentLapInvalid;     // Current lap invalid - 0 = valid, 1 = invalid
    uint8_t       m_penalties;             // Accumulated time penalties in seconds to be added
    uint8_t       m_gridPosition;          // Grid position the vehicle started the race in
    uint8_t       m_driverStatus;          // Status of driver - 0 = in garage, 1 = flying lap
                                         // 2 = in lap, 3 = out lap, 4 = on track
    uint8_t       m_resultStatus;          // Result status - 0 = invalid, 1 = inactive, 2 = active
                                         // 3 = finished, 4 = disqualified, 5 = not classified
                                         // 6 = retired
}__attribute__((packed));
struct PacketLapData {
    struct PacketHeader    m_header;              // Header

    struct LapData         m_lapData[20];         // Lap data for all cars on track
}__attribute__((packed));

// EVENT PACKET:
// This packet gives details of events that happen during the course of the race.
// Frequency: When the event occurs
// Size: 25 bytes
struct PacketEventData {
    struct PacketHeader    m_header;               // Header

    uint8_t           m_eventStringCode[4];   // Event string code, see above
}__attribute__((packed));

// PARTICIPANTS PACKET:
// This is a list of participants in the race. If the vehicle is controlled by AI, then the name will be the driver name.
// If this is a multiplayer game, the names will be the Steam Id on PC, or the LAN name if appropriate.
// On Xbox One, the names will always be the driver name, on PS4 the name will be the LAN name if playing a LAN game, otherwise it will be the driver name.
// Frequency: Every 5 seconds
// Size: 1082 bytes
struct ParticipantData {
    uint8_t      m_aiControlled;           // Whether the vehicle is AI (1) or Human (0) controlled
    uint8_t      m_driverId;               // Driver id - see appendix
    uint8_t      m_teamId;                 // Team id - see appendix
    uint8_t      m_raceNumber;             // Race number of the car
    uint8_t      m_nationality;            // Nationality of the driver
    char       m_name[48];               // Name of participant in UTF-8 format – null terminated
                                         // Will be truncated with … (U+2026) if too long
}__attribute__((packed));
struct PacketParticipantsData {
    struct PacketHeader    m_header;            // Header

    uint8_t           m_numCars;           // Number of cars in the data
    struct ParticipantData m_participants[20];
}__attribute__((packed));

// CAR SETUPS PACKET:
// This packet details the car setups for each vehicle in the session.
// Note that in multiplayer games, other player cars will appear as blank, you will only be able to see your car setup and AI cars.
// Frequency: Every 5 seconds
// Size: 841 bytes
struct CarSetupData {
    uint8_t     m_frontWing;                // Front wing aero
    uint8_t     m_rearWing;                 // Rear wing aero
    uint8_t     m_onThrottle;               // Differential adjustment on throttle (percentage)
    uint8_t     m_offThrottle;              // Differential adjustment off throttle (percentage)
    float     m_frontCamber;              // Front camber angle (suspension geometry)
    float     m_rearCamber;               // Rear camber angle (suspension geometry)
    float     m_frontToe;                 // Front toe angle (suspension geometry)
    float     m_rearToe;                  // Rear toe angle (suspension geometry)
    uint8_t     m_frontSuspension;          // Front suspension
    uint8_t     m_rearSuspension;           // Rear suspension
    uint8_t     m_frontAntiRollBar;         // Front anti-roll bar
    uint8_t     m_rearAntiRollBar;          // Front anti-roll bar
    uint8_t     m_frontSuspensionHeight;    // Front ride height
    uint8_t     m_rearSuspensionHeight;     // Rear ride height
    uint8_t     m_brakePressure;            // Brake pressure (percentage)
    uint8_t     m_brakeBias;                // Brake bias (percentage)
    float     m_frontTyrePressure;        // Front tyre pressure (PSI)
    float     m_rearTyrePressure;         // Rear tyre pressure (PSI)
    uint8_t     m_ballast;                  // Ballast
    float     m_fuelLoad;                 // Fuel load
}__attribute__((packed));
struct PacketCarSetupData {
    struct PacketHeader    m_header;            // Header

    struct CarSetupData    m_carSetups[20];
}__attribute__((packed));

// CAR TELEMETRY PACKET:
// This packet details telemetry for all the cars in the race.
// It details various values that would be recorded on the car such as speed, throttle application, DRS etc.
// Frequency: Rate as specified in menus
// Size: 1085 bytes
struct CarTelemetryData {
    uint16_t    m_speed;                      // Speed of car in kilometres per hour
    uint8_t     m_throttle;                   // Amount of throttle applied (0 to 100)
    int8_t      m_steer;                      // Steering (-100 (full lock left) to 100 (full lock right))
    uint8_t     m_brake;                      // Amount of brake applied (0 to 100)
    uint8_t     m_clutch;                     // Amount of clutch applied (0 to 100)
    int8_t      m_gear;                       // Gear selected (1-8, N=0, R=-1)
    uint16_t    m_engineRPM;                  // Engine RPM
    uint8_t     m_drs;                        // 0 = off, 1 = on
    uint8_t     m_revLightsPercent;           // Rev lights indicator (percentage)
    uint16_t    m_brakesTemperature[4];       // Brakes temperature (celsius)
    uint16_t    m_tyresSurfaceTemperature[4]; // Tyres surface temperature (celsius)
    uint16_t    m_tyresInnerTemperature[4];   // Tyres inner temperature (celsius)
    uint16_t    m_engineTemperature;          // Engine temperature (celsius)
    float     m_tyresPressure[4];           // Tyres pressure (PSI)
}__attribute__((packed));
struct PacketCarTelemetryData {
    struct PacketHeader        m_header;                // Header

    struct CarTelemetryData    m_carTelemetryData[20];

    uint32_t              m_buttonStatus;         // Bit flags specifying which buttons are being
                                                // pressed currently - see appendices
}__attribute__((packed));

// CAR STATUS PACKET:
// This packet details car statuses for all the cars in the race. It includes values such as the damage readings on the car.
// Frequency: 2 per second
// Size: 1061 bytes
struct CarStatusData {
    uint8_t       m_tractionControl;          // 0 (off) - 2 (high)
    uint8_t       m_antiLockBrakes;           // 0 (off) - 1 (on)
    uint8_t       m_fuelMix;                  // Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    uint8_t       m_frontBrakeBias;           // Front brake bias (percentage)
    uint8_t       m_pitLimiterStatus;         // Pit limiter status - 0 = off, 1 = on
    float       m_fuelInTank;               // Current fuel mass
    float       m_fuelCapacity;             // Fuel capacity
    uint16_t      m_maxRPM;                   // Cars max RPM, point of rev limiter
    uint16_t      m_idleRPM;                  // Cars idle RPM
    uint8_t       m_maxGears;                 // Maximum number of gears
    uint8_t       m_drsAllowed;               // 0 = not allowed, 1 = allowed, -1 = unknown
    uint8_t       m_tyresWear[4];             // Tyre wear percentage
    uint8_t       m_tyreCompound;             // Modern - 0 = hyper soft, 1 = ultra soft
                                            // 2 = super soft, 3 = soft, 4 = medium, 5 = hard
                                            // 6 = super hard, 7 = inter, 8 = wet
                                            // Classic - 0-6 = dry, 7-8 = wet
    uint8_t       m_tyresDamage[4];           // Tyre damage (percentage)
    uint8_t       m_frontLeftWingDamage;      // Front left wing damage (percentage)
    uint8_t       m_frontRightWingDamage;     // Front right wing damage (percentage)
    uint8_t       m_rearWingDamage;           // Rear wing damage (percentage)
    uint8_t       m_engineDamage;             // Engine damage (percentage)
    uint8_t       m_gearBoxDamage;            // Gear box damage (percentage)
    uint8_t       m_exhaustDamage;            // Exhaust damage (percentage)
    int8_t        m_vehicleFiaFlags;          // -1 = invalid/unknown, 0 = none, 1 = green
                                            // 2 = blue, 3 = yellow, 4 = red
    float       m_ersStoreEnergy;           // ERS energy store in Joules
    uint8_t       m_ersDeployMode;            // ERS deployment mode, 0 = none, 1 = low, 2 = medium
                                            // 3 = high, 4 = overtake, 5 = hotlap
    float       m_ersHarvestedThisLapMGUK;  // ERS energy harvested this lap by MGU-K
    float       m_ersHarvestedThisLapMGUH;  // ERS energy harvested this lap by MGU-H
    float       m_ersDeployedThisLap;       // ERS energy deployed this lap
}__attribute__((packed));
struct PacketCarStatusData {
    struct PacketHeader        m_header;            // Header

    struct CarStatusData       m_carStatusData[20];
}__attribute__((packed));
