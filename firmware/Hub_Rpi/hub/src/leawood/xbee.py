
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

    coordinating_device = None

    def __init__(self, config):
        super(Coordinator, self).__init__(config, "XBee_Coordinator")


    def __get_coordinator_device(self):
        if self.coordinating_device == None:
            config = self.config
            self.log.info('setting up the configuration of the XBee device')
            com = config.config_data['serial-port']
            baud = int(config.config_data['serial-baud'])
            self.coordinating_device = devices.XBeeDevice(com, baud)
            self.log.info(f"Created Coordinating device {self.coordinating_device}")
        return self.coordinating_device

    """
    Broadcases a request to locate any neighboring nodes.
    """
    def scan_network(self):
        self.nodes = []
        coordinator = self.__get_coordinator_device()
        self.log.info(f'Located the coordinator: {coordinator}')
        coordinator.open()
        xnet = coordinator.get_network()
        xnet.start_discovery_process(deep=True, n_deep_scans=1)
        self.log.info(f'Discovering the network: {xnet}')
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

    """
    Executes on receipt of messages to the coordinator.
    """
    def data_receive_callback(self):
        self.log.info('BEGIN')
        self.log.info('END')
        pass

    """
    Registers the call back to the coordinator.
    """
    def start_receiver(self):
        self.log.info('BEGIN')
        self.log.info('END')
        pass
        

    """
    Cycles through the list of devices and requests from each one if they have any data.
    """
    def request_data(self):
        coordinator_device = self.__get_coordinator_device()
        self.log.info(f'Located the coordinator: {coordinator_device}')
        coordinator_device.open()

        for remote in self.nodes:
            remote_device = devices.RemoteXbeeDevice(coordinator_device, devices.XBee64BitAddress(remote['ADDRESS']))
            self.log.info(f'Sending a DATA_REQ to {remote_device}')
            coordinator_device.send_data(remote_device, 'DATA_REQ')
            # remote_device.send_data_async(remove_device, 'DATA_REQ')


    """
    Closes the connection to the coordinator.
    """
    def close(self):
        self.coordinating_device.close()

