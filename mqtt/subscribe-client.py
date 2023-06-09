# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:56:03 2021

@author: fschoo

Source: http://www.steves-internet-guide.com/into-mqtt-python-client/

"""


import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


#broker_address="192.168.1.184" 
#broker_address="iot.eclipse.org"
broker_address="broker.mqttdashboard.com" #use external broker
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message        #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start()    #start the loop

print("Subscribing to topic","house/main-bulb")
client.subscribe("house/main-bulb")

print("Publishing message to topic","house/main-bulb")
client.publish("house/main-bulb","ON1")
time.sleep(4) 
print("Publishing message to topic","house/main-bulb")
client.publish("house/main-bulb","OFF1")
time.sleep(4) # wait

client.loop_stop() #stop the loop




