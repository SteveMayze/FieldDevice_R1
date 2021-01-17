import requests
import random
import time
import math
import json
from json import JSONEncoder


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



def httpPost(resource, payload):
    ## Get the device details
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic UkVTVF9VU0VSOlk4YzhVcTcyWjFEcg=='
    }
    url = f'{base_url}/{resource}'
    print (f'POST {url}\n   payload: {payload}')
    return requests.request("POST", url, headers=headers, data=payload, timeout=30)


## Get the device details
query = { "serial_id": {"$eq":"0013A20041AE49D4"}}
data = httpGet("devices", JSONEncoder().encode(query))
deviceId = data['device_id']
print (f'Device ID: {deviceId}')

# Get the data definitions
query = { "label": {"$eq":"water-level"}}
data = httpGet("data_definitions", JSONEncoder().encode(query))
waterLevelId = data['def_id']
print (f'Water level: {waterLevelId}')

## POST the data
value = 30
direction = "up"
while True:

    if direction == "up":
        value = value + 5
    else: 
        value = value -5

    if value > 80:
        direction = "down"
    if value < 30:
        direction = "up"

    payload = {
        "device_id": deviceId,
        "data_def_id": waterLevelId,
        "data_value": value
    }
    response = httpPost("data_points", JSONEncoder().encode(payload))
    time.sleep(20)

