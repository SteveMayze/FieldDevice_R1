
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeNetwork
import pytest
import os

@pytest.fixture
def config():
    port = os.environ.get('XBEE_PORT')
    assert port != None

    args = ["--serial-port", port, "--baud", "9600"]
    return Config(args)

@pytest.fixture
def initialised_coordinator(config):
    coordinator = Coordinator(config)
    yield coordinator
    coordinator.close()


class TestBasic:
    
    ## The gateway client starts up and activates the receiver which 
    ## monitors the XBee radio for any incomming messages and posts
    ## them immediatly to the MQTT server.

    ## The problem here when devising tests for this is that 
    ##      1. There is no actual user interaction
    ##      2. The actual logic is quite simple but the problem 
    ##         is with the dependent resouces.

    ## Chatting with HP one approach would be to plug a device in.
    ## After all, it is an functional/integration test!
    ## 11.04.21 - This has then initial code able to return OK.


    def test_receiver_can_scan_network(self, initialised_coordinator):
        coordinator = initialised_coordinator
        coordinator.scan_network()

        devices = coordinator.nodes
        device = devices[0]
        assert 'GREEN' == device['NI']


    ## The coordinator should send out some
    ## messages on start up - such as
    ##      1. Discover Network
    ##      2. Collect the details of the network
    ##      3. Issue a message for each device and request the data
    ##          3.1 The request for data can be at two levels
    ##              - What information will you send i.e. Domain, Class, label, data type
    ##              - THe readings of the sensors and the values.
