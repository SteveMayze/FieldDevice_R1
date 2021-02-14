from leawood.config import Config
import json
import os
import paho.mqtt.client as mqtt

config = Config()
log = config.getLogger("receive_and_publish")




if __name__ == "__main__":

    payload = {}
    with open(config.config_data['file']) as f:
        payload = json.load(f)
    
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.tls_set(
        ca_certs = os.path.join(config.config_data['certpath'], config.config_data['cacert']), 
        certfile= os.path.join(config.config_data['certpath'], config.config_data['clientcrt']), 
        keyfile= os.path.join(config.config_data['certpath'], config.config_data['clientkey'])
        )
    log.info("Connecting")
    client.connect( host=config.config_data['mqttserver'], port=int(config.config_data['mqttport']), keepalive = 60)
    log.info(f"Publishing {payload}")
    client.publish(
        topic = config.publish_topic,
        payload = json.dumps(payload)
    )


