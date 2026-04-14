import paho.mqtt.client as mqtt
import time

# MQTT Broker settings

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"
MQTT_USERNAME = "testuser"
MQTT_PASSWORD = "password"
TLS_CA_FILE = "cert/ca.crt"

# Create MQTT client and connect to broker

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.tls_set(ca_certs=TLS_CA_FILE)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Publish data to MQTT topic in a loop

while True:
    data = "Hello from Edge Node!"
    client.publish(MQTT_TOPIC, data)
    print(f"Published: {data}")
    time.sleep(5)