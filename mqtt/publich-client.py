# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 08:41:37 2021

@author: fschoo

Source: http://www.steves-internet-guide.com/into-mqtt-python-client/

"""

import paho.mqtt.client as mqtt #import the client1
import time

#broker_address="192.168.1.184" #local broker
#broker_address="iot.eclipse.org" #use external broker
broker_address="broker.mqttdashboard.com" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF1")#publish
time.sleep(4)
client.publish("house/main-light","ON1")#publish