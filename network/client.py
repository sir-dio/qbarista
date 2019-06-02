""" qBarista: tasty web-served seismic tests.

This file defines the socket-client that is used on the main computer to
control the Raspberry Pi.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import socket


def send(msg):
    """ Sends the message to the RPi server. """

    ip, port = '192.168.2.69', 9118

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data and get the response
    s.send(msg.encode())
    response = s.recv(36)

    return response.decode()


def test_connection():
    """ Test if the Pi is connected. """

    ip, port = '192.168.2.69', 9118

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))
        return True
    except ConnectionRefusedError:
        return False
