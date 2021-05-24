
from leawood.config import Config
from leawood.xbee import Coordinator
from leawood.xbee import Sensor
import os
import leawood.xbee
import time
import json

import tests.slow_tests.conftest

MAX_WAIT = 30


class TestBasic:


    def wait_for_runnning_state(self, coordinator, state):
        start_time = time.time()
        while True:
            try:
                assert coordinator.is_running() == state
                return
            except (AssertionError) as error:
                if time.time() - start_time > MAX_WAIT: 
                    raise error 
                time.sleep( 0.5)

    
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

    def test_background_thread_is_running(self, coordinator, sensor):
        coordinator.log.info('Activating the listener')
        leawood.xbee.activate(coordinator)
        coordinator.log.info('Waiting for startup')
        self.wait_for_runnning_state(coordinator, True)

        addr = str(coordinator.coordinating_device.get_64bit_addr())
        sensor.log.info(f'Sending a message to {addr}')

        payload = json.loads(f'{{"bus-voltage": 10.0}}')
        status = leawood.xbee.send_data(sensor, str(addr), str(payload))
        assert "OK" == status

        coordinator.log.info('Requesting the shutdown')
        leawood.xbee.shutdown(coordinator)
        coordinator.log.info('Waiting for shutdown')
        self.wait_for_runnning_state(coordinator, False)

