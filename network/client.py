""" qBarista: tasty web-served seismic quizzes.

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
    s = socket.create_connection((ip, port))

    # Send the data and get the response
    s.send(msg.encode())
    response = s.recv(36)

    return response.decode()


def test_connection(timeout=2):
    """ Test if the Pi is connected. """

    ip, port = '192.168.2.69', 9118

    try:
        socket.create_connection((ip, port), timeout=timeout)
        return True
    except OSError:
        return False
