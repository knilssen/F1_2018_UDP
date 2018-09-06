import socket
import ctypes
import sys
import binascii
import structs


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

    # convert from raw bytes to UDPPacket structure
    pack_len = len(data)
    print pack_len

    # return data
    # If packet recieved is Motion Data
    if pack_len == 1341:
        print "Motion Data Recieved"
        return structs.PacketMotionData.from_buffer_copy(data)
    # If packet recieved is Seesion Data
    elif pack_len == 147:
        print "Session Data Recieved"
        return structs.PacketSessionData.from_buffer_copy(data)
    # If packet recieved is Lap Data
    # elif pakc_len == 841:
    #     return structs.PacketSessionData.from_buffer_copy(data)



def get_telemetry(address, port):
    """
    :param address: IP address for receiving packets
    :param port: Port on which to receive packets
    :yeild: a UDPPacket for each udp packet received
    """
    last_packet = None

    while True:
        packet = get_packet(address, port)
    # if last_packet is None or packet.time > last_packet.time:
        yield packet
        last_packet = packet


def main(address, port):
    # Enter the ip and port you are using
    for packet in get_telemetry('127.0.0.1', 5003):
        print packet


if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Kristians Usuage:     python python_udp_test.py  127.0.0.1 5003
        print 'Correct Usage is:            python f1_udp_client.py     [ ip address ]      [ port ]'
    else:
        main(sys.argv[1],sys.argv[2])
