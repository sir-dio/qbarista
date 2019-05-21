""" qBarista: tasty web-served seismic tests.

This file defines the socket-server that runs on the Raspberry Pi and is used
to accept commands via the main computer based socket-clie.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from network.request_handler import qBaristaRequestHandler

import socketserver

if __name__ == '__main__':
    address = ('0.0.0.0', 9118)
    server = socketserver.TCPServer(address, qBaristaRequestHandler)
    server.serve_forever()
