
import pytest
from leawood.config import Config
from leawood.xbee import Coordinator

def pytest_addoption(parser):
    parser.addoption("--xbeeport", action='store', help='Set the serial/com port for the coordinator device', default='COM6')


@pytest.fixture
def coord_config(pytestconfig):
    port = pytestconfig.getoption('xbeeport')
    args = ["--serial-port", port, "--baud", "9600"]
    return Config(args)


@pytest.fixture
def coordinator(coord_config):
    coordinator = Coordinator(coord_config)
    yield coordinator
    coordinator.close()

