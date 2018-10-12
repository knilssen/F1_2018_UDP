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
import f1_udp_client_test

class GuiPart(Frame):
    def __init__(self, master, queue, endCommand):
        Frame.__init__(self)
        self.queue = queue
        # Set up the GUI
        console = Tkinter.Button(master, text='Done', command=endCommand)
        console.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # self.QUIT = Button(self)
        # self.QUIT["text"] = "QUIT"
        # self.QUIT["command"] =  self.quit
        #
        # self.QUIT.grid(row=0, sticky=W, padx=5, pady=5)

        # Show data from UDP stream

        # Set lables for the different packets
        self.motion_data_title = Label(self, text = "MOTION DATA").grid(row=4, column=0, sticky=W, columnspan=2, padx=5)
        self.session_data_title = Label(self, text = "SESSION DATA").grid(row=4, column=2, sticky=W, columnspan=2)
        self.lap_data_title = Label(self, text = "LAP DATA").grid(row=4, column=4, sticky=W, columnspan=2)
        self.event_data_title = Label(self, text = "EVENT DATA").grid(row=4, column=6, sticky=W, columnspan=2)
        self.participant_data_title = Label(self, text = "PARTICIPANT DATA").grid(row=4, column=8, sticky=W, columnspan=2)
        self.car_setup_data_title = Label(self, text = "CAR SETUP DATA").grid(row=4, column=10, sticky=W, columnspan=2)
        self.car_telemetry_data_title = Label(self, text = "CAR TELEMETRY DATA").grid(row=4, column=12, sticky=W, columnspan=2)
        self.packet_car_status_data_title = Label(self, text = "PACKET CAR STATUS DATA").grid(row=4, column=14, sticky=W, columnspan=2)






        # Set lables for each of the packets datas

        # Motion data
        # self.md_header = Label(self, text = "").grid(row=4, column=0, sticky=W)
        # self.md_car_motion_data = Label(self, text = "").grid(row=5, column=0, sticky=W)                            # For all cars, need to isolate only users car for now/this test
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



        # Event data



        # Partcipant data



        # Car Setup Data



        # Car Telemetry Data



        # Packet Car Status Data












        # Data for each of the packets

        # Motion data
        # self.md_car_motion_data = Label(self, text = "").grid(row=5, column=0, sticky=W)

        # ttk.Label(frame, textvariable = credit).pack()

        self.md_world_position_x_data_label = Label(self, textvariable = md_world_position_x_data).grid(row=6, column=1, sticky=W, padx=5)
        self.md_world_position_y_data_label = Label(self, textvariable = md_world_position_y_data).grid(row=7, column=1, sticky=W, padx=5)
        self.md_world_position_z_data_label = Label(self, textvariable = md_world_position_z_data).grid(row=8, column=1, sticky=W, padx=5)
        self.md_world_velocity_x_data_label = Label(self, textvariable = md_world_velocity_x_data).grid(row=9, column=1, sticky=W, padx=5)
        self.md_world_velocity_y_data_label = Label(self, textvariable = md_world_velocity_y_data).grid(row=10, column=1, sticky=W, padx=5)
        self.md_world_velocity_z_data_label = Label(self, textvariable = md_world_velocity_z_data).grid(row=11, column=1, sticky=W, padx=5)
        self.md_world_forward_dir_x_data_label = Label(self, textvariable = md_world_forward_dir_x_data).grid(row=12, column=1, sticky=W, padx=5)
        self.md_world_forward_dir_y_data_label = Label(self, textvariable = md_world_forward_dir_y_data).grid(row=13, column=1, sticky=W, padx=5)
        self.md_world_forward_dir_z_data_label = Label(self, textvariable = md_world_forward_dir_z_data).grid(row=14, column=1, sticky=W, padx=5)
        self.md_world_right_dir_x_data_label = Label(self, textvariable = md_world_right_dir_x_data).grid(row=15, column=1, sticky=W, padx=5)
        self.md_world_right_dir_y_data_label = Label(self, textvariable = md_world_right_dir_y_data).grid(row=16, column=1, sticky=W, padx=5)
        self.md_world_right_dir_z_data_label = Label(self, textvariable = md_world_right_dir_z_data).grid(row=17, column=1, sticky=W, padx=5)
        self.md_g_force_lateral_data_label = Label(self, textvariable = md_g_force_lateral_data).grid(row=18, column=1, sticky=W, padx=5)
        self.md_g_force_longitudinal_data_label = Label(self, textvariable = md_g_force_longitudinal_data).grid(row=19, column=1, sticky=W, padx=5)
        self.md_g_force_vertical_data_label = Label(self, textvariable = md_g_force_vertical_data).grid(row=20, column=1, sticky=W, padx=5)
        self.md_yaw_data_label = Label(self, textvariable = md_yaw_data).grid(row=21, column=1, sticky=W, padx=5)
        self.md_pitch_data_label = Label(self, textvariable = md_pitch_data).grid(row=22, column=1, sticky=W, padx=5)
        self.md_roll_data_label = Label(self, textvariable = md_roll_data).grid(row=23, column=1, sticky=W, padx=5)

        self.md_suspension_position_rl_data_label = Label(self, textvariable = md_suspension_position_rl_data).grid(row=25, column=0, sticky=W, padx=5)                   # All wheel arrays have the following order RL, RR, FL, FR
        self.md_suspension_position_rr_data_label = Label(self, textvariable = md_suspension_position_rr_data).grid(row=25, column=1, sticky=W, padx=5)
        self.md_suspension_position_fl_data_label = Label(self, textvariable = md_suspension_position_fl_data).grid(row=26, column=0, sticky=W, padx=5)
        self.md_suspension_position_fr_data_label = Label(self, textvariable = md_suspension_position_fr_data).grid(row=26, column=1, sticky=W, padx=5)

        self.md_suspension_velocity_rl_data_label = Label(self, textvariable = md_suspension_velocity_rl_data).grid(row=28, column=0, sticky=W, padx=5)
        self.md_suspension_velocity_rr_data_label = Label(self, textvariable = md_suspension_velocity_rr_data).grid(row=28, column=1, sticky=W, padx=5)
        self.md_suspension_velocity_fl_data_label = Label(self, textvariable = md_suspension_velocity_fl_data).grid(row=29, column=0, sticky=W, padx=5)
        self.md_suspension_velocity_fr_data_label = Label(self, textvariable = md_suspension_velocity_fr_data).grid(row=29, column=1, sticky=W, padx=5)

        self.md_suspension_acceleration_rl_data_label = Label(self, textvariable = md_suspension_acceleration_rl_data).grid(row=31, column=0, sticky=W, padx=5)
        self.md_suspension_acceleration_rr_data_label = Label(self, textvariable = md_suspension_acceleration_rr_data).grid(row=31, column=1, sticky=W, padx=5)
        self.md_suspension_acceleration_fl_data_label = Label(self, textvariable = md_suspension_acceleration_fl_data).grid(row=32, column=0, sticky=W, padx=5)
        self.md_suspension_acceleration_fr_data_label = Label(self, textvariable = md_suspension_acceleration_fr_data).grid(row=32, column=1, sticky=W, padx=5)

        self.md_wheel_speed_rl_data_label = Label(self, textvariable = md_wheel_speed_rl_data).grid(row=34, column=0, sticky=W, padx=5)
        self.md_wheel_speed_rr_data_label = Label(self, textvariable = md_wheel_speed_rr_data).grid(row=34, column=1, sticky=W, padx=5)
        self.md_wheel_speed_fl_data_label = Label(self, textvariable = md_wheel_speed_fl_data).grid(row=35, column=0, sticky=W, padx=5)
        self.md_wheel_speed_fr_data_label = Label(self, textvariable = md_wheel_speed_fr_data).grid(row=35, column=1, sticky=W, padx=5)

        self.md_wheel_slip_rl_data_label = Label(self, textvariable = md_wheel_slip_rl_data).grid(row=37, column=0, sticky=W, padx=5)
        self.md_wheel_slip_rr_data_label = Label(self, textvariable = md_wheel_slip_rr_data).grid(row=37, column=1, sticky=W, padx=5)
        self.md_wheel_slip_fl_data_label = Label(self, textvariable = md_wheel_slip_fl_data).grid(row=38, column=0, sticky=W, padx=5)
        self.md_wheel_slip_fr_data_label = Label(self, textvariable = md_wheel_slip_fr_data).grid(row=38, column=1, sticky=W, padx=5)

        self.md_local_velocityX_data_label = Label(self, textvariable = md_local_velocityX_data).grid(row=39, column=1, sticky=W, padx=5)
        self.md_local_velocityY_data_label = Label(self, textvariable = md_local_velocityY_data).grid(row=40, column=1, sticky=W, padx=5)
        self.md_local_velocityZ_data_label = Label(self, textvariable = md_local_velocityZ_data).grid(row=41, column=1, sticky=W, padx=5)
        self.md_angular_velocityX_data_label = Label(self, textvariable = md_angular_velocityX_data).grid(row=42, column=1, sticky=W, padx=5)
        self.md_angular_velocityY_data_label = Label(self, textvariable = md_angular_velocityY_data).grid(row=43, column=1, sticky=W, padx=5)
        self.md_angular_velocityZ_data_label = Label(self, textvariable = md_angular_velocityZ_data).grid(row=44, column=1, sticky=W, padx=5)
        self.md_angular_accelerationX_data_label = Label(self, textvariable = md_angular_accelerationX_data).grid(row=45, column=1, sticky=W, padx=5)
        self.md_angular_accelerationY_data_label = Label(self, textvariable = md_angular_accelerationY_data).grid(row=46, column=1, sticky=W, padx=5)
        self.md_angular_accelerationZ_data_label = Label(self, textvariable = md_angular_accelerationZ_data).grid(row=47, column=1, sticky=W, padx=5)
        self.md_front_wheels_angle_data_label = Label(self, textvariable = md_front_wheels_angle_data).grid(row=48, column=1, sticky=W, padx=5)


        # session DATA
        self.sd_weather = Label(self, textvariable = sd_weather_data).grid(row=6, column=3, sticky=W)
        self.sd_trackTemperature = Label(self, textvariable = sd_trackTemperature_data).grid(row=7, column=3, sticky=W)
        self.sd_airTemperature = Label(self, textvariable = sd_airTemperature_data).grid(row=8, column=3, sticky=W)
        self.sd_totalLaps = Label(self, textvariable = sd_totalLaps_data).grid(row=9, column=3, sticky=W)
        self.sd_trackLength = Label(self, textvariable = sd_trackLength_data).grid(row=10, column=3, sticky=W)
        self.sd_sessionType = Label(self, textvariable = sd_sessionType_data).grid(row=11, column=3, sticky=W)
        self.sd_trackId = Label(self, textvariable = sd_trackId_data).grid(row=12, column=3, sticky=W)
        self.sd_era = Label(self, textvariable = sd_era_data).grid(row=13, column=3, sticky=W)
        self.sd_sessionTimeLeft = Label(self, textvariable = sd_sessionTimeLeft_data).grid(row=14, column=3, sticky=W)
        self.sd_sessionDuration = Label(self, textvariable = sd_sessionDuration_data).grid(row=15, column=3, sticky=W)
        self.sd_pitSpeedLimit = Label(self, textvariable = sd_pitSpeedLimit_data).grid(row=16, column=3, sticky=W)
        self.sd_gamePaused = Label(self, textvariable = sd_gamePaused_data).grid(row=17, column=3, sticky=W)
        self.sd_isSpectating = Label(self, textvariable = sd_isSpectating_data).grid(row=18, column=3, sticky=W)
        self.sd_spectatorCarIndex = Label(self, textvariable = sd_spectatorCarIndex_data).grid(row=19, column=3, sticky=W)
        self.sd_sliProNativeSupport = Label(self, textvariable = sd_sliProNativeSupport_data).grid(row=20, column=3, sticky=W)
        self.sd_numMarshalZones = Label(self, textvariable = sd_numMarshalZones_data).grid(row=21, column=3, sticky=W)
        self.sd_marshalZones = Label(self, textvariable = sd_marshalZones_data).grid(row=22, column=3, sticky=W)
        self.sd_safetyCarStatus = Label(self, textvariable = sd_safetyCarStatus_data).grid(row=23, column=3, sticky=W)
        self.sd_networkGame = Label(self, textvariable = sd_networkGame_data).grid(row=24, column=3, sticky=W)
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

client = ThreadedClient(root)
root.mainloop()
# root.destroy()
