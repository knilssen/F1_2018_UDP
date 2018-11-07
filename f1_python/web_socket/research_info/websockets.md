### Websockets with python tornado

[https://www.simplicity.be/article/transferring-sensor-readings-over-websockets/](https://www.simplicity.be/article/transferring-sensor-readings-over-websockets/)

The WebSocket broker is the most difficult part of this project. What the broker does is function as a WebSocket server, listening for certain UDP packets to arrive and translate them into WebSocket messages. For demo purposes, it also contains a handler for serving HTML.

To handle WebSockets I’ve settled on using Tornado. The reason being that it’s a mature web framework that can easily scale to tens of thousands of open connections.


```
I won’t post the complete source code but will focus only on the important bits. I will share all the source code on my Github. We start with the section that listens for the UDP packets.

Python
@tornado.gen.coroutine
def handle_udp_messages(sock, fd, events):
    """ Handles UDP messages it receives """
    while True:
        try:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            if not data:
                sock.close()
                break
            else:
                # for debugging purpose
                print "Received %d bytes: '%s'" % (len(data), data)

                # notify that we have new data
                notifier.notify(data)
        except socket.error, e:
            break
```

Sockets are initialized in the same way we did for the sensor module. The only difference here is that we are receiving packets instead of sending them.

When listening for UDP messages we don’t want to block the execution of other code like our WebSocket handler. This can be easily done by adding a coroutine decorator) which makes that this code can run asynchronously.

When data is received we executed the notify method (also passing the data) of a notifier class that is also shared with our WebSocket handler.


```
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
```

I created this simple class to handle communications between the asynchronous part and our handler.

The main idea is that the WebSocket handler can register some of its methods that will be called from the moment the “notify method” is executed by the UDP listener. You can compare it best with the observer pattern.

```
class WSHandler(tornado.websocket.WebSocketHandler):
    """ WebSocket handler """

    def initialize(self, notifier):
        """ initialize when a new websocket connects """
        self._notifier = notifier
        self._notifier.register_callback(self.process_notification)

    def process_notification(self, data):
        """ process notification """
        self.write_message(data)

    ...
```

The WebSocket handler is also very simple. In our constructor, we register the callbacks that need to be called from the moment our UDP listener has received data.

In the “process_notification method”, we can directly pass the data to our connected clients as the sensor module is sending readings as JSON strings. And that is all that our broker needs to do.

From within JavaScript we can then do something like this to receive the readings

```
// connect to websocket
var ws = new WebSocket('ws://localhost:9090/ws');

// when a new message has been received
ws.onmessage = function(event){
   console.log(`sensor: ${event.data.sensor} value: ${event.data.value}`);
}
```
