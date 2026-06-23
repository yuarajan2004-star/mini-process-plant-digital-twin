import json
import time

import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect(
    "localhost",
    1883,
    60
)

while True:

    payload = {

        "PT101":0.70,

        "FT101":70,

        "TT101":36,

        "Pump_Status":1
    }

    client.publish(
        "plant/data",
        json.dumps(payload)
    )

    print(payload)

    time.sleep(1)
