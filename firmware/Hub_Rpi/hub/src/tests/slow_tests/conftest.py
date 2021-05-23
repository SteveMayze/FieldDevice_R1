
from leawood.lwmqtt import Publisher
import pytest
from leawood.config import Config
from leawood.xbee import Coordinator
import os

def pytest_addoption(parser):
    parser.addoption("--xbeeport", action='store', help='Set the serial/com port for the coordinator device', default='COM6')


@pytest.fixture
def coord_config(pytestconfig):
    port = pytestconfig.getoption('xbeeport')
    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, 'config.json')
    cert_path = os.path.join(script_dir, '.ssh')
    args = ["--serial-port", port, '--config', config_path, '--certpath', cert_path]
    return Config(args)


@pytest.fixture
def coordinator(coord_config):
    publisher = Publisher(coord_config)
    coordinator = Coordinator(coord_config, publisher)
    yield coordinator
    coordinator.close()

