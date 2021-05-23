
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import XBeeDevice
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

        self._messages = []

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, message):
        self._messages.append(message)

    def _scan_network(self):
        device = json.loads(f'{{"NI": "GREEN", "PL": "PowerLevel.High", "ADDRESS": "00000001", "ADDR": "0001"}}')
        device['device-id'] = 'NOT-SET'
        self.add_node(device)

    def _request_data(self):
        self.coordinating_device.spy['COORDINATOR'] = 'DATA_REQ'


    def data_receive_callback(self, xbee_message):
        self.messages = xbee_message

    def register_listeners(self, data_recevie_callback):
        pass

    def __str__(self):
        return 'FakeCoordinator'

