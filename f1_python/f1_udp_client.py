import socket
import ctypes
import sys
import binascii
import structs
from pprint import pprint

packet_structures = [structs.PacketMotionData, structs.PacketSessionData, structs.PacketLapData, structs.PacketEventData, structs.PacketParticipantsData, structs.PacketCarSetupData, structs.PacketCarTelemetryData, structs.PacketCarStatusData]
packet_names = ['MotionData', 'SessionData', 'LapData', 'ParticipantData', 'CarSetupData', 'CarTelemetryData', 'PacketCarStatusData']

def get_packet(address, port):
    """
    Recieve a single UDP telemetry packet from the specified port and ip address

    :param address: IP address for the socket
    :param port: Port for the socket
    :return: A UDPPacket
    """
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind the socket to the specified ip address and port
    sock.bind((address, port))

    # recieve data
    data, addr = sock.recvfrom(1341)


    # Read the packet header and determine which UDPPacket is being recieved from the game
    header_data = data[0:21]
    packet_header = structs.PacketHeader.from_buffer_copy(header_data)
    packet_id = packet_header.m_packetId

    # Print out the packets name
    print packet_names[packet_id]

    # return data and convert from raw bytes to UDPPacket structure
    return packet_structures[packet_id].from_buffer_copy(data)




def get_telemetry(address, port):
    """
    :param address: IP address for receiving packets
    :param port: Port on which to receive packets
    :yeild: a UDPPacket for each udp packet received
    """
    last_packet = None

    while True:
        packet = get_packet(address, port)
        if last_packet is None or packet.m_header.m_sessionTime > last_packet.m_header.m_sessionTime:
            yield packet
            last_packet = packet


def main(address, port):
    # Enter the ip and port you are using
    for packet in get_telemetry(address, port):
        pprint(dir(packet))

        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Kristians Usuage:     python python_udp_test.py  127.0.0.1 5003
        print 'Correct Usage is:            python f1_udp_client.py     [ ip address ]      [ port ]'
    else:
        main(sys.argv[1],sys.argv[2])
