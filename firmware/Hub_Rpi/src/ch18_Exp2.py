# Chapter 18 Exercise 2

from digi.xbee.devices import XBeeDevice
import time

# Definitions - Serial Input function, preset the number of modules.

# GPIO 5, 6, 13
# 3V3 17, GND 25
# Serial DOUT 8, DIN 10

xbee = XBeeDevice("COM4", 9600)

xbee.open()

# Wait for Ground on Test PIN

# Transmit API packet "ND"
xnet = xbee.get_network()
# For each expected module:
    # Wait for 0xFE
    # for each byte received
        # Get message-byte-count bytes - Calculate the byte count
        # Get message data byte - Save byte in dataND array - add checksum bytes
    # End for
    # if checksum not OK
        # Error - Throw exception
# End For
xnet.start_discovery_process()          
while xnet.is_discovery_running():
    time.sleep(0.5)

nodes = xnet.get_devices()

for node in nodes:
    print(f'NI: {node.get_node_id()}, Power level: {node.get_power_level()}, SH/SL: {node.get_64bit_addr()}, MY: {node.get_16bit_addr()}')

# Done LED on - Print XBee data
xbee.close()
