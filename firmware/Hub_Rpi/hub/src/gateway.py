from leawood.config import Config
from leawood.lwmqtt import Publisher
from leawood.lwmqtt import Subscriber
import time
import json

config = Config()
log = config.getLogger("gateway")


if __name__ == "__main__":

    subscriber = Subscriber(config)
    subscriber.start()        

    try:
        payload = {}
        with open(config.config_data['file']) as f:
            payload = json.load(f)
        log.info(f"Publishing {payload}")

        publisher = Publisher(config)
        publisher.publish(
                topic = config.publish_topic,
                payload = json.dumps(payload)
        )

    except KeyboardInterrupt:
        log.info(f'KeyboardInterrupt - Shutting down')
    else:
        log.info(f'Shutting down')
        subscriber.stop()

