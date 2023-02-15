"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))


if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python. For example:
    
    `client.connect("eclipse.usc.edu", 11000, 60)` 
    
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect("eclipse.usc.edu", 11000, 60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_start()
    time.sleep(1) #causes program to pause for 1 second to complete connection process

    while True:
        #replace user with your USC username in all subscriptions
        #the f-string is evalutued and passed as the argument to the publish method to the subtopic diegoaga/ipinfo on the MQTT broker
        client.publish("diegoaga/ipinfo", f"{ip_address}")
        print("Publishing ip address")
        time.sleep(4)
        #get date and time 
        #The datetimenow() returns the current date and time as the imported datetime object
        #The strftime() method formats it into a string with format below
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #publish date in its own topic
        #split the current_datetime string into a list of substrings, using the space character as a delimiter. 
        client.publish("diegoaga/date", current_datetime.split(" ")[0])
        print("Publishing date", current_datetime.split(" ")[0])
        #publish time in its own topic
        client.publish("diegoaga/time", current_datetime.split(" ")[1])
        print("Publishing time")
        time.sleep(4)
        
