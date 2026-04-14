const express = require('express');
const mqtt = require('mqtt');

// Configuration

const MQTT_BROKER = 'mqtt://localhost';
const MQTT_PORT = 1883;
const MQTT_TOPIC = 'test/topic';
const SERVER_PORT = 3000;
const MQTT_USERNAME = "testuser";
const MQTT_PASSWORD = "password";

// Create an Express application

const app = express();

// Connect to the MQTT broker

const client = mqtt.connect(`${MQTT_BROKER}:${MQTT_PORT}`, {
  username: MQTT_USERNAME,
  password: MQTT_PASSWORD
});

client.on('connect', () => {
  console.log('Connected to MQTT broker');
  client.subscribe(MQTT_TOPIC, (err) => {
    if (err) {
      console.error('Error subscribing to topic:', err);
    } else {
      console.log('Subscribed to topic:', MQTT_TOPIC);
    }
  });
});

// Handle incoming MQTT messages

client.on('message', (topic, message) => {
  console.log(`Received message on topic ${topic}: ${message.toString()}`);
});


// Define a simple route for testing

app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server

app.listen(SERVER_PORT, () => {
  console.log('Server is running on port 3000');
});