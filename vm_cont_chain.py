"""EE 250L Lab 04 PONG Code"""
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	print("Connected to rPi with result code "+str(rc))
#Subscribe to ping	
	client.subscribe("diegoaga/ping")
	client.message_callback_add("diegoaga/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
	number= int(message.payload.decode())+1
	time.sleep(0.5)
	client.publish("diegoaga/pong",number)
	print("Updated Pong:"+ f"{number}")
	
def on_message(client, userdata, msg):
    print("Default callback - time: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect("192.168.1.146",1883, 60)
	client.loop_forever()
	time.sleep(0.5)
