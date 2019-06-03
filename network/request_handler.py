""" qBarista: tasty web-served seismic quizzes.

This file defines the request handler for the socket-server.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import socketserver
import subprocess

from wireless import Wireless


class qBaristaRequestHandler(socketserver.BaseRequestHandler):
    """ The Request Handler for the qBarista socket server. """

    def handle(self):
        """ Handle the request from the client. """

        data = self.request.recv(1024)
        msg = data.decode()

        if msg == 'Hello!':
            # greet back
            self.request.send(b'Hello to you to!')

        elif msg == 'Shutdown!':
            # halt the RPi
            self.request.send(b'Shutting down...')
            subprocess.run(['sudo', 'shutdown', '-h', 'now'])

        elif msg == 'Reboot!':
            # reboot the RPi
            self.request.send(b'Rebooting...')
            subprocess.run(['sudo', 'shutdown', '-r', 'now'])

        elif msg == 'Report connection!':
            # report current wifi connection
            self.server.wireless_connection = Wireless()
            current = self.server.wireless_connection.current()
            if current:
                self.request.send(b'Currently connected to %s!' % current.encode())
            else:
                self.request.send(b'Currently not connected!')

        elif msg[:8] == 'Connect:':
            # connect to a Wifi Network
            self.server.wireless_connection = Wireless()
            _, ssid, password = msg.split()
            if self.server.wireless_connection.connect(ssid, password):
                self.request.send(b'Connected to WiFi!')
            else:
                self.request.send(b'Connection attempt failed.')

        else:
            self.request.send(b'Unrecognized request')

        return
