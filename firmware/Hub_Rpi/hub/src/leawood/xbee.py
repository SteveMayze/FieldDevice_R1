
from digi.xbee.devices import XBeeDevice

class XBEE:
    def __init__(self):
        pass

class Receiver:
    def __init__(self, config):
        self.config = config
        self.log = config.getLogger("Receiver")

    def start(self):
        config = self.config
        com = config.config_data['serial-port']
        baud = int(config.config_data['serial-baud'])
        device = XBeeDevice(com, baud)
        device.open()