echo Running mosquitto commands...
echo Creating password file with testuser...
mosquitto_passwd -c config/passwd testuser
@REM Use "password" as the password when prompted.
echo Password file created.
@REM Run the following to change ownership and permissions of the password file to allow mosquitto to read it:
@REM docker exec -it mqtt-broker sh
@REM chown mosquitto:mosquitto /mosquitto/config/passwd
@REM chmod 0700 /mosquitto/config/passwd
echo Starting mosquitto broker with configuration...
mosquitto -v -c config/mosquitto.conf
pause