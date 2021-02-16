import paho.mqtt.client as mqtt
from leawood.config import Config
from leawood.lwrest import Rest
import json
import os
import logging

from json import JSONEncoder

def on_connect(client, userdata, flags, rc):
    userdata.log.info(f'Result from connect: {mqtt.connack_string(rc)}')
    # Subscribe to the power/sensor/+/data
    client.subscribe(userdata.config.subscribe_topic, qos=2)

def on_subscribe(client, userdata, mid, granted_qos):
     userdata.log.info(f'I have subscribed with QoS {granted_qos[0]}')

def on_message(client, userdata, msg):
    userdata.log.info(f'Message received. Topic: {msg.topic}, payload {str(msg.payload)}')
    qData = json.loads(msg.payload);
    rest = Rest(userdata.config)
    response = rest.post("data_points", JSONEncoder().encode(qData).encode("utf-8"))
    userdata.log.info(f'Response: {response.status_code}')
    if response.status_code != 200:
        userdata.log.error(f' ERROR {response.text}')

##
## Subscriber
class Subscriber:
    def __init__(self, config):
        self.config = config
        self.log = config.getLogger('lwmqtt.Subscriber')
        self.client = mqtt.Client(protocol=mqtt.MQTTv311, userdata=self)
        self.client.on_connect = on_connect
        self.client.on_subscribe = on_subscribe
        self.client.on_message = on_message
        self.client.tls_set(
            ca_certs = os.path.join(config.config_data['certpath'], config.config_data['cacert']), 
            certfile = os.path.join(config.config_data['certpath'], config.config_data['clientcrt']), 
            keyfile  = os.path.join(config.config_data['certpath'], config.config_data['clientkey'])
            )


    def __enter__(self): 
        config = self.config
        self.log.info("Connecting")
        self.client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
        return self.client
  
    def __exit__(self, exc_type, exc_value, traceback):
        # self.log.info(f'exec_type: {exec_type}, exec_value: {exec_value}, traceback: {traceback}') 
        self.log.info("Disconnecting")
        self.client.disconnect



##
## Publisher
class Publisher:
    def __init__(self, config):
        self.config = config
        self.log = config.getLogger("lwmqtt.Publisher")
        self.client = mqtt.Client(protocol=mqtt.MQTTv311, userdata=self)
        self.client.tls_set(
            ca_certs = os.path.join(config.config_data['certpath'], config.config_data['cacert']), 
            certfile = os.path.join(config.config_data['certpath'], config.config_data['clientcrt']), 
            keyfile  = os.path.join(config.config_data['certpath'], config.config_data['clientkey'])
            )

    def __enter__(self): 
        config = self.config
        self.log.info("Connecting")
        self.client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
        return self.client
  
    def __exit__(self, exc_type, exc_value, traceback):
        # self.log.info(f'exec_type: {exec_type}, exec_value: {exec_value}, traceback: {traceback}') 
        self.log.info("Disconnecting")
        self.client.disconnect

 

    def publish(self, topic, payload):
        config = self.config
        self.log.info("Connecting")
        self.client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
        self.log.info(f"Publishing {payload}")
        self.client.publish(
            topic = self.config.publish_topic,
            payload = json.dumps(payload)
        )
        self.client.disconnect


    def __enter__(self): 
        config = self.config
        self.log.info("Connecting")
        self.client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
        return self.client
  
    def __exit__(self, exc_type, exc_value, traceback):
        # self.log.info(f'exec_type: {exec_type}, exec_value: {exec_value}, traceback: {traceback}') 
        self.log.info("Disconnecting")
        self.client.disconnect
