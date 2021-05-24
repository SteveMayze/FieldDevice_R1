
from leawood.config import Config
from leawood.xbee import Sensor
from unittest.mock import patch
from digi.xbee.devices import XBeeException
import pytest
import json
import leawood.xbee
import tests.fast_tests.xbee_support
import tests.fast_tests.mqtt_support
import time

MAX_WAIT = 1


@pytest.fixture
def config():
    args = ["--serial-port", "COM1", "--baud", "9600", "--sleeptime", "0"]
    return Config(args)

@pytest.fixture
def sensor(config):
    return tests.fast_tests.xbee_support.FakeSensor(config)

class TestCase:

    def test_coordinator_send_data(self, sensor):
        payload = json.loads(f'{{"bus-voltage": 10.0}}')

        status = leawood.xbee.send_data(sensor, '0013A20041AE49D4', payload)
        assert "OK" == status

        # assert node_data[0]['voltage'] == 10.6
        assert sensor.sensing_device.spy["0013A20041AE49D4"] == payload

