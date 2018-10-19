#
#
# Requires Scapy to run!
# pip install scapy
# Before running this script
#
#

from scapy.all import *
import structs
# import scapy

packet_structures = [structs.PacketMotionData, structs.PacketSessionData, structs.PacketLapData, structs.PacketEventData, structs.PacketParticipantsData, structs.PacketCarSetupData, structs.PacketCarTelemetryData, structs.PacketCarStatusData]
packet_names = ['MotionData', 'SessionData', 'EventData', 'LapData', 'ParticipantData', 'CarSetupData', 'CarTelemetryData', 'PacketCarStatusData']

def main(pcap, packet_name):
    count = 0
    for pkt in PcapReader(pcap):
        count += 1
        packet_hex = str(pkt).encode("HEX")[84:]
        packet_binary = binascii.unhexlify(packet_hex)

        header_data = packet_binary[0:21]
        packet_header = structs.PacketHeader.from_buffer_copy(header_data)
        packet_id = packet_header.m_packetId
        packet_name = packet_names[packet_id]

        if packet_name == packet_name:
            print "Found a", packet_name, "packet!"
            print "Found with the", count, "packet of the pcap"
            return packet_hex



    # print PcapReader(pcap)[0].show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Correct Usage is:            python pcap_packet_finder.py     [ pcap file address ]      [ packet name ]'
        print 'For our sake, having the f1.pcap file in the current directory, just use:     python pcap_packet_finder.py f1.pcap CarSetupData'
    else:
        print main(sys.argv[1])
