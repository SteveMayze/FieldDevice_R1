
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import XBeeException
import pytest
import json
import leawood.xbee
import tests.xbee_support

@pytest.fixture
def config():
    args = ["--serial-port", "COM1", "--baud", "9600"]
    return Config(args)



class TestCase:

    def test_coordinator_scan_network(self, config):
        coordinator = tests.xbee_support.FakeCoordinator(config)
        status = leawood.xbee.scan_network(coordinator)
        assert "OK" == status

        devices = coordinator.nodes
        device = devices[0]
        assert 'GREEN' == device['NI']


    def test_coordinator_can_request_data(self, config):
        coordinator = tests.xbee_support.FakeCoordinator(config)
        device = json.loads(f'{{"NI": "GREEN", "PL": "FF", "ADDRESS": "00000001", "ADDR": "0001"}}')
        device['device-id'] = 'NOT-SET'
        coordinator.add_node(device)

        status = leawood.xbee.request_data(coordinator)
        assert "OK" == status

        # assert node_data[0]['voltage'] == 10.6
        assert coordinator.coordinating_device.spy["COORDINATOR"] == 'DATA_REQ'


    """
    Defines its own coordinator to throw an un qualified XBee Exception.
    """
    def test_xbee_exception_returns_failed(self, config):
        ## A local fake coordinator just to throw an exception
        class BrokenCoordinator(tests.xbee_support.FakeCoordinator):
            def __init__(self, config):
                tests.xbee_support.FakeCoordinator.__init__(self, config )
                self.log.info('BrokenCoordinator: __init__')

            def _scan_network(self):
                raise XBeeException()

        ## TODO - Further possibilities are here to examine the type
        ##        of exception and produce a better response and handling
        ##        i.e. logging the issues back to the base.
        coordinator = BrokenCoordinator(config)
        status = leawood.xbee.scan_network(coordinator)
        assert "EXCEPTION" == status


