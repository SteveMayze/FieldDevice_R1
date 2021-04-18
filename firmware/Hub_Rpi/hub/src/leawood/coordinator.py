

class AbstractCoordinator:

    def __init__(self, config, name):
        self.config = config
        self.log = config.getLogger(name)
