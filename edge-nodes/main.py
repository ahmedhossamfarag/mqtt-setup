import paho.mqtt.client as mqtt
import time

# MQTT Broker settings

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "test/topic"

# Create MQTT client and connect to broker

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Publish data to MQTT topic in a loop

while True:
    data = "Hello from Edge Node!"
    client.publish(MQTT_TOPIC, data)
    print(f"Published: {data}")
    time.sleep(5)