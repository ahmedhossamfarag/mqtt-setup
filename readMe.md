# MQTT Local Setup
Classic MQTT local setup with three parts:
1. MQTT broker (server)
2. Python publisher (sends messages)
3. Express (Node.js) subscriber (listens to messages)

## Branches
- **basic**: Basic setup whitout authentication
- **basic-auth**: Setup with basic username/password authenticaiton
- **tls-auth**: Setup with TLS configurations
- **dockerize**: Setup with TLS configurations & Docker Containers
