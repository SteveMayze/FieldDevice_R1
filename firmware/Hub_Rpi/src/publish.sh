#!/bin/bash

mosquitto_pub -h 192.168.178.45 -V mqttv311 -p 8883 \
    --cafile /Users/steve/Documents/PCBs/Leawood/FieldDevice_R3/firmware/Hub_Rpi/src/.ssh/ca.crt \
    --cert /Users/steve/Documents/PCBs/Leawood/FieldDevice_R3/firmware/Hub_Rpi/src/.ssh/hub001.crt \
    --key /Users/steve/Documents/PCBs/Leawood/FieldDevice_R3/firmware/Hub_Rpi/src/.ssh/hub001.key \
    -t power/sensor/0013A20041629BFB/data -f $1 -d


