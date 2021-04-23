
from  digi.xbee import devices
from digi.xbee.exception import XBeeException
from  leawood.coordinator import AbstractCoordinator

import time
import json

"""
Broadcases a request to locate any neighboring nodes.
"""
def scan_network(coordinator):
    try:
        coordinator._scan_network()
        return "OK"
    except XBeeException:
        return "EXCEPTION"




"""
Cycles through the list of devices and requests from each one if they have any data.
"""
def request_data(coordinator):
    try:
        coordinator._request_data()
        return "OK"
    except XBeeException as e:
        return f"EXCEPTION: {type(e)}, {e.args}, {e}"


"""
The XBee module/classes provides an API wrapper around the 
"""
class Coordinator(AbstractCoordinator):


    def __init__(self, config):
        super(Coordinator, self).__init__(config, "XBee_Coordinator")
        self._coordinating_device = None

        self.log.info('XBee_Coordinator: __init__')



    @property
    def coordinating_device(self):
        if ( self._coordinating_device == None):
            com = self.config.config_data['serial-port']
            baud = int(self.config.config_data['serial-baud'])
            self.coordinating_device = devices.XBeeDevice(com, baud)
        return self._coordinating_device

    @coordinating_device.setter
    def coordinating_device(self, device):
            self._coordinating_device = device
            self.log.info(f"Created Coordinating device {self._coordinating_device}")

    """
    Broadcases a request to locate any neighboring nodes.
    """
    def _scan_network(self):
        coordinator = self.coordinating_device
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
            self._nodes.append(device)

        self.log.info (f'Network: {self._nodes}')


    def __str__(self):
        return f'Coordinator'


    """
    Cycles through the list of devices and requests from each one if they have any data.
    """
    def _request_data(self):
        coordinator_device = self.coordinating_device
        self.log.info(f'Located the coordinator: {coordinator_device.get_node_id()}')
        coordinator_device.open()

        for remote in self.nodes:
            self.log.info(f'Sending a data request to {remote["ADDRESS"]}')
            remote_device = devices.RemoteXBeeDevice(coordinator_device, devices.XBee64BitAddress.from_hex_string(remote['ADDRESS']))
            self.log.info(f'Sending a DATA_REQ to {remote_device}')
            ## coordinator_device.send_data(remote_device, 'DATA_REQ')
            coordinator_device.send_data_broadcast( 'DATA_REQ')
            # remote_device.send_data_async(remove_device, 'DATA_REQ')


    """
    Closes the connection to the coordinator.
    """
    def close(self):
        self.coordinating_device.close()


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

    