#
#
# Need to install tornado
# Using this as a WebSocket server, listening for certain UDP packets to arrive and translate them into WebSocket messages.
#
# pip install tornado
#
# Written with help from https://github.com/simplicitylab/electronics-experiments/tree/master/Transfer%20sensor%20readings%20over%20WebSockets/python
#
#

# tornado
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

# standard lib
import socket
import functools
import ConfigParser
import json

# Import udp data structs
import structs

# Import out packet to json converter
import structs_to_json  # All Cars
# import structs_to_json_users_car # Only users car

class Notifier():
    """ Notifier utility class """

    _callbacks = []

    def register_callback(self, callback):
        """ register callback """
        self._callbacks.append(callback)

    def remove_callback(self, callback):
        """ remove callback """
        self._callbacks.remove(callback)

    def notify(self, data):
        """ notify """
        for callback in self._callbacks:
            callback(data) # callback

notifier = Notifier()

class WSHandler(tornado.websocket.WebSocketHandler):
    """ WebSocket handler """

    def initialize(self, notifier):
        """ initialize when a new websocket connects """
        self._notifier = notifier
        self._notifier.register_callback(self.process_notification)

    def process_notification(self, data):
        """ process notification """
        self.write_message(data)

    def open(self):
        """ when a websocket connect """
        pass

    def on_message(self, message):
        print 'received message: %s\n' %message
        self.write_message(message + ' OK')

    def on_close(self):
        """ when the websocket disconnects"""
        # remove callback so it doesn't get called in the future
        self._notifier.remove_callback(self.process_notification)

class HTMLHandler(tornado.web.RequestHandler):
    """ HTML handler """
    def get(self):
        loader = tornado.template.Loader(".")
        # self.write(loader.load("user_car_packets_view.html").generate())
        self.write(loader.load("map_draw_live.html").generate())

@tornado.gen.coroutine
def handle_udp_messages(sock, fd, events):
    """ Handles UDP messages it receives """
    packet_structures = [structs.PacketMotionData, structs.PacketSessionData, structs.PacketLapData, structs.PacketEventData, structs.PacketParticipantsData, structs.PacketCarSetupData, structs.PacketCarTelemetryData, structs.PacketCarStatusData]
    packet_names = ['MotionData', 'SessionData', 'LapData', 'EventData', 'ParticipantData', 'CarSetupData', 'CarTelemetryData', 'PacketCarStatusData']
    while True:
        try:
            data, addr = sock.recvfrom(1341) # buffer size is 1341 bytes


            # Header data is contained in the first 21 bytes. Take this to obtain packets identifying information
            header_data = data[0:21]
            packet_header = structs.PacketHeader.from_buffer_copy(header_data)
            packet_id = packet_header.m_packetId
            # Since the live map is only dealing with the motion data packet, only proceed to json and the notifier
            # if and only if the packet received is the motion data packet
            if packet_id == 0:
                packet = packet_structures[packet_id].from_buffer_copy(data)
                packet = structs_to_json.structs(packet_names[packet_id], packet)
                # notify that we have new data
                notifier.notify(packet)
        except socket.error, e:
            break

# setup application routes
application = tornado.web.Application([
  (r'/ws', WSHandler, dict(notifier=notifier)),
  (r'/', HTMLHandler),
  (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
])

if __name__ == '__main__':
    # Port used for the local host webpage, http://localhost:9090/
    server_port = '9090'
    # Use the below commented out line in order to make work with matts f1 udp broadcasting on port 20777
    # udp_port    = '20777'
    udp_port    = 5003

    # application start listening on port 9090
    application.listen(server_port)

    # setup socket for UDP listening
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',udp_port))
    sock.setblocking(False)

    # create handler that deals with our UDP messages
    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(handle_udp_messages, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)

    io_loop.start()
