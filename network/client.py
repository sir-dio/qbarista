""" qBarista: tasty web-served seismic tests.

This file defines the socket-client that is used on the main computer to
control the Raspberry Pi.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import socket


def send(msg):
    """ Sends the message to the RPi server. """

    # ip, port = '192.168.2.69', 9118
    ip, port = '127.0.0.1', 9118

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data
    s.send(msg.encode())

    # receive the response
    response = s.recv(24)
    return response

# # Receive a response
# response = s.recv(len_sent)
# print('Received: {!r}'.format(response))
