
# from config import *
from leawood.lwmqtt import Subscriber
from leawood.config import Config
import sys

config = Config(sys.argv[1:])
log = config.getLogger("subscribe_and_post")


if __name__ == "__main__":

    try:
        with Subscriber(config) as mqtt:
            mqtt.loop_forever()
    except KeyboardInterrupt:
        log.info(f'Keyboard interrupt shutting down')
        
