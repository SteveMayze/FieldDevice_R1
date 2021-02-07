# Chapter 18 Exercise 2

from digi.xbee.devices import XBeeDevice
from json import JSONEncoder

import time
import json
import requests

base_url = "https://b0o5r0vxkz5ekbo-db202011271753.adb.eu-frankfurt-1.oraclecloudapps.com/ords/leawood_dev/api/1.0"

def httpGet(resource, query):
    ## Get the device details
    payload={}
    headers = { 'Authorization': 'Basic UkVTVF9VU0VSOlk4YzhVcTcyWjFEcg=='}
    if not query:
        url = f'{base_url}/{resource}'
    else:
        url = f'{base_url}/{resource}?q={query}'
    print (f'GET {url}\n  query: {query}')
    response =  requests.request("GET", url, headers=headers, data=payload, timeout=30)
    return response.json()['items'][0]

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

devices = []
for node in nodes:
    device = json.loads(f'{{"NI": "{node.get_node_id()}", "PL": "{node.get_power_level()}", "ADDRESS": "{node.get_64bit_addr()}", "ADDR": "{node.get_16bit_addr()}"}}')
    query = { "serial_id": {"$eq":device["ADDRESS"]}}
    data = httpGet("devices", JSONEncoder().encode(query))
    deviceId = data['device_id']
    if deviceId:
        device["device-id"] = data['device_id']
        devices.append(device)


# Done LED on - Print XBee data
xbee.close()


print(f'devices: {devices}')

# At this point we have an array of devices on the network and they have been reconciled back
# at the database. There is the question of registering a new device if it has not been
# found.

# The issue that I have when attempting to create when not existing is the additional information
# such as the name of the device the properties that it is expected to deliver i.e. unit,
# multiplier and symbol etc.

for device in devices:
    xbee.open()
    
    xbee.close()