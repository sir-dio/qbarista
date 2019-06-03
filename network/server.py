""" qBarista: tasty web-served seismic quizzes.

This file defines the socket-server that runs on the Raspberry Pi and is used
to accept commands via the main computer based socket-client.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import network

import socketserver
from wireless import Wireless


class qBaristaServer(socketserver.TCPServer):

    def __init__(self, handler_class=network.qBaristaRequestHandler):
        self.address = ('0.0.0.0', 9118)
        super().__init__(self.address, handler_class)

        self.wireless_connection = None
