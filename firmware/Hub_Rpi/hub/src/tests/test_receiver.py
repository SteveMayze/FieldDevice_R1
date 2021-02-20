
from leawood.config import Config
from leawood.xbee import Receiver
from unittest.mock import patch
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeNetwork
import pytest

@pytest.fixture
def config():
    args = ["--serial-port", "COM1", "--baud", "9600"]
    return Config(args)

class MockXBeeNetwork(XBeeNetwork):
    def start_discovery_process(self, *args, **kwargs):
        return object()        

    def is_discovery_running(self):
        return False

class MockXBeeDevice(XBeeDevice):
    def open(self):
        pass

    def get_network(self):
        return MockXBeeNetwork(self)


class TestCase:

    @patch('leawood.xbee.devices')
    def test_receiver_start(self, xbee_mock, config):
        xbee_mock.XBeeDevice = MockXBeeDevice
        receiver = Receiver(config)
        receiver.start()
