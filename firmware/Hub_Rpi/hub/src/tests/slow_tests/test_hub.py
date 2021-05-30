
from leawood.config import Config
from leawood.xbee import Coordinator
from leawood.xbee import Sensor
from leawood.lwrest import Rest
import os
import leawood.xbee
import time
import json
import logging
import random
import tests.slow_tests.conftest

MAX_WAIT = 30


class TestBasic:


    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value



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

     # Then we need to check if the messages have been received.

    def test_coordinator_can_send_and_receive(self, coordinator, sensor, message_handler):
        self._log = logging.getLogger('test_hub.TestBasic')

        self.log.info('Activating the listener')
        leawood.xbee.activate(coordinator)
        self.log.info('Waiting for startup')
        self.wait_for_runnning_state(coordinator, True)
        leawood.lwmqtt.start_message_handler(message_handler)

        # Send a message from GREEN to be picked up and handled
        # by the coordinator RED. This message is then posted 
        # to the MQTT
        addr = str(coordinator.coordinating_device.get_64bit_addr())
        self.log.info(f'Sending a message to {addr}')
        devices = coordinator.nodes
        device = devices[0]
        node_address = str(device["ADDRESS"])

        test_value = random.randrange(9000, 15000) / 1000
        payload = json.loads(f'{{"address":"{node_address}", "label": "bus-voltage","value": {test_value}}}')
        status = leawood.xbee.send_data(sensor, str(addr), json.dumps(payload))
        assert "OK" == status

        # Use the REST API to pull back down the last posted message and compare the
        # random generated value with what has been posted.
        rest = Rest(coordinator.config)
        response = rest.get("devices", '{"name":"Mobile+Chook+shed"}')
        device_id = response["device_id"]
        self.log.info(f'Found the Mobile chook shed: {device_id}')
        response = rest.get("data_points", f'{{"device_id": "{device_id}", "$orderby":{{"POINT_TIMESTAMP":"DESC"}}}}')
        self.log.info(f'Last device data: {response}')
        assert response["point_value"] == test_value




        # The message is being posted to the MQTT ... this
        # now needs a mechanism to subscribe and wait for a
        # message to appear on the queue.
        # NB: The MQTT is only working based on a bodge to reduce the 
        #     security checking. Otherwise the certificates are failing
        #     though they work on the command line.
        # Failure in the MQTT layer is not being reflected back 
        # at the higher end of the system and is going undetected.#
        # This can only be seen with the following options on the test
        # -v  --log-cli-level=NOTSET -s

        # Make sure the XBee units are running as is the MQTT server
        # Verification is only made using a manual subscriber
        #  "C:\Program Files\mosquitto\mosquitto_sub" -h 192.168.178.45 
        #             -V mqttv311 -p 8883 --cafile ca.crt --cert hub001.crt 
        #             --key hub001.key -t "power/sensor/0013A20041629BFB/data"


        
        

        ### This now constitues a tear down of the whole test.
        coordinator.log.info('Requesting the shutdown')
        leawood.xbee.shutdown(coordinator)
        coordinator.log.info('Waiting for shutdown')
        self.wait_for_runnning_state(coordinator, False)

