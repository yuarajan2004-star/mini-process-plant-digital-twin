import json
import time
import random
import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("localhost",1883,60)

while True:

    payload = {
        "PT101": round(random.uniform(0.8,1.2),2),
        "FT101": round(random.uniform(90,120),2),
        "TT101": round(random.uniform(25,35),2),
        "Pump_Status": 1
    }

    client.publish(
        "plant/data",
        json.dumps(payload)
    )

    print(payload)

    time.sleep(1)
