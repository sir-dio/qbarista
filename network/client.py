""" qBarista: tasty web-served seismic quizzes.

This file defines the socket-client that is used on the main computer to
control the Raspberry Pi.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import socket


def send(msg, host='alex-pi.local', port=9118):
    """ Sends the message to the RPi server. """

    # Connect to the server
    s = socket.create_connection((host, port))

    # Send the data and get the response
    s.send(msg.encode())
    response = s.recv(36)

    return response.decode()


def test_connection(host='alex-pi.local', port=9118, timeout=2):
    """ Test if the Pi is connected. """

    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except OSError:
        return False
