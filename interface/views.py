from django.shortcuts import render, redirect

from django.urls import reverse

from django.utils import timezone

from datetime import datetime

import time
import random
import paho.mqtt.client as mqtt

TOPIC = "wrist/data/sensors"

mess = [-1, -1, -1]

client = mqtt.Client("client" + str(random.randrange(100000, 999999)), clean_session=True)

print("2")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))
    client.loop_stop()

def on_message(client, userdata, msg):
    global mess

    data = list(msg.payload)

    timestamp = int.from_bytes(bytes(data[:-3]), "little")
    curr_time = time.time()
    elapsed = curr_time - timestamp

    sensor_data = data[-3:]
    mess = sensor_data
    print(elapsed, ":\t", sensor_data)


def interface_view(request):

    print("1")

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("mqtt.eclipseprojects.io", 1883, 60)

    client.loop_start()

    print("5")

    myDate = datetime.now()

    return render(request, 'interface/index.html', {
        'myDate': myDate,
        'opacity1': 1,
        'object1': str(mess[0]) + 'px',
        'opacity2': 1,
        'object2': str(mess[1]) + 'px',
        'opacity3': 1,
        'object3': str(mess[2]) + 'px',
    })
