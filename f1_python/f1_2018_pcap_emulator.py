import socket
import ctypes
import binascii
import time
import structs
from scapy.all import *

def main():
    # Use the ip and the port set is the games udp settings
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5003


    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT

    sending_sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

    for pkt in PcapReader('f1.pcap'):
        packet_hex = str(pkt).encode("HEX")[84:]
        packet_binary = binascii.unhexlify(packet_hex)
        sending_sock.sendto(packet_binary, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    main()
