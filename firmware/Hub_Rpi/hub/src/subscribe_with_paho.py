from config import *
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f'Result from connect: {mqtt.connack_string(rc)}')
    # Subscribe to the power/sensor/+/data
    client.subscribe('power/sensor/+/data', qos=2)


def on_subscribe(client, userdata, mid, granted_qos):
    print(f'I have subscribed with QoS {granted_qos[0]}')

def on_message(client, userdata, msg):
    print(f'Message received. Topic: {msg.topic}, payload {str(msg.payload)}')


if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.tls_set(ca_certs = ca_certificate, certfile=client_certificate, keyfile=client_key)
    client.connect(host=mqtt_server, port=mqtt_port, keepalive=mqtt_keepalive)
    client.loop_forever()

