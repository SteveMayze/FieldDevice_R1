
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


class TestBasic:
    
    ## The gateway client starts up and activates the receiver which 
    ## monitors the XBee radio for any incomming messages and posts
    ## them immediatly to the MQTT server.

    ## The problem here when devising tests for this is that 
    ##      1. There is no actual user interaction
    ##      2. The actual logic is quite simple but the problem 
    ##         is with the dependent resouces.


    def test_receiver_is_started(self, config):
        receiver = Receiver(config)
        receiver.start()

        ## What to test for on the startup of the reciever?
        ##      1. The initialisation of the XBee module
        ##      2. That this does not block but there is also
        ##         a running thread.
        ##
        ## Here we need to mock the actual XBee code and or provide spies.

    ## The receiver is also a coordinator and so should send out some
    ## messages on start up - such as
    ##      1. Discover Network
    ##      2. Collect the details of the network
    ##      3. Issue a message for each device and request the data
    ##          3.1 The request for data can be at two levels
    ##              - What information will you send i.e. Domain, Class, label, data type
    ##              - THe readings of the sensors and the values.
