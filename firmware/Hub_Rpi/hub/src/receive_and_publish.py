from leawood.config import Config
import json
import os
import paho.mqtt.client as mqtt
from leawood.lwmqtt import LW_MQTT

config = Config()
log = config.getLogger("receive_and_publish")




if __name__ == "__main__":

    payload = {}
    with open(config.config_data['file']) as f:
        payload = json.load(f)
    log.info(f"Publishing {payload}")

    with LW_MQTT(config) as mqtt:
        mqtt.publish (
            topic = config.publish_topic,
            payload = json.dumps(payload)
        )



