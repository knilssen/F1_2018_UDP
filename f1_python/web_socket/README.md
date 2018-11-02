In order to run the websocket, you will need to install tornado:

    pip install tornado

## Running The WebSocket

To run the websocket, there are two options.

* Default when running the websocket for both of the following udp_port is set to 5003, the pcap emultor

* directions to switch over to F1 packet broadcasting are below

### Users Car Packet View

To run the user car packets view simply run:

    python tornado_broker.py

To run with pcap emulator or with the actual f1 game, simply comment out the correct line in tornado_broker:

    119  # For using with the live F1 2018 game
    120  # listning_ip_address     = ''
    121  # udp_port                = 20777
    122  
    123  # For using the pcap emulator
    124  listning_ip_address     = '127.0.0.1'
    125  udp_port                = 5003

Go to your web browser and enter:

    http://localhost:9090/


### Live Map View

To run the live map view simply run:

    python live_map_tornado.py

To run with pcap emulator or with the actual f1 game, simply comment out the correct line in live_map_tornado:

    124  # For using with the live F1 2018 game
    125  # listning_ip_address     = ''
    126  # udp_port                = 20777
    127      
    128  # For using the pcap emulator
    129  listning_ip_address     = '127.0.0.1'
    130  udp_port                = 5003

Go to your web browser and enter:

    http://localhost:9090/




## Screen shots
### USERS CAR PACKET DATAS
![MENU](./screenshots/user_car_packet_view.png)

### LIVE MAP
![MENU](./screenshots/live_map_view.png)
