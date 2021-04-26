
from leawood.config import Config
from leawood.xbee import Coordinator
from unittest.mock import patch
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import XBeeNetwork
import pytest
import os
import leawood.xbee
import time

import functional_tests.conftest



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

    """
    Peroforms a basic test on the ability for the coordinator to scan the
    netowrk for other devices.

    The coordinator fixure is defined in the conftest.py 
    """

    def test_coordinator_can_scan_network(self, coordinator):
        status = leawood.xbee.scan_network(coordinator)
        assert "OK" == status

        devices = coordinator.nodes
        device = devices[0]
        assert 'RED' == coordinator.coordinating_device.get_node_id()
        assert 'GREEN' == device['NI']


    ## The coordinator should send out some
    ## messages on start up - such as
    ##      1. Discover Network
    ##      2. Collect the details of the network
    ##      3. Issue a message for each device and request the data
    ##          3.1 The request for data can be at two levels
    ##              - What information will you send i.e. Domain, Class, label, data type
    ##              - THe readings of the sensors and the values.

    def test_coordinator_can_send_and_receive(self, coordinator):
        
        # We need to start some sort of process to receive
        # the messages.

        # Sending the request like this means to send out for each 
        # device in the list.
        status = leawood.xbee.scan_network(coordinator)      
        status = leawood.xbee.request_data(coordinator)
        assert "OK" == status

        # Then we need to check if the messages have been received.

    def test_background_thread_is_running(self, coordinator):
        coordinator.log.info('Activating the listener')
        leawood.xbee.activate(coordinator)
        coordinator.log.info('Waiting 10 seconds before checking the state')
        time.sleep(10)
        assert coordinator.is_running() == True

        coordinator.log.info('Requesting the shutdown')
        leawood.xbee.shutdown(coordinator)
        time.sleep(10)
        coordinator.log.info('Waiting 10 seconds before checking the state')
        assert coordinator.is_running() == False