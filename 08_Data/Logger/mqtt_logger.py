import json
import csv
import os

from datetime import datetime

import paho.mqtt.client as mqtt

FILE = "../Historian/plant_historian.csv"

if not os.path.exists(FILE):

    with open(FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Timestamp",
            "PT101",
            "FT101",
            "TT101",
            "Pump_Status"
        ])

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    with open(FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now(),
            data["PT101"],
            data["FT101"],
            data["TT101"],
            data["Pump_Status"]
        ])

    print("Logged:", data)

client = mqtt.Client()

client.on_message = on_message

client.connect("localhost",1883,60)

client.subscribe("plant/data")

client.loop_forever()
