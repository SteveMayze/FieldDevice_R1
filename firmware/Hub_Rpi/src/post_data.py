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


query = { "serial_id": {"$eq":"0013A20041629BFB"}}
data = httpGet("devices", JSONEncoder().encode(query))
deviceId = data['device_id']
print (f'Device ID: {deviceId}')

# Get the data definitions

query = { "label": {"$eq":"bus-voltage"}}
data = httpGet("data_definitions",  JSONEncoder().encode(query))
busVoltageId = data['def_id']
print (f'Bus Voltage: {busVoltageId}')

query = { "label": {"$eq":"load-current"}}
data = httpGet("data_definitions",  JSONEncoder().encode(query))
loadCurrentId = data['def_id']
print (f'Load Current: {loadCurrentId}')



## POST the data
while True:

    value = random.random() * 6
    value = value + 11
    
    factor = 1000.0
    value =  math.trunc(value * factor) / factor

    payload = {
        "device_id": deviceId,
        "data_def_id": busVoltageId,
        "data_value": value
    }
    # payload=f'{{"device_id": "{deviceId}","data_def_id": "{busVoltageId}","data_value": {value}}}'
    response = httpPost("data_points", JSONEncoder().encode(payload))

    payload = {
        "device_id": deviceId,
        "data_def_id": loadCurrentId,
        "data_value": value
    }
    # payload=f'{{"device_id": "{deviceId}","data_def_id": "{loadCurrentId}","data_value": {value}}}'
    response = httpPost("data_points", JSONEncoder().encode(payload))

    time.sleep(20)

