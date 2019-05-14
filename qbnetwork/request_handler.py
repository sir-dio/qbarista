""" qBarista: tasty web-served seismic tests.

This file defines the request handler for the socket-server.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import socketserver


class qBaristaRequestHandler(socketserver.BaseRequestHandler):
    """ The Request Handler for the qBarista socket server."""

    def handle(self):
        """ Handle the request from the client. """

        data = self.request.recv(1024)
        self.request.send(data)

        return
