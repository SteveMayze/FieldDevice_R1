
# from config import *
import os
import paho.mqtt.client as mqtt
# import logging
import json
from json import JSONEncoder
import requests
from requests.auth import HTTPBasicAuth
import leawood.config


config = leawood.config.Config()
log = config.getLogger("subscribe_and_post")

def httpGet(resource, query):
    ## Get the device details
    payload={}
    base_url = config.config_data['rest']
    headers = { f'Authorization': 'Basic {url_auth}'}
    if not query:
        url = f'{base_url}/{resource}'
    else:
        url = f'{base_url}/{resource}?q={query}'
    log.info (f'GET {url}\n  query: {query}')
    response =  requests.request("GET", url, headers=headers, data=payload, timeout=30, auth=HTTPBasicAuth(config.config_data['username'], config.config_data['password']))
    return response.json()['items'][0]

def httpPost(resource, payload):
    ## Get the device details
    base_url = config.config_data['rest']
    headers = {
        'Content-Type': 'application/json',
       ## f'Authorization': 'Basic {url_auth}'
    }
    url = f'{base_url}/{resource}'
    log.info (f'POST {url}\n   payload: {payload}\n user {config.config_data["username"]}, pwd: {config.config_data["password"]}')
    return requests.request("POST", url, headers=headers, data=payload, timeout=30, auth=HTTPBasicAuth(config.config_data['username'], config.config_data['password']))

def on_connect(client, userdata, flags, rc):
    log.info(f'Result from connect: {mqtt.connack_string(rc)}')
    # Subscribe to the power/sensor/+/data
    client.subscribe('power/sensor/+/data', qos=2)

def on_subscribe(client, userdata, mid, granted_qos):
     log.info(f'I have subscribed with QoS {granted_qos[0]}')

def on_message(client, userdata, msg):
    log.info(f'Message received. Topic: {msg.topic}, payload {str(msg.payload)}')
    qData = json.loads(msg.payload);
    response = httpPost("data_points", JSONEncoder().encode(qData).encode("utf-8"))
    log.info(f'Response: {response.status_code}')
    if response.status_code != 200:
        log.error(f' ERROR {response.text}')


if __name__ == "__main__":
    # log.basicConfig( level=log.INFO)

    # log.info("Starting")
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.tls_set(
        ca_certs = os.path.join(config.config_data['certpath'], config.config_data['cacert']), 
        certfile= os.path.join(config.config_data['certpath'], config.config_data['clientcrt']), 
        keyfile= os.path.join(config.config_data['certpath'], config.config_data['clientkey'])
        )
    log.info("Connecting")
    client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
    log.info("Going into wait state...")
    client.loop_forever()

