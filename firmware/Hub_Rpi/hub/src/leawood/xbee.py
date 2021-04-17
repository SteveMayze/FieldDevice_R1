
from  digi.xbee import devices
from  leawood.coordinator import AbstractCoordinator

import time
import json

class XBEE:
    def __init__(self):
        pass
"""
The XBee module/classes provides an API wrapper around the 
"""
class Coordinator(AbstractCoordinator):

    def __init__(self, config):
        super(Coordinator, self).__init__(config, "XBee_Coordinator")

    ## =======================================================================
    ## =======================================================================
    def scan_network(self):
        self.nodes = []
        config = self.config
        self.log.info('setting up the configuration of the XBee device')
        com = config.config_data['serial-port']
        baud = int(config.config_data['serial-baud'])

        self.device = devices.XBeeDevice(com, baud)
        self.device.open()
        xnet = self.device.get_network()
        xnet.start_discovery_process(deep=True, n_deep_scans=1)
        self.log.info('Discovering the network')
        while xnet.is_discovery_running():
            time.sleep(0.5)

        # Get the list of the nodes in the network.
        nodes = xnet.get_devices()
        self.log.info(f'Retrieved the nodes {nodes}')

        for node in nodes:
            device = json.loads(f'{{"NI": "{node.get_node_id()}", "PL": "{node.get_power_level()}", "ADDRESS": "{node.get_64bit_addr()}", "ADDR": "{node.get_16bit_addr()}"}}')
            device['device-id'] = 'NOT-SET'
            self.nodes.append(device)

        self.log.info (f'Network: {self.nodes}')


    def close(self):
        self.device.close()

