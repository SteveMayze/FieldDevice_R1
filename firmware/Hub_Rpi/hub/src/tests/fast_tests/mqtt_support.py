


from leawood.lwmqtt import Publisher, Subscriber
import paho.mqtt.client as mqtt

class FakePublisher(Publisher):

    
    def __init__(self, config):
        ## Publisher.__init__(self, config)
        self._publish_queue = {}
        self.config = config
        self.log = config.getLogger("lwmqtt.FakePublisher")

    @property
    def publish_queue(self):
        return self._publish_queue

    @publish_queue.setter
    def publish_queue(self, value):
        self.publish_queue = value

    def publish(self, topic, payload):
        config = self.config
        self.log.info(f"Publishing")
        if not (topic in self.publish_queue) or [topic] == None:
            self.publish_queue[topic] = []

        self.publish_queue[topic].append(payload)


class FakeSubscriber(Subscriber):
    def __init__(self, config):
        self._subscribe_queue = {}
        self.config = config
        self.log = config.getLogger('FakeSubscriber')

    @property
    def subscribe_queue(self):
        return self._subscribe_queue

    @subscribe_queue.setter
    def subscribe_queue(self, value):
        self._subscribe_queue = value

    def set_on_connect_callback(self, on_connect):
        pass

    def set_on_subscribe_callback(self, on_subscribe):
        pass
    
    def set_on_message_callback(self, on_message):
        pass


    def start(self):
        pass

    
