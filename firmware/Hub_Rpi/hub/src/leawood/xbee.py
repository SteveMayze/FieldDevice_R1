
# from digi.xbee.devices import XBeeDevice
# from digi.xbee.devices import XBeeNetwork
from  digi.xbee import devices

import time

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

        device = devices.XBeeDevice(com, baud)
        device.open()
        xnet = device.get_network()
        xnet.start_discovery_process(deep=True, n_deep_scans=1)
        while xnet.is_discovery_running():
            time.sleep(0.5)

        # Get the list of the nodes in the network.
        nodes = xnet.get_devices()

