import paho.mqtt.client as mqtt
from leawood.config import Config
import json
import os
import logging

import requests
from json import JSONEncoder




class LW_MQTT:

    def __init__(self, config):
        self.config = config
        self.log = config.getLogger("mqtt")
        self.client = mqtt.Client(protocol=mqtt.MQTTv311)

        self.client.tls_set(
            ca_certs = os.path.join(config.config_data['certpath'], config.config_data['cacert']), 
            certfile= os.path.join(config.config_data['certpath'], config.config_data['clientcrt']), 
            keyfile= os.path.join(config.config_data['certpath'], config.config_data['clientkey'])
            )

 

    def publish(self, topic, payload):
        config = self.config
        self.log.info("Connecting")
        self.client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
        self.log.info(f"Publishing {payload}")
        self.client.publish(
            topic = LW_MQT.config.publish_topic,
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
