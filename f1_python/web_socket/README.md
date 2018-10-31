In order to run the websocket, you will need to install tornado:

    pip install tornado

To run the websocket, there are two options.

### user car packets view

To run the user car packets view simply run:

    python tornado_broker.py

To run with pcap emulator or with the actual f1 game, simply comment out the correct line in tornado_broker:

    118 # Use the below commented out line in order to make work with matts f1 udp broadcasting on port 20777
    119 # udp_port    = '20777'
    120 udp_port    = 5003

### live map view

To run the live map view simply run:

    python live_map_tornado.py

To run with pcap emulator or with the actual f1 game, simply comment out the correct line in live_map_tornado:

    117 # Use the below commented out line in order to make work with matts f1 udp broadcasting on port 20777
    118 # udp_port    = '20777'
    119 udp_port    = 5003

Go to your web browser and enter:

    http://localhost:9090/




## Screen shots
### USERS CAR PACKET DATAS
![MENU](./screenshots/user_car_packet_view.png)

### LIVE MAP
![MENU](./screenshots/live_map_view_screenshot.png)
