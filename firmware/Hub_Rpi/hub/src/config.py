
import os

certificate_path = os.environ.get('LW_CERT_PATH')
ca_cert = os.environ.get('LW_CACERT')
cl_cert = os.environ.get('LW_CIENT_CERT')
cl_key = os.environ.get('LW_CIENT_KEY')
ca_certificate = os.path.join(certificate_path, ca_cert)
client_certificate = os.path.join(certificate_path, cl_cert)
client_key = os.path.join(certificate_path, cl_key)

mqtt_server = os.environ.get('LW_MQTT_SERVER')
mqtt_port = int(os.environ.get('LW_MQTT_PORT'))
mqtt_keepalive = 60


