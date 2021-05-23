


from leawood.lwmqtt import Publisher

class FakePublisher(Publisher):

    publish_queue = []
    
    def __init__(self, config):
        ## Publisher.__init__(self, config)
        pass

    def publish(self, topic, payload):
        config = self.config
        self.log.info(f"Publishing")
        self.publish_queue[topic] = payload






