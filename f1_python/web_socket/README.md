In order to run the websocket, you will need to install tornado:

    pip install tornado

to run the websocket:

    python tornado_broker.py

Go to your web browser and enter:

    http://localhost:9090/






To change the GUI, simply comment out which gui you would like to run such as:


    class HTMLHandler(tornado.web.RequestHandler):
        """ HTML handler """
        def get(self):
            loader = tornado.template.Loader(".")
            # self.write(loader.load("user_car_packets_view.html").generate())
            self.write(loader.load("map_draw_live.html").generate())
    
