import Tkinter
# from Tkinter import *
from Tkinter import Label
from Tkinter import Frame
from Tkinter import W
from Tkinter import Button
# from Tkinter import QUIT
import time
import threading
import random
import Queue
import socket
import ctypes
import sys
import binascii
import structs
# from __future__ import print_function
from pprint import pprint
# import f1_udp_client_test

class GuiPart(Frame):
    def __init__(self, master, queue, endCommand):
        Frame.__init__(self)
        self.configure(background='grey')
        self.queue = queue

        # Set up the GUI
        console = Tkinter.Button(master, text='Done', command=endCommand)
        console.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # Show data from UDP stream
        # Set lables for the different packets
        self.motion_data_title = Label(self, text = "MOTION DATA", anchor=W).grid(row=4, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.session_data_title = Label(self, text = "SESSION DATA", anchor=W).grid(row=4, column=2, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.lap_data_title = Label(self, text = "LAP DATA", anchor=W).grid(row=4, column=4, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.event_data_title = Label(self, text = "EVENT DATA", anchor=W).grid(row=4, column=6, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.participant_data_title = Label(self, text = "PARTICIPANT DATA", anchor=W).grid(row=4, column=8, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.car_setup_data_title = Label(self, text = "CAR SETUP DATA", anchor=W).grid(row=4, column=10, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.car_telemetry_data_title = Label(self, text = "CAR TELEMETRY DATA", anchor=W).grid(row=4, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)
        self.packet_car_status_data_title = Label(self, text = "PACKET CAR STATUS DATA", anchor=W).grid(row=4, column=14, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, columnspan=2)



        # Set lables for each of the packets datas
        # Motion data
        self.md_world_position_x = Label(self, text = "worldPositionX", background='grey').grid(row=6, column=0, sticky=W)
        self.md_world_position_y = Label(self, text = "worldPositionY", background='grey').grid(row=7, column=0, sticky=W)
        self.md_world_position_z = Label(self, text = "worldPositionZ", background='grey').grid(row=8, column=0, sticky=W)
        self.md_world_velocity_x = Label(self, text = "worldVelocityX", background='grey').grid(row=9, column=0, sticky=W)
        self.md_world_velocity_y = Label(self, text = "worldVelocityY", background='grey').grid(row=10, column=0, sticky=W)
        self.md_world_velocity_z = Label(self, text = "worldVelocityZ", background='grey').grid(row=11, column=0, sticky=W)
        self.md_world_forward_dir_x = Label(self, text = "worldForwardDirX", background='grey').grid(row=12, column=0, sticky=W)
        self.md_world_forward_dir_y = Label(self, text = "worldForwardDirY", background='grey').grid(row=13, column=0, sticky=W)
        self.md_world_forward_dir_z = Label(self, text = "worldForwardDirZ", background='grey').grid(row=14, column=0, sticky=W)
        self.md_world_right_dir_x = Label(self, text = "worldRightDirX", background='grey').grid(row=15, column=0, sticky=W)
        self.md_world_right_dir_y = Label(self, text = "worldRightDirY", background='grey').grid(row=16, column=0, sticky=W)
        self.md_world_right_dir_z = Label(self, text = "worldRightDirZ", background='grey').grid(row=17, column=0, sticky=W)
        self.md_g_force_lateral = Label(self, text = "gForceLateral", background='grey').grid(row=18, column=0, sticky=W)
        self.md_g_force_longitudinal = Label(self, text = "gForceLongitudinal", background='grey').grid(row=19, column=0, sticky=W)
        self.md_g_force_vertical = Label(self, text = "gForceVertical", background='grey').grid(row=20, column=0, sticky=W)
        self.md_yaw = Label(self, text = "yaw", background='grey').grid(row=21, column=0, sticky=W)
        self.md_pitch = Label(self, text = "pitch", background='grey').grid(row=22, column=0, sticky=W)
        self.md_roll = Label(self, text = "roll", background='grey').grid(row=23, column=0, sticky=W)
        self.md_suspension_position_rl = Label(self, text = "suspension_positions [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=24, column=0, sticky=W, columnspan=2)                   # All wheel arrays have the following order RL, RR, FL, FR
        # self.md_suspension_position_rr = Label(self, text = "suspension_position_rr").grid(row=25, column=0, sticky=W)
        # self.md_suspension_position_fl = Label(self, text = "suspension_position_fl").grid(row=26, column=0, sticky=W)
        # self.md_suspension_position_fr = Label(self, text = "suspension_position_fr").grid(row=27, column=0, sticky=W)
        self.md_suspension_velocity_rl = Label(self, text = "suspension_velocity  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=27, column=0, sticky=W, columnspan=2)
        # self.md_suspension_velocity_rr = Label(self, text = "suspension_velocity_rr").grid(row=29, column=0, sticky=W)
        # self.md_suspension_velocity_fl = Label(self, text = "suspension_velocity_fl").grid(row=30, column=0, sticky=W)
        # self.md_suspension_velocity_fr = Label(self, text = "suspension_velocity_fr").grid(row=31, column=0, sticky=W)
        self.md_suspension_acceleration_rl = Label(self, text = "suspension_acceleration  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=30, column=0, sticky=W, columnspan=2)
        # self.md_suspension_acceleration_rr = Label(self, text = "suspension_acceleration_rr").grid(row=33, column=0, sticky=W)
        # self.md_suspension_acceleration_fl = Label(self, text = "suspension_acceleration_fl").grid(row=34, column=0, sticky=W)
        # self.md_suspension_acceleration_fr = Label(self, text = "suspension_acceleration_fr").grid(row=35, column=0, sticky=W)
        self.md_wheel_speed_rl = Label(self, text = "wheel_speed  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=33, column=0, sticky=W, columnspan=2)
        # self.md_wheel_speed_rr = Label(self, text = "wheel_speed_rr").grid(row=37, column=0, sticky=W)
        # self.md_wheel_speed_fl = Label(self, text = "wheel_speed_fl").grid(row=38, column=0, sticky=W)
        # self.md_wheel_speed_fr = Label(self, text = "wheel_speed_fr").grid(row=39, column=0, sticky=W)
        self.md_wheel_slip_rl = Label(self, text = "wheel_slip  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=36, column=0, sticky=W, columnspan=2)
        # self.md_wheel_slip_rr = Label(self, text = "wheel_slip_rr").grid(row=41, column=0, sticky=W)
        # self.md_wheel_slip_fl = Label(self, text = "wheel_slip_fl").grid(row=42, column=0, sticky=W)
        # self.md_wheel_slip_fr = Label(self, text = "wheel_slip_fr").grid(row=43, column=0, sticky=W)
        self.md_local_velocityX = Label(self, text = "localVelocityX", background='grey').grid(row=39, column=0, sticky=W)
        self.md_local_velocityY = Label(self, text = "localVelocityY", background='grey').grid(row=40, column=0, sticky=W)
        self.md_local_velocityZ = Label(self, text = "localVelocityZ", background='grey').grid(row=41, column=0, sticky=W)
        self.md_angular_velocityX = Label(self, text = "angularVelocityX", background='grey').grid(row=42, column=0, sticky=W)
        self.md_angular_velocityY = Label(self, text = "angularVelocityY", background='grey').grid(row=43, column=0, sticky=W)
        self.md_angular_velocityZ = Label(self, text = "angularVelocityZ", background='grey').grid(row=44, column=0, sticky=W)
        self.md_angular_accelerationX = Label(self, text = "angularAccelerationX", background='grey').grid(row=45, column=0, sticky=W)
        self.md_angular_accelerationY = Label(self, text = "angularAccelerationY", background='grey').grid(row=46, column=0, sticky=W)
        self.md_angular_accelerationZ = Label(self, text = "angularAccelerationZ", background='grey').grid(row=47, column=0, sticky=W)
        self.md_front_wheels_angle = Label(self, text = "frontWheelsAngle", background='grey').grid(row=48, column=0, sticky=W)



        # Session data

        self.sd_weather = Label(self, text = "weather", background='grey').grid(row=6, column=2, sticky=W)
        self.sd_trackTemperature = Label(self, text = "trackTemperature", background='grey').grid(row=7, column=2, sticky=W)
        self.sd_airTemperature = Label(self, text = "airTemperature", background='grey').grid(row=8, column=2, sticky=W)
        self.sd_totalLaps = Label(self, text = "totalLaps", background='grey').grid(row=9, column=2, sticky=W)
        self.sd_trackLength = Label(self, text = "trackLength", background='grey').grid(row=10, column=2, sticky=W)
        self.sd_sessionType = Label(self, text = "sessionType", background='grey').grid(row=11, column=2, sticky=W)
        self.sd_trackId = Label(self, text = "trackId", background='grey').grid(row=12, column=2, sticky=W)
        self.sd_era = Label(self, text = "era", background='grey').grid(row=13, column=2, sticky=W)
        self.sd_sessionTimeLeft = Label(self, text = "sessionTimeLeft", background='grey').grid(row=14, column=2, sticky=W)
        self.sd_sessionDuration = Label(self, text = "sessionDuration", background='grey').grid(row=15, column=2, sticky=W)
        self.sd_pitSpeedLimit = Label(self, text = "pitSpeedLimit", background='grey').grid(row=16, column=2, sticky=W)
        self.sd_gamePaused = Label(self, text = "gamePaused", background='grey').grid(row=17, column=2, sticky=W)
        self.sd_isSpectating = Label(self, text = "isSpectating", background='grey').grid(row=18, column=2, sticky=W)
        self.sd_spectatorCarIndex = Label(self, text = "spectatorCarIndex", background='grey').grid(row=19, column=2, sticky=W)
        self.sd_sliProNativeSupport = Label(self, text = "sliProNativeSuppor", background='grey').grid(row=20, column=2, sticky=W)
        self.sd_numMarshalZones = Label(self, text = "numMarshalZones", background='grey').grid(row=21, column=2, sticky=W)
        self.sd_marshalZones = Label(self, text = "marshalZones", background='grey').grid(row=22, column=2, sticky=W)
        self.sd_safetyCarStatus = Label(self, text = "safetyCarStatus", background='grey').grid(row=23, column=2, sticky=W)
        self.sd_networkGame = Label(self, text = "networkGame", background='grey').grid(row=24, column=2, sticky=W)

        # Lap data
        # self.ld_lapData = Label(self, text = "lapData", background='grey').grid(row=6, column=4, sticky=W)
        self.ld_lastLapTime = Label(self, text = "lastLapTime", background='grey').grid(row=6, column=4, sticky=W)
        self.ld_currentLapTime = Label(self, text = "currentLapTime", background='grey').grid(row=7, column=4, sticky=W)
        self.ld_bestLapTime = Label(self, text = "bestLapTime", background='grey').grid(row=8, column=4, sticky=W)
        self.ld_sector1Time = Label(self, text = "sector1Time", background='grey').grid(row=9, column=4, sticky=W)
        self.ld_sector2Time = Label(self, text = "sector2Time", background='grey').grid(row=10, column=4, sticky=W)
        self.ld_lapDistance = Label(self, text = "lapDistance", background='grey').grid(row=11, column=4, sticky=W)
        self.ld_totalDistance = Label(self, text = "totalDistance", background='grey').grid(row=12, column=4, sticky=W)
        self.ld_safetyCarDelta = Label(self, text = "safetyCarDelta", background='grey').grid(row=13, column=4, sticky=W)
        self.ld_carPosition = Label(self, text = "carPosition", background='grey').grid(row=14, column=4, sticky=W)
        self.ld_currentLapNum = Label(self, text = "currentLapNum", background='grey').grid(row=15, column=4, sticky=W)
        self.ld_pitStatus = Label(self, text = "pitStatus", background='grey').grid(row=16, column=4, sticky=W)
        self.ld_sector = Label(self, text = "sector", background='grey').grid(row=17, column=4, sticky=W)
        self.ld_currentLapInvalid = Label(self, text = "currentLapInvalid", background='grey').grid(row=18, column=4, sticky=W)
        self.ld_penalties = Label(self, text = "penalties", background='grey').grid(row=19, column=4, sticky=W)
        self.ld_gridPosition = Label(self, text = "gridPosition", background='grey').grid(row=20, column=4, sticky=W)
        self.ld_driverStatus = Label(self, text = "driverStatus", background='grey').grid(row=21, column=4, sticky=W)
        self.ld_resultStatus = Label(self, text = "resultStatus", background='grey').grid(row=22, column=4, sticky=W)

        # Event data
        self.ed_eventStringCode = Label(self, text = "eventStringCode", background='grey').grid(row=6, column=6, sticky=W)


        # Partcipant data
        self.pd_numCars = Label(self, text = "numCars", background='grey').grid(row=6, column=8, sticky=W)
        self.pd_aiControlled = Label(self, text = "aiControlled", background='grey').grid(row=7, column=8, sticky=W)
        self.pd_driverId = Label(self, text = "driverId", background='grey').grid(row=8, column=8, sticky=W)
        self.pd_teamId = Label(self, text = "teamId", background='grey').grid(row=9, column=8, sticky=W)
        self.pd_raceNumber = Label(self, text = "raceNumber", background='grey').grid(row=10, column=8, sticky=W)
        self.pd_nationality = Label(self, text = "nationality", background='grey').grid(row=11, column=8, sticky=W)
        self.pd_name = Label(self, text = "name", background='grey').grid(row=12, column=8, sticky=W)


        # Car Setup Data
        self.csd_frontWing = Label(self, text = "frontWing", background='grey').grid(row=6, column=10, sticky=W)
        self.csd_rearWing = Label(self, text = "rearWing", background='grey').grid(row=7, column=10, sticky=W)
        self.csd_onThrottle = Label(self, text = "onThrottle", background='grey').grid(row=8, column=10, sticky=W)
        self.csd_offThrottle = Label(self, text = "offThrottle", background='grey').grid(row=9, column=10, sticky=W)
        self.csd_frontCamber = Label(self, text = "frontCamber", background='grey').grid(row=10, column=10, sticky=W)
        self.csd_rearCamber = Label(self, text = "rearCamber", background='grey').grid(row=11, column=10, sticky=W)
        self.csd_frontToe = Label(self, text = "frontToe", background='grey').grid(row=12, column=10, sticky=W)
        self.csd_rearToe = Label(self, text = "rearToe", background='grey').grid(row=13, column=10, sticky=W)
        self.csd_frontSuspension = Label(self, text = "frontSuspension", background='grey').grid(row=14, column=10, sticky=W)
        self.csd_rearSuspension = Label(self, text = "rearSuspension", background='grey').grid(row=15, column=10, sticky=W)
        self.csd_frontAntiRollBar = Label(self, text = "frontAntiRollBar", background='grey').grid(row=16, column=10, sticky=W)
        self.csd_rearAntiRollBar = Label(self, text = "rearAntiRollBar", background='grey').grid(row=17, column=10, sticky=W)
        self.csd_frontSuspensionHeight = Label(self, text = "frontSuspensionHeight", background='grey').grid(row=18, column=10, sticky=W)
        self.csd_rearSuspensionHeight = Label(self, text = "rearSuspensionHeight", background='grey').grid(row=19, column=10, sticky=W)
        self.csd_brakePressure = Label(self, text = "brakePressure", background='grey').grid(row=20, column=10, sticky=W)
        self.csd_brakeBias = Label(self, text = "brakeBias", background='grey').grid(row=21, column=10, sticky=W)
        self.csd_frontTyrePressure = Label(self, text = "frontTyrePressure", background='grey').grid(row=22, column=10, sticky=W)
        self.csd_rearTyrePressure = Label(self, text = "rearTyrePressure", background='grey').grid(row=23, column=10, sticky=W)
        self.csd_ballast = Label(self, text = "ballast", background='grey').grid(row=24, column=10, sticky=W)
        self.csd_fuelLoad = Label(self, text = "fuelLoad", background='grey').grid(row=25, column=10, sticky=W)


        # Car Telemetry Data
        self.ctd_speed = Label(self, text = "speed", background='grey').grid(row=6, column=12, sticky=W)
        self.ctd_throttle = Label(self, text = "throttle", background='grey').grid(row=7, column=12, sticky=W)
        self.ctd_steer = Label(self, text = "steer", background='grey').grid(row=8, column=12, sticky=W)
        self.ctd_brake = Label(self, text = "brake", background='grey').grid(row=9, column=12, sticky=W)
        self.ctd_clutch = Label(self, text = "clutch", background='grey').grid(row=10, column=12, sticky=W)
        self.ctd_gear = Label(self, text = "gear", background='grey').grid(row=11, column=12, sticky=W)
        self.ctd_engineRPM = Label(self, text = "engineRPM", background='grey').grid(row=12, column=12, sticky=W)
        self.ctd_drs = Label(self, text = "drs", background='grey').grid(row=13, column=12, sticky=W)
        self.ctd_revLightsPercent = Label(self, text = "revLightsPercent", background='grey').grid(row=14, column=12, sticky=W)
        self.ctd_brakesTemperature_rl = Label(self, text = "brakesTemperature  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=15, column=12, sticky=W, columnspan=2)
        # self.ctd_brakesTemperature_rr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_brakesTemperature_fl = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_brakesTemperature_fr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        self.ctd_tyresSurfaceTemperature_rl = Label(self, text = "tyresSurfaceTemperature  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=18, column=12, sticky=W, columnspan=2)
        # self.ctd_tyresSurfaceTemperature_rr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresSurfaceTemperature_fl = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresSurfaceTemperature_fr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        self.ctd_tyresInnerTemperature_rl = Label(self, text = "tyresInnerTemperature  [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=21, column=12, sticky=W, columnspan=2)
        # self.ctd_tyresInnerTemperature_rr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresInnerTemperature_fl = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresInnerTemperature_fr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        self.ctd_engineTemperature = Label(self, text = "engineTemperature", background='grey').grid(row=24, column=12, sticky=W)
        self.ctd_tyresPressure_rl = Label(self, text = "tyresPressure [rl]  [rr]    [fl]    [fr]", background='grey').grid(row=25, column=12, sticky=W, columnspan=2)
        # self.ctd_tyresPressure_rr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresPressure_fl = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        # self.ctd_tyresPressure_fr = Label(self, text = "", background='grey').grid(row=6, column=12, sticky=W)
        self.ctd_buttonStatus = Label(self, text = "buttonStatus", background='grey').grid(row=28, column=12, sticky=W)

        # Packet Car Status Data












        # Data for each of the packets

        # Motion data
        self.md_world_position_x_data_label = Label(self, textvariable = md_world_position_x_data, anchor=W).grid(row=6, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_position_y_data_label = Label(self, textvariable = md_world_position_y_data, anchor=W).grid(row=7, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_position_z_data_label = Label(self, textvariable = md_world_position_z_data, anchor=W).grid(row=8, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_velocity_x_data_label = Label(self, textvariable = md_world_velocity_x_data, anchor=W).grid(row=9, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_velocity_y_data_label = Label(self, textvariable = md_world_velocity_y_data, anchor=W).grid(row=10, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_velocity_z_data_label = Label(self, textvariable = md_world_velocity_z_data, anchor=W).grid(row=11, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_forward_dir_x_data_label = Label(self, textvariable = md_world_forward_dir_x_data, anchor=W).grid(row=12, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_forward_dir_y_data_label = Label(self, textvariable = md_world_forward_dir_y_data, anchor=W).grid(row=13, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_forward_dir_z_data_label = Label(self, textvariable = md_world_forward_dir_z_data, anchor=W).grid(row=14, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_right_dir_x_data_label = Label(self, textvariable = md_world_right_dir_x_data, anchor=W).grid(row=15, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_right_dir_y_data_label = Label(self, textvariable = md_world_right_dir_y_data, anchor=W).grid(row=16, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_world_right_dir_z_data_label = Label(self, textvariable = md_world_right_dir_z_data, anchor=W).grid(row=17, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_g_force_lateral_data_label = Label(self, textvariable = md_g_force_lateral_data, anchor=W).grid(row=18, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_g_force_longitudinal_data_label = Label(self, textvariable = md_g_force_longitudinal_data, anchor=W).grid(row=19, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_g_force_vertical_data_label = Label(self, textvariable = md_g_force_vertical_data, anchor=W).grid(row=20, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_yaw_data_label = Label(self, textvariable = md_yaw_data, anchor=W).grid(row=21, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_pitch_data_label = Label(self, textvariable = md_pitch_data, anchor=W).grid(row=22, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_roll_data_label = Label(self, textvariable = md_roll_data, anchor=W).grid(row=23, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_position_rl_data_label = Label(self, textvariable = md_suspension_position_rl_data, anchor=W).grid(row=25, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)                   # All wheel arrays have the following order RL, RR, FL, FR
        self.md_suspension_position_rr_data_label = Label(self, textvariable = md_suspension_position_rr_data, anchor=W).grid(row=25, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_position_fl_data_label = Label(self, textvariable = md_suspension_position_fl_data, anchor=W).grid(row=26, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_position_fr_data_label = Label(self, textvariable = md_suspension_position_fr_data, anchor=W).grid(row=26, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_velocity_rl_data_label = Label(self, textvariable = md_suspension_velocity_rl_data, anchor=W).grid(row=28, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_velocity_rr_data_label = Label(self, textvariable = md_suspension_velocity_rr_data, anchor=W).grid(row=28, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_velocity_fl_data_label = Label(self, textvariable = md_suspension_velocity_fl_data, anchor=W).grid(row=29, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_velocity_fr_data_label = Label(self, textvariable = md_suspension_velocity_fr_data, anchor=W).grid(row=29, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_acceleration_rl_data_label = Label(self, textvariable = md_suspension_acceleration_rl_data, anchor=W).grid(row=31, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_acceleration_rr_data_label = Label(self, textvariable = md_suspension_acceleration_rr_data, anchor=W).grid(row=31, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_acceleration_fl_data_label = Label(self, textvariable = md_suspension_acceleration_fl_data, anchor=W).grid(row=32, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_suspension_acceleration_fr_data_label = Label(self, textvariable = md_suspension_acceleration_fr_data, anchor=W).grid(row=32, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_speed_rl_data_label = Label(self, textvariable = md_wheel_speed_rl_data, anchor=W).grid(row=34, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_speed_rr_data_label = Label(self, textvariable = md_wheel_speed_rr_data, anchor=W).grid(row=34, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_speed_fl_data_label = Label(self, textvariable = md_wheel_speed_fl_data, anchor=W).grid(row=35, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_speed_fr_data_label = Label(self, textvariable = md_wheel_speed_fr_data, anchor=W).grid(row=35, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_slip_rl_data_label = Label(self, textvariable = md_wheel_slip_rl_data, anchor=W).grid(row=37, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_slip_rr_data_label = Label(self, textvariable = md_wheel_slip_rr_data, anchor=W).grid(row=37, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_slip_fl_data_label = Label(self, textvariable = md_wheel_slip_fl_data, anchor=W).grid(row=38, column=0, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_wheel_slip_fr_data_label = Label(self, textvariable = md_wheel_slip_fr_data, anchor=W).grid(row=38, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_local_velocityX_data_label = Label(self, textvariable = md_local_velocityX_data, anchor=W).grid(row=39, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_local_velocityY_data_label = Label(self, textvariable = md_local_velocityY_data, anchor=W).grid(row=40, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_local_velocityZ_data_label = Label(self, textvariable = md_local_velocityZ_data, anchor=W).grid(row=41, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_velocityX_data_label = Label(self, textvariable = md_angular_velocityX_data, anchor=W).grid(row=42, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_velocityY_data_label = Label(self, textvariable = md_angular_velocityY_data, anchor=W).grid(row=43, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_velocityZ_data_label = Label(self, textvariable = md_angular_velocityZ_data, anchor=W).grid(row=44, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_accelerationX_data_label = Label(self, textvariable = md_angular_accelerationX_data, anchor=W).grid(row=45, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_accelerationY_data_label = Label(self, textvariable = md_angular_accelerationY_data, anchor=W).grid(row=46, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_angular_accelerationZ_data_label = Label(self, textvariable = md_angular_accelerationZ_data, anchor=W).grid(row=47, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)
        self.md_front_wheels_angle_data_label = Label(self, textvariable = md_front_wheels_angle_data, anchor=W).grid(row=48, column=1, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W, padx=5)


        # session DATA
        self.sd_weather_data_label = Label(self, textvariable = sd_weather_data, anchor=W).grid(row=6, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_trackTemperature_data_label = Label(self, textvariable = sd_trackTemperature_data, anchor=W).grid(row=7, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_airTemperature_data_label = Label(self, textvariable = sd_airTemperature_data, anchor=W).grid(row=8, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_totalLaps_data_label = Label(self, textvariable = sd_totalLaps_data, anchor=W).grid(row=9, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_trackLength_data_label = Label(self, textvariable = sd_trackLength_data, anchor=W).grid(row=10, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_sessionType_data_label = Label(self, textvariable = sd_sessionType_data, anchor=W).grid(row=11, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_trackId_data_label = Label(self, textvariable = sd_trackId_data, anchor=W).grid(row=12, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_era_data_label = Label(self, textvariable = sd_era_data, anchor=W).grid(row=13, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_sessionTimeLeft_data_label = Label(self, textvariable = sd_sessionTimeLeft_data, anchor=W).grid(row=14, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_sessionDuration_data_label = Label(self, textvariable = sd_sessionDuration_data, anchor=W).grid(row=15, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_pitSpeedLimit_data_label = Label(self, textvariable = sd_pitSpeedLimit_data, anchor=W).grid(row=16, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_gamePaused_data_label = Label(self, textvariable = sd_gamePaused_data, anchor=W).grid(row=17, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_isSpectating_data_label = Label(self, textvariable = sd_isSpectating_data, anchor=W).grid(row=18, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_spectatorCarIndex_data_label = Label(self, textvariable = sd_spectatorCarIndex_data, anchor=W).grid(row=19, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_sliProNativeSupport_data_label = Label(self, textvariable = sd_sliProNativeSupport_data, anchor=W).grid(row=20, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_numMarshalZones_data_label = Label(self, textvariable = sd_numMarshalZones_data, anchor=W).grid(row=21, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_marshalZones_data_label = Label(self, textvariable = sd_marshalZones_data, anchor=W).grid(row=22, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_safetyCarStatus_data_label = Label(self, textvariable = sd_safetyCarStatus_data, anchor=W).grid(row=23, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.sd_networkGame_data_label = Label(self, textvariable = sd_networkGame_data, anchor=W).grid(row=24, column=3, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)


        # Lap data
        # self.ld_lapData_data_label = Label(self, textvariable = ld_lapData_data, anchor=W).grid(row=6, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_lastLapTime_data_label = Label(self, textvariable = ld_lastLapTime_data, anchor=W).grid(row=6, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_currentLapTime_data_label = Label(self, textvariable = ld_currentLapTime_data, anchor=W).grid(row=7, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_bestLapTime_data_label = Label(self, textvariable = ld_bestLapTime_data, anchor=W).grid(row=8, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_sector1Time_data_label = Label(self, textvariable = ld_sector1Time_data, anchor=W).grid(row=9, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_sector2Time_data_label = Label(self, textvariable = ld_sector2Time_data, anchor=W).grid(row=10, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_lapDistance_data_label = Label(self, textvariable = ld_lapDistance_data, anchor=W).grid(row=11, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_totalDistance_data_label = Label(self, textvariable = ld_totalDistance_data, anchor=W).grid(row=12, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_safetyCarDelta_data_label = Label(self, textvariable = ld_safetyCarDelta_data, anchor=W).grid(row=13, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_carPosition_data_label = Label(self, textvariable = ld_carPosition_data, anchor=W).grid(row=14, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_currentLapNum_data_label = Label(self, textvariable = ld_currentLapNum_data, anchor=W).grid(row=15, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_pitStatus_data_label = Label(self, textvariable = ld_pitStatus_data, anchor=W).grid(row=16, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_sector_data_label = Label(self, textvariable = ld_sector_data, anchor=W).grid(row=17, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_currentLapInvalid_data_label = Label(self, textvariable = ld_currentLapInvalid_data, anchor=W).grid(row=18, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_penalties_data_label = Label(self, textvariable = ld_penalties_data, anchor=W).grid(row=19, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_gridPosition_data_label = Label(self, textvariable = ld_gridPosition_data, anchor=W).grid(row=20, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_driverStatus_data_label = Label(self, textvariable = ld_driverStatus_data, anchor=W).grid(row=21, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ld_resultStatus_data_label = Label(self, textvariable = ld_resultStatus_data, anchor=W).grid(row=22, column=5, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

        # Event data
        self.ed_eventStringCode_data_label = Label(self, textvariable = ed_eventStringCode_data, anchor=W).grid(row=6, column=7, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

        # Participant data
        self.pd_numCars_data_label = Label(self, textvariable = pd_numCars_data, anchor=W).grid(row=6, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_aiControlled_data_label = Label(self, textvariable = pd_aiControlled_data, anchor=W).grid(row=7, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_driverId_data_label = Label(self, textvariable = pd_driverId_data, anchor=W).grid(row=8, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_teamId_data_label = Label(self, textvariable = pd_teamId_data, anchor=W).grid(row=9, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_raceNumber_data_label = Label(self, textvariable = pd_raceNumber_data, anchor=W).grid(row=10, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_nationality_data_label = Label(self, textvariable = pd_nationality_data, anchor=W).grid(row=11, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.pd_name_data_label = Label(self, textvariable = pd_name_data, anchor=W).grid(row=12, column=9, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

        # Car Setup data
        self.csd_frontWing_data_label = Label(self, textvariable = csd_frontWing_data, anchor=W).grid(row=6, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearWing_data_label = Label(self, textvariable = csd_rearWing_data, anchor=W).grid(row=7, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_onThrottle_data_label = Label(self, textvariable = csd_onThrottle_data, anchor=W).grid(row=8, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_offThrottle_data_label = Label(self, textvariable = csd_offThrottle_data, anchor=W).grid(row=9, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontCamber_data_label = Label(self, textvariable = csd_frontCamber_data, anchor=W).grid(row=10, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearCamber_data_label = Label(self, textvariable = csd_rearCamber_data, anchor=W).grid(row=11, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontToe_data_label = Label(self, textvariable = csd_frontToe_data, anchor=W).grid(row=12, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearToe_data_label = Label(self, textvariable = csd_rearToe_data, anchor=W).grid(row=13, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontSuspension_data_label = Label(self, textvariable = csd_frontSuspension_data, anchor=W).grid(row=14, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearSuspension_data_label = Label(self, textvariable = csd_rearSuspension_data, anchor=W).grid(row=15, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontAntiRollBar_data_label = Label(self, textvariable = csd_frontAntiRollBar_data, anchor=W).grid(row=16, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearAntiRollBar_data_label = Label(self, textvariable = csd_rearAntiRollBar_data, anchor=W).grid(row=17, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontSuspensionHeight_data_label = Label(self, textvariable = csd_frontSuspensionHeight_data, anchor=W).grid(row=18, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearSuspensionHeight_data_label = Label(self, textvariable = csd_rearSuspensionHeight_data, anchor=W).grid(row=19, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_brakePressure_data_label = Label(self, textvariable = csd_brakePressure_data, anchor=W).grid(row=20, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_brakeBias_data_label = Label(self, textvariable = csd_brakeBias_data, anchor=W).grid(row=21, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_frontTyrePressure_data_label = Label(self, textvariable = csd_frontTyrePressure_data, anchor=W).grid(row=22, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_rearTyrePressure_data_label = Label(self, textvariable = csd_rearTyrePressure_data, anchor=W).grid(row=23, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_ballast_data_label = Label(self, textvariable = csd_ballast_data, anchor=W).grid(row=24, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.csd_fuelLoad_data_label = Label(self, textvariable = csd_fuelLoad_data, anchor=W).grid(row=25, column=11, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

        # Car Telemetry Data
        self.ctd_speed_data_label = Label(self, textvariable = ctd_speed_data, anchor=W).grid(row=6, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_throttle_data_label  = Label(self, textvariable = ctd_throttle_data, anchor=W).grid(row=7, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_steer_data_label  = Label(self, textvariable = ctd_steer_data, anchor=W).grid(row=8, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_brake_data_label  = Label(self, textvariable = ctd_brake_data, anchor=W).grid(row=9, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_clutch_data_label  = Label(self, textvariable = ctd_clutch_data, anchor=W).grid(row=10, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_gear_data_label  = Label(self, textvariable = ctd_gear_data, anchor=W).grid(row=11, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_engineRPM_data_label  = Label(self, textvariable = ctd_engineRPM_data, anchor=W).grid(row=12, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_drs_data_label  = Label(self, textvariable = ctd_drs_data, anchor=W).grid(row=13, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_revLightsPercent_data_label  = Label(self, textvariable = ctd_revLightsPercent_data, anchor=W).grid(row=14, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_brakesTemperature_rl_data_label  = Label(self, textvariable = ctd_brakesTemperature_rl_data, anchor=W).grid(row=16, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_brakesTemperature_rr_data_label  = Label(self, textvariable = ctd_brakesTemperature_rr_data, anchor=W).grid(row=16, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_brakesTemperature_fl_data_label  = Label(self, textvariable = ctd_brakesTemperature_fl_data, anchor=W).grid(row=17, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_brakesTemperature_fr_data_label  = Label(self, textvariable = ctd_brakesTemperature_fr_data, anchor=W).grid(row=17, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresSurfaceTemperature_rl_data_label  = Label(self, textvariable = ctd_tyresSurfaceTemperature_rl_data, anchor=W).grid(row=19, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresSurfaceTemperature_rr_data_label  = Label(self, textvariable = ctd_tyresSurfaceTemperature_rr_data, anchor=W).grid(row=19, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresSurfaceTemperature_fl_data_label  = Label(self, textvariable = ctd_tyresSurfaceTemperature_fl_data, anchor=W).grid(row=20, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresSurfaceTemperature_fr_data_label  = Label(self, textvariable = ctd_tyresSurfaceTemperature_fr_data, anchor=W).grid(row=20, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresInnerTemperature_rl_data_label  = Label(self, textvariable = ctd_tyresInnerTemperature_rl_data, anchor=W).grid(row=22, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresInnerTemperature_rr_data_label  = Label(self, textvariable = ctd_tyresInnerTemperature_rr_data, anchor=W).grid(row=22, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresInnerTemperature_fl_data_label  = Label(self, textvariable = ctd_tyresInnerTemperature_fl_data, anchor=W).grid(row=23, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresInnerTemperature_fr_data_label  = Label(self, textvariable = ctd_tyresInnerTemperature_fr_data, anchor=W).grid(row=23, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_engineTemperature_data_label  = Label(self, textvariable = ctd_engineTemperature_data, anchor=W).grid(row=24, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresPressure_rl_data_label  = Label(self, textvariable = ctd_tyresPressure_rl_data, anchor=W).grid(row=26, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresPressure_rr_data_label  = Label(self, textvariable = ctd_tyresPressure_rr_data, anchor=W).grid(row=26, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresPressure_fl_data_label  = Label(self, textvariable = ctd_tyresPressure_fl_data, anchor=W).grid(row=27, column=12, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_tyresPressure_fr_data_label  = Label(self, textvariable = ctd_tyresPressure_fr_data, anchor=W).grid(row=27, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)
        self.ctd_buttonStatus_data_label = Label(self, textvariable = ctd_buttonStatus_data, anchor=W).grid(row=28, column=13, sticky = Tkinter.N+Tkinter.S+Tkinter.E+Tkinter.W)

        # Add more GUI stuff here
        self.grid()
        # root.update()

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                packet = self.queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply print it
                # print msg

                # Check which packet we grab out of the queue and update GUI accordingly

                if packet[0] == "SessionData":
                    # print "found sd"
                    self.new_session_data(packet[1])
                    root.update()
                elif packet[0] == "MotionData":
                    # print "found md"
                    self.new_motion_data(packet[1])
                    root.update()
                elif packet[0] == "LapData":
                    # print "found sd"
                    self.new_lap_data(packet[1])
                    root.update()
                elif packet[0] == "EventData":
                    # print "found ed"
                    self.new_event_data(packet[1])
                    root.update()
                elif packet[0] == "ParticipantData":
                    # print "found pd"
                    self.new_participant_data(packet[1])
                    root.update()
                elif packet[0] == "CarSetupData":
                    # print "found csd"
                    self.new_car_setup_data(packet[1])
                    root.update()
                elif packet[0] == "CarTelemetryData":
                    # print "fount ctd"
                    self.new_car_telemetry_data(packet[1])
                    root.update


            except Queue.Empty:
                pass


    def new_motion_data(self, packet):
        global md_world_position_x_data
        global md_world_position_y_data
        global md_world_position_z_data
        global md_world_velocity_x_data
        global md_world_velocity_y_data
        global md_world_velocity_z_data
        global md_world_forward_dir_x_data
        global md_world_forward_dir_y_data
        global md_world_forward_dir_z_data
        global md_world_right_dir_x_data
        global md_world_right_dir_y_data
        global md_world_right_dir_z_data
        global md_g_force_lateral_data
        global md_g_force_longitudinal_data
        global md_g_force_vertical_data
        global md_yaw_data
        global md_pitch_data
        global md_roll_data
        global md_suspension_position_rl_data
        global md_suspension_position_rr_data
        global md_suspension_position_fl_data
        global md_suspension_position_fr_data
        global md_suspension_velocity_rl_data
        global md_suspension_velocity_rr_data
        global md_suspension_velocity_fl_data
        global md_suspension_velocity_fr_data
        global md_suspension_acceleration_rl_data
        global md_suspension_acceleration_rr_data
        global md_suspension_acceleration_fl_data
        global md_suspension_acceleration_fr_data
        global md_wheel_speed_rl_data
        global md_wheel_speed_rr_data
        global md_wheel_speed_fl_data
        global md_wheel_speed_fr_data
        global md_wheel_slip_rl_data
        global md_wheel_slip_rr_data
        global md_wheel_slip_fl_data
        global md_wheel_slip_fr_data
        global md_local_velocityX_data
        global md_local_velocityY_data
        global md_local_velocityZ_data
        global md_angular_velocityX_data
        global md_angular_velocityY_data
        global md_angular_velocityZ_data
        global md_angular_accelerationX_data
        global md_angular_accelerationY_data
        global md_angular_accelerationZ_data
        global md_front_wheels_angle_data



        md_world_position_x_data.set(str(packet.m_carMotionData[0].m_worldPositionX))
        md_world_position_y_data.set(str(packet.m_carMotionData[0].m_worldPositionY))
        md_world_position_z_data.set(str(packet.m_carMotionData[0].m_worldPositionZ))
        md_world_velocity_x_data.set(str(packet.m_carMotionData[0].m_worldVelocityX))
        md_world_velocity_y_data.set(str(packet.m_carMotionData[0].m_worldVelocityY))
        md_world_velocity_z_data.set(str(packet.m_carMotionData[0].m_worldVelocityZ))
        md_world_forward_dir_x_data.set(str(packet.m_carMotionData[0].m_worldForwardDirX))
        md_world_forward_dir_y_data.set(str(packet.m_carMotionData[0].m_worldForwardDirY))
        md_world_forward_dir_z_data.set(str(packet.m_carMotionData[0].m_worldForwardDirZ))
        md_world_right_dir_x_data.set(str(packet.m_carMotionData[0].m_worldRightDirX))
        md_world_right_dir_y_data.set(str(packet.m_carMotionData[0].m_worldRightDirY))
        md_world_right_dir_z_data.set(str(packet.m_carMotionData[0].m_worldRightDirZ))
        md_g_force_lateral_data.set(str(packet.m_carMotionData[0].m_gForceLateral))
        md_g_force_longitudinal_data.set(str(packet.m_carMotionData[0].m_gForceLongitudinal))
        md_g_force_vertical_data.set(str(packet.m_carMotionData[0].m_gForceVertical))
        md_yaw_data.set(str(packet.m_carMotionData[0].m_yaw))
        md_pitch_data.set(str(packet.m_carMotionData[0].m_pitch))
        md_roll_data.set(str(packet.m_carMotionData[0].m_roll))
        md_suspension_position_rl_data.set(str(packet.m_suspensionPosition[0]))
        md_suspension_position_rr_data.set(str(packet.m_suspensionPosition[1]))
        md_suspension_position_fl_data.set(str(packet.m_suspensionPosition[2]))
        md_suspension_position_fr_data.set(str(packet.m_suspensionPosition[3]))
        md_suspension_velocity_rl_data.set(str(packet.m_suspensionVelocity[0]))
        md_suspension_velocity_rr_data.set(str(packet.m_suspensionVelocity[1]))
        md_suspension_velocity_fl_data.set(str(packet.m_suspensionVelocity[2]))
        md_suspension_velocity_fr_data.set(str(packet.m_suspensionVelocity[3]))
        md_suspension_acceleration_rl_data.set(str(packet.m_suspensionAcceleration[0]))
        md_suspension_acceleration_rr_data.set(str(packet.m_suspensionAcceleration[1]))
        md_suspension_acceleration_fl_data.set(str(packet.m_suspensionAcceleration[2]))
        md_suspension_acceleration_fr_data.set(str(packet.m_suspensionAcceleration[3]))
        md_wheel_speed_rl_data.set(str(packet.m_wheelSpeed[0]))
        md_wheel_speed_rr_data.set(str(packet.m_wheelSpeed[1]))
        md_wheel_speed_fl_data.set(str(packet.m_wheelSpeed[2]))
        md_wheel_speed_fr_data.set(str(packet.m_wheelSpeed[3]))
        md_wheel_slip_rl_data.set(str(packet.m_wheelSlip[0]))
        md_wheel_slip_rr_data.set(str(packet.m_wheelSlip[1]))
        md_wheel_slip_fl_data.set(str(packet.m_wheelSlip[2]))
        md_wheel_slip_fr_data.set(str(packet.m_wheelSlip[3]))
        md_local_velocityX_data.set(str(packet.m_localVelocityX))
        md_local_velocityY_data.set(str(packet.m_localVelocityY))
        md_local_velocityZ_data.set(str(packet.m_localVelocityZ))
        md_angular_velocityX_data.set(str(packet.m_angularVelocityX))
        md_angular_velocityY_data.set(str(packet.m_angularVelocityY))
        md_angular_velocityZ_data.set(str(packet.m_angularVelocityZ))
        md_angular_accelerationX_data.set(str(packet.m_angularAccelerationX))
        md_angular_accelerationY_data.set(str(packet.m_angularAccelerationY))
        md_angular_accelerationZ_data.set(str(packet.m_angularAccelerationZ))
        md_front_wheels_angle_data.set(str(packet.m_frontWheelsAngle))

    def new_session_data(self, packet):
        global sd_weather_data
        global sd_trackTemperature_data
        global sd_airTemperature_data
        global sd_totalLaps_data
        global sd_trackLength_data
        global sd_sessionType_data
        global sd_trackId_data
        global sd_era_data
        global sd_sessionTimeLeft_data
        global sd_sessionDuration_data
        global sd_pitSpeedLimit_data
        global sd_gamePaused_data
        global sd_isSpectating_data
        global sd_spectatorCarIndex_data
        global sd_sliProNativeSupport_data
        global sd_numMarshalZones_data
        global sd_marshalZones_data
        global sd_safetyCarStatus_data
        global sd_networkGame_data

        sd_weather_data.set(str(packet.m_weather))
        sd_trackTemperature_data.set(str(packet.m_trackTemperature))
        sd_airTemperature_data.set(str(packet.m_airTemperature))
        sd_totalLaps_data.set(str(packet.m_totalLaps))
        sd_trackLength_data.set(str(packet.m_trackLength))
        sd_sessionType_data.set(str(packet.m_sessionType))
        sd_trackId_data.set(str(packet.m_trackId))
        sd_era_data.set(str(packet.m_era))
        sd_sessionTimeLeft_data.set(str(packet.m_sessionTimeLeft))
        sd_sessionDuration_data.set(str(packet.m_sessionDuration))
        sd_pitSpeedLimit_data.set(str(packet.m_pitSpeedLimit))
        sd_gamePaused_data.set(str(packet.m_gamePaused))
        sd_isSpectating_data.set(str(packet.m_isSpectating))
        sd_spectatorCarIndex_data.set(str(packet.m_spectatorCarIndex))
        sd_sliProNativeSupport_data.set(str(packet.m_sliProNativeSupport))
        sd_numMarshalZones_data.set(str(packet.m_numMarshalZones))
        # sd_marshalZones_data.set(str(packet.m_marshalZones))
        sd_safetyCarStatus_data.set(str(packet.m_safetyCarStatus))
        sd_networkGame_data.set(str(packet.m_networkGame))

    def new_lap_data(self, packet):
        global ld_lapData_data
        global ld_lastLapTime_data
        global ld_currentLapTime_data
        global ld_bestLapTime_data
        global ld_sector1Time_data
        global ld_sector2Time_data
        global ld_lapDistance_data
        global ld_totalDistance_data
        global ld_safetyCarDelta_data
        global ld_carPosition_data
        global ld_currentLapNum_data
        global ld_pitStatus_data
        global ld_sector_data
        global ld_currentLapInvalid_data
        global ld_penalties_data
        global ld_gridPosition_data
        global ld_driverStatus_data
        global ld_resultStatus_data

        # ld_lapData_data.set(str())
        ld_lastLapTime_data.set(str(packet.m_lapData[0].m_lastLapTime))
        ld_currentLapTime_data.set(str(packet.m_lapData[0].m_currentLapTime))
        ld_bestLapTime_data.set(str(packet.m_lapData[0].m_bestLapTime))
        ld_sector1Time_data.set(str(packet.m_lapData[0].m_sector1Time))
        ld_sector2Time_data.set(str(packet.m_lapData[0].m_sector2Time))
        ld_lapDistance_data.set(str(packet.m_lapData[0].m_lapDistance))
        ld_totalDistance_data.set(str(packet.m_lapData[0].m_totalDistance))
        ld_safetyCarDelta_data.set(str(packet.m_lapData[0].m_safetyCarDelta))
        ld_carPosition_data.set(str(packet.m_lapData[0].m_carPosition))
        ld_currentLapNum_data.set(str(packet.m_lapData[0].m_currentLapNum))
        ld_pitStatus_data.set(str(packet.m_lapData[0].m_pitStatus))
        ld_sector_data.set(str(packet.m_lapData[0].m_sector))
        ld_currentLapInvalid_data.set(str(packet.m_lapData[0].m_currentLapInvalid))
        ld_penalties_data.set(str(packet.m_lapData[0].m_penalties))
        ld_gridPosition_data.set(str(packet.m_lapData[0].m_gridPosition))
        ld_driverStatus_data.set(str(packet.m_lapData[0].m_driverStatus))
        ld_resultStatus_data.set(str(packet.m_lapData[0].m_resultStatus))

    def new_event_data(self, packet):
        global ed_eventStringCode_data

        ed_eventStringCode_data.set(str(packet.m_eventStringCode))

    def new_participant_data(self, packet):
        global pd_numCars_data
        global pd_aiControlled_data
        global pd_driverId_data
        global pd_teamId_data
        global pd_raceNumber_data
        global pd_nationality_data
        global pd_name_data

        pd_numCars_data.set(str(packet.m_numCars))
        pd_aiControlled_data.set(str(packet.m_participants[0].m_aiControlled))
        pd_driverId_data.set(str(packet.m_participants[0].m_driverId))
        pd_teamId_data.set(str(packet.m_participants[0].m_teamId))
        pd_raceNumber_data.set(str(packet.m_participants[0].m_raceNumber))
        pd_nationality_data.set(str(packet.m_participants[0].m_nationality))
        pd_name_data.set(str(packet.m_participants[0].m_name))

    def new_car_setup_data(self, packet):
        global csd_frontWing_data
        global csd_rearWing_data
        global csd_onThrottle_data
        global csd_offThrottle_data
        global csd_frontCamber_data
        global csd_rearCamber_data
        global csd_frontToe_data
        global csd_rearToe_data
        global csd_frontSuspension_data
        global csd_rearSuspension_data
        global csd_frontAntiRollBar_data
        global csd_rearAntiRollBar_data
        global csd_frontSuspensionHeight_data
        global csd_rearSuspensionHeight_data
        global csd_brakePressure_data
        global csd_brakeBias_data
        global csd_frontTyrePressure_data
        global csd_rearTyrePressure_data
        global csd_ballast_data
        global csd_fuelLoad_data

        csd_frontWing_data.set(str(packet.m_carSetups[0].m_frontWing))
        csd_rearWing_data.set(str(packet.m_carSetups[0].m_rearWing))
        csd_onThrottle_data.set(str(packet.m_carSetups[0].m_onThrottle))
        csd_offThrottle_data.set(str(packet.m_carSetups[0].m_offThrottle))
        csd_frontCamber_data.set(str(packet.m_carSetups[0].m_frontCamber))
        csd_rearCamber_data.set(str(packet.m_carSetups[0].m_rearCamber))
        csd_frontToe_data.set(str(packet.m_carSetups[0].m_frontToe))
        csd_rearToe_data.set(str(packet.m_carSetups[0].m_rearToe))
        csd_frontSuspension_data.set(str(packet.m_carSetups[0].m_frontSuspension))
        csd_rearSuspension_data.set(str(packet.m_carSetups[0].m_rearSuspension))
        csd_frontAntiRollBar_data.set(str(packet.m_carSetups[0].m_frontAntiRollBar))
        csd_rearAntiRollBar_data.set(str(packet.m_carSetups[0].m_rearAntiRollBar))
        csd_frontSuspensionHeight_data.set(str(packet.m_carSetups[0].m_frontSuspensionHeight))
        csd_rearSuspensionHeight_data.set(str(packet.m_carSetups[0].m_rearSuspensionHeight))
        csd_brakePressure_data.set(str(packet.m_carSetups[0].m_brakePressure))
        csd_brakeBias_data.set(str(packet.m_carSetups[0].m_brakeBias))
        csd_frontTyrePressure_data.set(str(packet.m_carSetups[0].m_frontTyrePressure))
        csd_rearTyrePressure_data.set(str(packet.m_carSetups[0].m_rearTyrePressure))
        csd_ballast_data.set(str(packet.m_carSetups[0].m_ballast))
        csd_fuelLoad_data.set(str(packet.m_carSetups[0].m_fuelLoad))

    def new_car_telemetry_data(self, packet):
        global ctd_speed_data
        global ctd_throttle_data
        global ctd_steer_data
        global ctd_brake_data
        global ctd_clutch_data
        global ctd_gear_data
        global ctd_engineRPctd_data
        global ctd_drs_data
        global ctd_revLightsPercent_data
        global ctd_brakesTemperature_rl_data
        global ctd_brakesTemperature_rr_data
        global ctd_brakesTemperature_fl_data
        global ctd_brakesTemperature_fr_data
        global ctd_tyresSurfaceTemperature_rl_data
        global ctd_tyresSurfaceTemperature_rr_data
        global ctd_tyresSurfaceTemperature_fl_data
        global ctd_tyresSurfaceTemperature_fr_data
        global ctd_tyresInnerTemperature_rl_data
        global ctd_tyresInnerTemperature_rr_data
        global ctd_tyresInnerTemperature_fl_data
        global ctd_tyresInnerTemperature_fr_data
        global ctd_engineTemperature_data
        global ctd_tyresPressure_rl_data
        global ctd_tyresPressure_rr_data
        global ctd_tyresPressure_fl_data
        global ctd_tyresPressure_fr_data
        global ctd_buttonStatus_data

        ctd_speed_data.set(str(packet.m_carTelemetryData[0].m_speed))
        ctd_throttle_data.set(str(packet.m_carTelemetryData[0].m_throttle))
        ctd_steer_data.set(str(packet.m_carTelemetryData[0].m_steer))
        ctd_brake_data.set(str(packet.m_carTelemetryData[0].m_brake))
        ctd_clutch_data.set(str(packet.m_carTelemetryData[0].m_clutch))
        ctd_gear_data.set(str(packet.m_carTelemetryData[0].m_gear))
        ctd_engineRPM_data.set(str(packet.m_carTelemetryData[0].m_engineRPM))
        ctd_drs_data.set(str(packet.m_carTelemetryData[0].m_drs))
        ctd_revLightsPercent_data.set(str(packet.m_carTelemetryData[0].m_revLightsPercent))
        ctd_brakesTemperature_rl_data.set(str(packet.m_carTelemetryData[0].m_brakesTemperature[0]))  #RL, RR, FL, FR
        ctd_brakesTemperature_rr_data.set(str(packet.m_carTelemetryData[0].m_brakesTemperature[1]))
        ctd_brakesTemperature_fl_data.set(str(packet.m_carTelemetryData[0].m_brakesTemperature[2]))
        ctd_brakesTemperature_fr_data.set(str(packet.m_carTelemetryData[0].m_brakesTemperature[3]))
        ctd_tyresSurfaceTemperature_rl_data.set(str(packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[0])) #RL, RR, FL, FR
        ctd_tyresSurfaceTemperature_rr_data.set(str(packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[1]))
        ctd_tyresSurfaceTemperature_fl_data.set(str(packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[2]))
        ctd_tyresSurfaceTemperature_fr_data.set(str(packet.m_carTelemetryData[0].m_tyresSurfaceTemperature[3]))
        ctd_tyresInnerTemperature_rl_data.set(str(packet.m_carTelemetryData[0].m_tyresInnerTemperature[0])) #RL, RR, FL, FR
        ctd_tyresInnerTemperature_rr_data.set(str(packet.m_carTelemetryData[0].m_tyresInnerTemperature[1]))
        ctd_tyresInnerTemperature_fl_data.set(str(packet.m_carTelemetryData[0].m_tyresInnerTemperature[2]))
        ctd_tyresInnerTemperature_fr_data.set(str(packet.m_carTelemetryData[0].m_tyresInnerTemperature[3]))
        ctd_engineTemperature_data.set(str(packet.m_carTelemetryData[0].m_engineTemperature))
        ctd_tyresPressure_rl_data.set(str(packet.m_carTelemetryData[0].m_tyresPressure[0])) #RL, RR, FL, FR
        ctd_tyresPressure_rr_data.set(str(packet.m_carTelemetryData[0].m_tyresPressure[1]))
        ctd_tyresPressure_fl_data.set(str(packet.m_carTelemetryData[0].m_tyresPressure[2]))
        ctd_tyresPressure_fr_data.set(str(packet.m_carTelemetryData[0].m_tyresPressure[3]))
        ctd_buttonStatus_data.set(str(packet.m_buttonStatus))

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
    	self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            root.destroy()
        self.master.after(100, self.periodicCall)

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        packet_structures = [structs.PacketMotionData, structs.PacketSessionData, structs.PacketLapData, structs.PacketEventData, structs.PacketParticipantsData, structs.PacketCarSetupData, structs.PacketCarTelemetryData, structs.PacketCarStatusData]
        packet_names = ['MotionData', 'SessionData', 'LapData', 'EventData', 'ParticipantData', 'CarSetupData', 'CarTelemetryData', 'PacketCarStatusData']

        # while self.running:
        # To simulate asynchronous I/O, we create a random number at
        # random intervals. Replace the following 2 lines with the real
        # thing.
        # time.sleep(rand.random() * 0.3)
        # msg = rand.random()


        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # bind the socket to the specified ip address and port
        sock.bind(('127.0.0.1', 5003))

        # packet_count = 0

        last_packet = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None}

        while self.running:
            # packet = get_packet(address, port, sock)

            data, addr = sock.recvfrom(1341)




            # Read the packet header and determine which UDPPacket is being recieved from the game
            header_data = data[0:21]
            packet_header = structs.PacketHeader.from_buffer_copy(header_data)
            packet_id = packet_header.m_packetId

            # Print out the packets name
            # print packet_names[packet_id]


            # return data and convert from raw bytes to UDPPacket structure
            packet = packet_structures[packet_id].from_buffer_copy(data)


            # packet_count += 1
            # if last_packet[packet.m_header.m_packetId] is None or packet.m_header.m_sessionTime > last_packet[packet.m_header.m_packetId].m_header.m_sessionTime:
            #     # yield packet
            #     last_packet[packet.m_header.m_packetId] = packet


            # If there are no previous packets recieved thus far for the packet type then use the packet and save it to its previous
            if last_packet[packet.m_header.m_packetId] is None:
                # yield packet
                # print "First PACKET", packet_names[packet.m_header.m_packetId], packet.m_header.m_sessionTime
                last_packet[packet.m_header.m_packetId] = packet
                self.queue.put((packet_names[packet.m_header.m_packetId], packet))
                # return packet_names[packet.m_header.m_packetId], found_packet

            # If the packet is newer than the last recieved and used packet, then use the packet and save it to its previous
            elif packet.m_header.m_sessionTime > last_packet[packet.m_header.m_packetId].m_header.m_sessionTime:
                # yield packet
                # print "New PACKET", packet_names[packet.m_header.m_packetId], packet.m_header.m_sessionTime
                last_packet[packet.m_header.m_packetId] = packet
                self.queue.put((packet_names[packet.m_header.m_packetId], packet))
                # return packet_names[packet.m_header.m_packetId], packet


            # print packet_names[packet.m_header.m_packetId]
            # print "total packets recieved:", packet_count










            # packet = f1_udp_client_test.get_telemetry('127.0.0.1', 5003)
            # self.queue.put(packet)

    def endApplication(self):
        self.running = 0


# rand = random.Random()
root = Tkinter.Tk()
# root.configure(background='SteelBlue1')
# root.lift()
# root.attributes('-topmost',True)
RWidth=root.winfo_screenwidth()
RHeight=root.winfo_screenheight()
root.geometry(("%dx%d")%(RWidth,RHeight))


# motion data
md_world_position_x_data = Tkinter.StringVar(root, value="N/A")
md_world_position_y_data = Tkinter.StringVar(root, value="N/A")
md_world_position_z_data = Tkinter.StringVar(root, value="N/A")
md_world_velocity_x_data = Tkinter.StringVar(root, value="N/A")
md_world_velocity_y_data = Tkinter.StringVar(root, value="N/A")
md_world_velocity_z_data = Tkinter.StringVar(root, value="N/A")
md_world_forward_dir_x_data = Tkinter.StringVar(root, value="N/A")
md_world_forward_dir_y_data = Tkinter.StringVar(root, value="N/A")
md_world_forward_dir_z_data = Tkinter.StringVar(root, value="N/A")
md_world_right_dir_x_data = Tkinter.StringVar(root, value="N/A")
md_world_right_dir_y_data = Tkinter.StringVar(root, value="N/A")
md_world_right_dir_z_data = Tkinter.StringVar(root, value="N/A")
md_g_force_lateral_data = Tkinter.StringVar(root, value="N/A")
md_g_force_longitudinal_data = Tkinter.StringVar(root, value="N/A")
md_g_force_vertical_data = Tkinter.StringVar(root, value="N/A")
md_yaw_data = Tkinter.StringVar(root, value="N/A")
md_pitch_data = Tkinter.StringVar(root, value="N/A")
md_roll_data = Tkinter.StringVar(root, value="N/A")
md_suspension_position_rl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_position_rr_data = Tkinter.StringVar(root, value="N/A")
md_suspension_position_fl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_position_fr_data = Tkinter.StringVar(root, value="N/A")
md_suspension_velocity_rl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_velocity_rr_data = Tkinter.StringVar(root, value="N/A")
md_suspension_velocity_fl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_velocity_fr_data = Tkinter.StringVar(root, value="N/A")
md_suspension_acceleration_rl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_acceleration_rr_data = Tkinter.StringVar(root, value="N/A")
md_suspension_acceleration_fl_data = Tkinter.StringVar(root, value="N/A")
md_suspension_acceleration_fr_data = Tkinter.StringVar(root, value="N/A")
md_wheel_speed_rl_data = Tkinter.StringVar(root, value="N/A")
md_wheel_speed_rr_data = Tkinter.StringVar(root, value="N/A")
md_wheel_speed_fl_data = Tkinter.StringVar(root, value="N/A")
md_wheel_speed_fr_data = Tkinter.StringVar(root, value="N/A")
md_wheel_slip_rl_data = Tkinter.StringVar(root, value="N/A")
md_wheel_slip_rr_data = Tkinter.StringVar(root, value="N/A")
md_wheel_slip_fl_data = Tkinter.StringVar(root, value="N/A")
md_wheel_slip_fr_data = Tkinter.StringVar(root, value="N/A")
md_local_velocityX_data = Tkinter.StringVar(root, value="N/A")
md_local_velocityY_data = Tkinter.StringVar(root, value="N/A")
md_local_velocityZ_data = Tkinter.StringVar(root, value="N/A")
md_angular_velocityX_data = Tkinter.StringVar(root, value="N/A")
md_angular_velocityY_data = Tkinter.StringVar(root, value="N/A")
md_angular_velocityZ_data = Tkinter.StringVar(root, value="N/A")
md_angular_accelerationX_data = Tkinter.StringVar(root, value="N/A")
md_angular_accelerationY_data = Tkinter.StringVar(root, value="N/A")
md_angular_accelerationZ_data = Tkinter.StringVar(root, value="N/A")
md_front_wheels_angle_data = Tkinter.StringVar(root, value="N/A")


# session data
sd_header_data = Tkinter.StringVar(root, value="N/A")
sd_weather_data = Tkinter.StringVar(root, value="N/A")
sd_trackTemperature_data  = Tkinter.StringVar(root, value="N/A")
sd_airTemperature_data  = Tkinter.StringVar(root, value="N/A")
sd_totalLaps_data = Tkinter.StringVar(root, value="N/A")
sd_trackLength_data  = Tkinter.StringVar(root, value="N/A")
sd_sessionType_data  = Tkinter.StringVar(root, value="N/A")
sd_trackId_data = Tkinter.StringVar(root, value="N/A")
sd_era_data = Tkinter.StringVar(root, value="N/A")
sd_sessionTimeLeft_data = Tkinter.StringVar(root, value="N/A")
sd_sessionDuration_data = Tkinter.StringVar(root, value="N/A")
sd_pitSpeedLimit_data = Tkinter.StringVar(root, value="N/A")
sd_gamePaused_data = Tkinter.StringVar(root, value="N/A")
sd_isSpectating_data = Tkinter.StringVar(root, value="N/A")
sd_spectatorCarIndex_data = Tkinter.StringVar(root, value="N/A")
sd_sliProNativeSupport_data = Tkinter.StringVar(root, value="N/A")
sd_numMarshalZones_data = Tkinter.StringVar(root, value="N/A")
sd_marshalZones_data = Tkinter.StringVar(root, value="N/A")
sd_safetyCarStatus_data = Tkinter.StringVar(root, value="N/A")
sd_networkGame_data = Tkinter.StringVar(root, value="N/A")

# lap data
ld_lapData_data = Tkinter.StringVar(root, value="N/A")
ld_lastLapTime_data = Tkinter.StringVar(root, value="N/A")
ld_currentLapTime_data = Tkinter.StringVar(root, value="N/A")
ld_bestLapTime_data = Tkinter.StringVar(root, value="N/A")
ld_sector1Time_data = Tkinter.StringVar(root, value="N/A")
ld_sector2Time_data = Tkinter.StringVar(root, value="N/A")
ld_lapDistance_data = Tkinter.StringVar(root, value="N/A")
ld_totalDistance_data = Tkinter.StringVar(root, value="N/A")
ld_safetyCarDelta_data = Tkinter.StringVar(root, value="N/A")
ld_carPosition_data = Tkinter.StringVar(root, value="N/A")
ld_currentLapNum_data = Tkinter.StringVar(root, value="N/A")
ld_pitStatus_data = Tkinter.StringVar(root, value="N/A")
ld_sector_data = Tkinter.StringVar(root, value="N/A")
ld_currentLapInvalid_data = Tkinter.StringVar(root, value="N/A")
ld_penalties_data = Tkinter.StringVar(root, value="N/A")
ld_gridPosition_data = Tkinter.StringVar(root, value="N/A")
ld_driverStatus_data = Tkinter.StringVar(root, value="N/A")
ld_resultStatus_data = Tkinter.StringVar(root, value="N/A")

# event data
ed_eventStringCode_data = Tkinter.StringVar(root, value="N/A")

# participant data
pd_numCars_data = Tkinter.StringVar(root, value="N/A")
pd_aiControlled_data = Tkinter.StringVar(root, value="N/A")
pd_driverId_data = Tkinter.StringVar(root, value="N/A")
pd_teamId_data = Tkinter.StringVar(root, value="N/A")
pd_raceNumber_data = Tkinter.StringVar(root, value="N/A")
pd_nationality_data = Tkinter.StringVar(root, value="N/A")
pd_name_data = Tkinter.StringVar(root, value="N/A")

# car setup data
csd_frontWing_data = Tkinter.StringVar(root, value="N/A")
csd_rearWing_data = Tkinter.StringVar(root, value="N/A")
csd_onThrottle_data = Tkinter.StringVar(root, value="N/A")
csd_offThrottle_data = Tkinter.StringVar(root, value="N/A")
csd_frontCamber_data = Tkinter.StringVar(root, value="N/A")
csd_rearCamber_data = Tkinter.StringVar(root, value="N/A")
csd_frontToe_data = Tkinter.StringVar(root, value="N/A")
csd_rearToe_data = Tkinter.StringVar(root, value="N/A")
csd_frontSuspension_data = Tkinter.StringVar(root, value="N/A")
csd_rearSuspension_data = Tkinter.StringVar(root, value="N/A")
csd_frontAntiRollBar_data = Tkinter.StringVar(root, value="N/A")
csd_rearAntiRollBar_data = Tkinter.StringVar(root, value="N/A")
csd_frontSuspensionHeight_data = Tkinter.StringVar(root, value="N/A")
csd_rearSuspensionHeight_data = Tkinter.StringVar(root, value="N/A")
csd_brakePressure_data = Tkinter.StringVar(root, value="N/A")
csd_brakeBias_data = Tkinter.StringVar(root, value="N/A")
csd_frontTyrePressure_data = Tkinter.StringVar(root, value="N/A")
csd_rearTyrePressure_data = Tkinter.StringVar(root, value="N/A")
csd_ballast_data = Tkinter.StringVar(root, value="N/A")
csd_fuelLoad_data = Tkinter.StringVar(root, value="N/A")

# car telemetry data
ctd_speed_data = Tkinter.StringVar(root, value="N/A")
ctd_throttle_data = Tkinter.StringVar(root, value="N/A")
ctd_steer_data = Tkinter.StringVar(root, value="N/A")
ctd_brake_data = Tkinter.StringVar(root, value="N/A")
ctd_clutch_data = Tkinter.StringVar(root, value="N/A")
ctd_gear_data = Tkinter.StringVar(root, value="N/A")
ctd_engineRPM_data = Tkinter.StringVar(root, value="N/A")
ctd_drs_data = Tkinter.StringVar(root, value="N/A")
ctd_revLightsPercent_data = Tkinter.StringVar(root, value="N/A")
ctd_brakesTemperature_rl_data = Tkinter.StringVar(root, value="N/A")
ctd_brakesTemperature_rr_data = Tkinter.StringVar(root, value="N/A")
ctd_brakesTemperature_fl_data = Tkinter.StringVar(root, value="N/A")
ctd_brakesTemperature_fr_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresSurfaceTemperature_rl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresSurfaceTemperature_rr_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresSurfaceTemperature_fl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresSurfaceTemperature_fr_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresInnerTemperature_rl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresInnerTemperature_rr_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresInnerTemperature_fl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresInnerTemperature_fr_data = Tkinter.StringVar(root, value="N/A")
ctd_engineTemperature_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresPressure_rl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresPressure_rr_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresPressure_fl_data = Tkinter.StringVar(root, value="N/A")
ctd_tyresPressure_fr_data = Tkinter.StringVar(root, value="N/A")
ctd_buttonStatus_data = Tkinter.StringVar(root, value="N/A")

client = ThreadedClient(root)
root.mainloop()
# root.destroy()
