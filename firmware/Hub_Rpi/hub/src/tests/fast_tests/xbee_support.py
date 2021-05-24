
from leawood.config import Config
from leawood.xbee import Coordinator
from leawood.xbee import Sensor
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

    def __init__(self, config, publisher):
        Coordinator.__init__(self, config, publisher )
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


    def data_receive_callback(self, xbee_message):
        self.publisher.publish(self.config.publish_topic, xbee_message)

    def register_listeners(self, data_recevie_callback):
        pass

    def __str__(self):
        return 'FakeCoordinator'


class FakeSensingDevice(XBeeDevice):
    def __init__(self, com, baud):
        XBeeDevice.__init__(self, com, baud)
        self.spy = {}
        self.log.info('FakeSensingDevice: __init__')

    def __str__(self):
        return 'FakeSensingDevice'


class FakeSensor(Sensor):
    def __init__(self, config):
        Sensor.__init__(self, config )
        com = config.config_data['serial-port']
        baud = int(config.config_data['serial-baud'])
        self.sensing_device = FakeSensingDevice(com, baud)
        self.log.info('FakeSensor: __init__')

    def _send_data(self, address, payload):
        self.sensing_device.spy[address] = payload

    def __str__(self):
        return 'FakeSensor'
