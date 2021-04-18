
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import AbstractXBeeDevice
from digi.xbee.devices import XBeeNetwork
import pytest
import json

@pytest.fixture
def config():
    args = ["--serial-port", "COM1", "--baud", "9600"]
    return Config(args)


class MockXBeeDevice(AbstractXBeeDevice):

    spy = {}

    def open(self):
        pass

    def get_network(self):
        return MockXBeeNetwork(self)

    def get_node_id(self):
        return self._node_id

    def get_power_level(self):
        return self._power_level
    
    def get_64bit_addr(self):
        return self._64bit_addr

    def get_16bit_addr(self):
        return self._16bit_addr

    def send_data(self, remote_device, command):
        self.log.info(f'COORDINATOR: {self}')
        self.spy['COORDINATOR'] = command

    
class MockXBeeNetwork(XBeeNetwork):
    def start_discovery_process(self, *args, **kwargs):
        return object()        

    def is_discovery_running(self):
        return False

    def get_devices(self):
        device = MockXBeeDevice('COM1', 9600)
        device._node_id = 'GREEN'
        device._64bit_addr = '00000001'
        device._16bit_addr = '0001'
        device._power_level = 100
        self.nodes = []
        self.nodes.append(device)
        return self.nodes


class TestCase:

    @patch('leawood.xbee.devices')
    def test_coordinator_scan_network(self, xbee_mock, config):
        xbee_mock.XBeeDevice = MockXBeeDevice
        coordinator = Coordinator(config)
        coordinator.scan_network()

        devices = coordinator.nodes
        device = devices[0]
        assert 'GREEN' == device['NI']


    @patch('leawood.xbee.devices')
    def test_coordinator_can_request_data(self, xbee_mock, config):
        xbee_mock.XBeeDevice = MockXBeeDevice
        coordinator = Coordinator(config)
        coordinator.nodes = []
        device = json.loads(f'{{"NI": "GREEN", "PL": "FF", "ADDRESS": "00000001", "ADDR": "0001"}}')
        device['device-id'] = 'NOT-SET'
        coordinator.nodes.append(device)

        coordinator.request_data()
        # assert node_data[0]['voltage'] == 10.6
        assert coordinator.coordinating_device.spy["COORDINATOR"] == 'DATA_REQ'



