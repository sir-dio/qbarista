# Hardware Setup

The Quiz Barista is designed to be used with a **Raspberry Pi Zero W**.  
This file contains the description of the process of setting up the Pi to work with
the app.

### Setting up the Ethernet over USB
1. Flash the Pi's microSD card with a Raspbian Stretch Lite image.
2. In the `boot` partition of the newly flashed card, edit the `config.txt` file by
appending `dtoverlay=dwc2` at the end.
3. in the `cmdline.txt` file, after the `rootwait` and before anything else
*(there will be something else only if the Pi was never booted before)* insert
`modules-load=dwc2,g_ether`. This file is very picky, so it’s important that the
format is correct — the inserted command has to be separated from other ones only by
a single space on each side. 
4.  Enable SSH by creating an empty file called `ssh`.

### Setting static IP addresses
Static IPs will help manage the connections to the Pi.

To SSH into the Pi for the first time, the `ssh pi@raspberrypi.local` command can be used.
After that I personally prefer to change the hostname of the device, so there is no
conflicts with other Raspberry Pis. 

To set static IP address for the `usb0` interface, modify the `/etc/dhcpcd.conf`
file to include the following:
```
interface usb0
	static ip_address=192.168.2.69
	static ip6_address=fe80::8d97:da30:f5f5:fc2a
	static gateway=192.168.2.1
	static domain_name_servers=8.8.8.8
	nohook wpa_supplicant
```
The static gateway is the IP address that the main computer needs to use for RPi to
connect to it successfully. It means that the interface might need to be manually setup
to use this address.
