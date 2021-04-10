from leawood.config import Config
from leawood.lwmqtt import Publisher
import json
import sys

config = Config(sys.argv[1:])
log = config.getLogger("receive_and_publish")


if __name__ == "__main__":

    payload = {}
    with open(config.config_data['file']) as f:
        payload = json.load(f)
    log.info(f"Publishing {payload}")

    with Publisher(config) as mqtt:
        mqtt.publish (
            topic = config.publish_topic,
            payload = json.dumps(payload)
        )
