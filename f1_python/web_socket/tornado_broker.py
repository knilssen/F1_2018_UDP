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
        self.write(loader.load("index.html").generate())

@tornado.gen.coroutine
def handle_udp_messages(sock, fd, events):
    """ Handles UDP messages it receives """
    packet_structures = [structs.PacketMotionData, structs.PacketSessionData, structs.PacketLapData, structs.PacketEventData, structs.PacketParticipantsData, structs.PacketCarSetupData, structs.PacketCarTelemetryData, structs.PacketCarStatusData]
    packet_names = ['MotionData', 'SessionData', 'LapData', 'EventData', 'ParticipantData', 'CarSetupData', 'CarTelemetryData', 'PacketCarStatusData']
    # last_packet = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None}
    while True:
        try:
            data, addr = sock.recvfrom(1341) # buffer size is 1341 bytes

            if not data:
                print "connection closed"
                sock.close()
                break
            else:
                # print "Received %d bytes: '%s'" % (len(data), data)
                header_data = data[0:21]
                packet_header = structs.PacketHeader.from_buffer_copy(header_data)
                packet_id = packet_header.m_packetId
                packet = packet_structures[packet_id].from_buffer_copy(data)
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

    # Read configuration
    # Config = ConfigParser.ConfigParser()
    # Config.read("settings.ini")
    server_port = '9090'
    udp_port    = '20777'

    # application start listening on port 9090
    application.listen(server_port)

    # setup socket for UDP listening
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('',udp_port))
    sock.setblocking(False)

    # create handler that deals with our UDP messages
    io_loop = tornado.ioloop.IOLoop.current()
    callback = functools.partial(handle_udp_messages, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)

    io_loop.start()
