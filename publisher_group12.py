import socket
import logging
import time
import json
from sense_hat import SenseHat
from datetime import datetime

HOST = "100.83.170.97"  # Brokers IP (aka the VPN the broker is using)
PORT = 1234  # Brokers port

sense = SenseHat()  # initializing the sensehat
loopCount = 0  # only needed to keep track of sequence number
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")
    while True:

        # sensor data
        temp = round(sense.get_temperature(), 1)
        humidity = round(sense.get_humidity(), 1)
        pressure = round(sense.get_pressure(), 1)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # local time

        # payload using sensor data
        payload = {
            "sequence": loopCount,
            "timestamp": timestamp,
            "temp": temp,
            "humidity": humidity,
            "pressure": pressure
        }
        message = json.dumps(payload) + "\n"
        try:
            sock.sendall(message.encode())
            print(f"Sent to {HOST}:{PORT}: {message.strip()}")  # only sending the payload to the Broker
        except Exception as e:
            print(f"TCP Error: {str(e)}")

        loopCount += 1
        time.sleep(10)
finally:
    sock.close()

