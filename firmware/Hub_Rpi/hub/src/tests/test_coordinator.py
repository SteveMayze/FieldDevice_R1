
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import AbstractXBeeDevice
from digi.xbee.devices import XBeeNetwork
from digi.xbee.devices import XBeeDevice
import pytest
import json
import leawood.xbee

@pytest.fixture
def config():
    args = ["--serial-port", "COM1", "--baud", "9600"]
    return Config(args)

class FakeCoordinatingDevice(XBeeDevice):
    def __init__(self, com, baud):
        XBeeDevice.__init__(self, com, baud)
        self.spy = {}
        self.log.info('FakeCoordinatingDevice: __init__')

    def __str__(self):
        return 'FakeCoordinatingDevice'


class FakeCoordinator(Coordinator):
    def __init__(self, config):
        Coordinator.__init__(self, config )
        com = config.config_data['serial-port']
        baud = int(config.config_data['serial-baud'])
        self.coordinating_device = FakeCoordinatingDevice(com, baud)
        self.log.info('FakeCoordinator: __init__')

    def _scan_network(self):
        device = json.loads(f'{{"NI": "GREEN", "PL": "PowerLevel.High", "ADDRESS": "00000001", "ADDR": "0001"}}')
        device['device-id'] = 'NOT-SET'
        self.add_node(device)

    def _request_data(self):
        self.coordinating_device.spy['COORDINATOR'] = 'DATA_REQ'

    def __str__(self):
        return 'FakeCoordinator'



class TestCase:

    def test_coordinator_scan_network(self, config):
        coordinator = FakeCoordinator(config)
        leawood.xbee.scan_network(coordinator)

        devices = coordinator.nodes
        device = devices[0]
        assert 'GREEN' == device['NI']


    def test_coordinator_can_request_data(self, config):
        coordinator = FakeCoordinator(config)
        device = json.loads(f'{{"NI": "GREEN", "PL": "FF", "ADDRESS": "00000001", "ADDR": "0001"}}')
        device['device-id'] = 'NOT-SET'
        coordinator.add_node(device)

        leawood.xbee.request_data(coordinator)
        # assert node_data[0]['voltage'] == 10.6
        assert coordinator.coordinating_device.spy["COORDINATOR"] == 'DATA_REQ'



