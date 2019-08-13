import paho.mqtt.client as mqtt
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Publisher client')
print('-----------------------------------')
client = mqtt.Client()
username = 'mec'
password = 'password'
broker_ip = input("Broker's IP: ").strip()
broker_port_no = '1883'
topic = 'mec'
print('-----------------------------------')


def on_connect(connect_client, userdata, flags, rc):
    print("Subscribed to Topic :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic)


client.on_connect = on_connect
client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)

while True:
    try:
        message = input('Input Message: ').strip().lower()
        client.publish(topic, message, retain=True)
        print("Message Sent")
    except KeyboardInterrupt:
        print('\nProgramme Terminated')