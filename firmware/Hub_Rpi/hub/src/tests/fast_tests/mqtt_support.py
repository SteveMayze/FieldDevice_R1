


from leawood.lwmqtt import Publisher

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






