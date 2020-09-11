#// Author : Steve Gale 29/04/19
#// Modified : SG - 29/04/19 -
#// Modified : SG - 13/03/20 - added host addresses for the 2020 VM test server
#// Copyright 2019 Steve Gale - seek permission and terms of use before you copy or modify this code
import os
import time
import struct
import machine
import socket
import json


from pysense import Pysense
from SI7006A20 import SI7006A20

#set up sensor class
py = Pysense()
si = SI7006A20(py)
 
# IP address of PHP / MySQL server

host = '192.168.100.100'   # VM Stetic IP in SG HOME Mikrotik Network - 11/08/20
#host = '10.0.0.60'   # VM DHCP Lease in SG HOME Network
#host = '192.168.223.240'   # VM DHCP Lease in E223 (OR 241)
#host = '192.168.208.240'   # VM DHCP Lease in E208
#host = '192.168.217.9'      # VM DHCP Lease in E216
port = 80

# check if Lopy DHCP IP has changed


for i in range(0,3):
    time.sleep(1)           # 1 sec delay
    tempValue = si.temperature()        #/100.0
    humidityValue = si.humidity()  
 
    try:                    # try to connect to server
        # Test message  message based on the LoRa package format (protocol definition)
        #device_id = 1       # simulated LoRa client id
        #msg = '{ "H" : "%.2f", "T": "%.2f" }'%(humidityValue,tempValue)
        #print('Device: %d - Pkg:  %s' % (device_id, msg))
         
        # extract measured values from recieved Json string from LoRa client message
        #obJsMeasuredVals = json.loads(msg)                  # json object
        #TemperatureStr = json.dumps(obJsMeasuredVals["T"])  # key for Temperature value in dictionary
        #HumidityStr = json.dumps(obJsMeasuredVals["H"])     # key for Humidity value in dictionary
 
        # construct new json string with measured values inserted for server post
        # construct json string with measured values insetred
        contentStr='{ "RoomName" : "E223", "Humidity" : "%.2f", "Temperature": "%.2f" }'%(humidityValue,tempValue)
        postStr = 'POST /i40Test/admin/InsertJsonRESTData.php HTTP/1.1\r\n'
        hostStr = 'Host: %s:%s\r\n'%(str(host),str(port))
        contentTypeStr = 'Content-Type: application/json\r\n'
        contentLengthStr = 'Content-Length: %s\r\n\r\n'%str(len(contentStr))
         
        # format HTTP post payload string for sending to the PHP / mySQL server
        payload =  postStr + hostStr+ contentTypeStr + contentLengthStr  + contentStr
        print(payload)      #debugging
        
        # connect to php / database server, send the payload data and recieve the server response
        try:
            s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

            s.connect((host, port))
            s.send(payload.encode())
            svrResponse = s.recv(4096)

            print(svrResponse)   
      
        # extract the json string from the recieved data based on byte location (could use content length and trim off from end of string)
            strJsonResponse = ""
            for b in range(148,192):    # json string location in recieved data (148,192) - this may change
                strJsonResponse += chr(svrResponse[b])
        #print(strJsonResponse)
         
        # convert recieved json string to a python object (dictionary)
            obJsRecieved = json.loads(strJsonResponse)      #dictionary object
            print(json.dumps(obJsRecieved))
        #print(json.dumps(obJsRecieved["code"]))         #key for code value in dictionary
        #print(json.dumps(obJsRecieved["message"]))      # key for message value in dictionary
        except Exception:
            print("host unreachable")   
    except ValueError:
        print ("Buffer too small OR JSON Value error")
    # Respond to device with an acknowledge packet

 