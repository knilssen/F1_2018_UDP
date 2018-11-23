package main

import (
  "bytes"

  "encoding/binary"

  "net"

  "fmt"

  // Imports our struct package which has all of our udp structs
  "github.com/knilssen/f1_go/structs"
)


func main() {
  addr, _ := net.ResolveUDPAddr("udp", ":5003")
  sock, _ := net.ListenUDP("udp", addr)


  // Set up our structs including the header struct so we are able to determine which
  // udp packet is incoming and we can deal with it accordingly
  var header structs.PacketHeader
  var motion_packet structs.PacketMotionData
  var session_packet structs.PacketSessionData
  var lap_packet structs.PacketLapData
  var event_packet structs.PacketEventData
  var participant_packet structs.PacketParticipantsData
  var car_setup_packet structs.PacketCarSetupData
  var telemetry_packet structs.PacketCarTelemetryData
  var car_status_packet structs.PacketCarStatusData



  // Now loop, checking for udp packets and dealing with them accordingly
  for {
    // Create a buffer to read the incoming udp packets
    // Read the udp packets and if we get an error while reading, print out the error
    buf := make([]byte, 1341)
    _, _, err := sock.ReadFromUDP(buf)
    if err != nil {
      fmt.Println(err)
    }


    // Set two new readers in which to cast into our structs.
    // One is for the header, which we determine what packet we have and then use the other
    // for the whole packet.
    header_bytes_reader := bytes.NewReader(buf[0:21])
    packet_bytes_reader := bytes.NewReader(buf)

    // Read the binary of the udp packet header into our struct
    if err := binary.Read(header_bytes_reader, binary.LittleEndian, &header); err != nil {
		    fmt.Println("binary.Read header failed:", err)
  	}

    // Depending on which packet we have, which we find by looking at header.M_packetId
    // We use a switch statement to then read the whole binary udp packet into its associated struct
    switch header.M_packetId {
    case 0:
        // If the packet we received is a motion_packet, read its binary into our motion_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &motion_packet); err != nil {
    		    fmt.Println("binary.Read motion_packet failed:", err)
      	}
        fmt.Println(motion_packet)
    case 1:
        // If the packet we received is the session_packet, read its binary into our session_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &session_packet); err != nil {
    		    fmt.Println("binary.Read session_packet failed:", err)
      	}
        fmt.Println(session_packet)
    case 2:
        // If the packet we received is the lap_packet, read its binary into our lap_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &lap_packet); err != nil {
    		    fmt.Println("binary.Read lap_packet failed:", err)
      	}
        fmt.Println(lap_packet)
    case 3:
        // If the packet we received is the event_packet, read its binary into our event_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &event_packet); err != nil {
    		    fmt.Println("binary.Read event_packet failed:", err)
      	}
        fmt.Println(event_packet)
    case 4:
        // If the packet we received is the participant_packet, read its binary into our participant_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &participant_packet); err != nil {
    		    fmt.Println("binary.Read participant_packet failed:", err)
      	}
        fmt.Println(participant_packet)
    case 5:
        // If the packet we received is the car_setup_packet, read its binary into our car_setup_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &car_setup_packet); err != nil {
    		    fmt.Println("binary.Read car_setup_packet failed:", err)
      	}
        fmt.Println(car_setup_packet)
    case 6:
        // If the packet we received is the telemetry_packet, read its binary into our telemetry_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &telemetry_packet); err != nil {
    		    fmt.Println("binary.Read telemetry_packet failed:", err)
      	}
        fmt.Println(telemetry_packet)
    case 7:
        // If the packet we received is the car_status_packet, read its binary into our car_status_packet struct
        if err := binary.Read(packet_bytes_reader, binary.LittleEndian, &car_status_packet); err != nil {
    		    fmt.Println("binary.Read car_status_packet failed:", err)
      	}
        fmt.Println(car_status_packet)
    }

  }
}
