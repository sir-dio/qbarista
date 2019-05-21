""" qBarista: tasty web-served seismic tests.

This file defines the startup sequence for the RPi.
This is the target for the cronjob that runs on Pi's reboot.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from network import server

if __name__ == '__main__':
    server.run()
