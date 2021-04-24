
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeException
import pytest
import json
import leawood.xbee

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

