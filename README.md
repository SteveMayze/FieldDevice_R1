# FieldDevice_R3
A field sensor is a a remote sensor that is envisaged for a larger network of sensors. 

# Components (envisaged)

* MCU:
* Power Monitoring: INA219
* Telemetry: XBee/ZigBee

XBee/ZigBee is considered for support and simplicity of use and will be included as a module connector and not implemented in-system.

# Running the Tests

## Run all tests
```shell
python -m pytest 
```
## Run unit tests
```shell
python -m pytest tests
```
## Run runctional/integration tests
```shell
python -m pytest functional_tests
```
Note: Use the -s option on pytest to see any stdout messages. To see the logging that is
a part of the leawood package then use the --log-cli-level=NOTSET option.

```shell
python -m pytest --log-cli-level=NOTSET -s .\\functional_tests
```

python -m pytest -s tests

# Windows
## Power Shell
$Env:XBEE_PORT = "COM6"
python -m pytest 

# Mac/Linux
export XBEE_PORT=/dev/ttyUSB0
python -m pytest


Request for Data - Specific module.
'''
RX (Receive) Packet 16-bit Address (API 2)

7E 00 0D 81 01 0A 7D 33 00 44 41 54 41 5F 52 45 51 FF

Start delimiter: 7E
Length: 00 0D (13)
Frame type: 81 (RX (Receive) Packet 16-bit Address)
16-bit source address: 01 0A
RSSI: 13
Options: 00
RF data: 44 41 54 41 5F 52 45 51
Checksum: FF
'''

Request for Data - Broadcast.
'''
RX (Receive) Packet 16-bit Address (API 2)

7E 00 0D 81 01 0A 7D 33 02 44 41 54 41 5F 52 45 51 FD

Start delimiter: 7E
Length: 00 0D (13)
Frame type: 81 (RX (Receive) Packet 16-bit Address)
16-bit source address: 01 0A
RSSI: 13
Options: 02
RF data: 44 41 54 41 5F 52 45 51
Checksum: FD
'''