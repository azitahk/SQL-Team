#// Author : Steve Gale 11/08/20
#// Modified : 
#// Copyright 2019 Steve Gale - seek permission and terms of use before you copy or modify this code
# https://github.com/micropython/micropython-lib/tree/master/urequests
# https://docs.pycom.io/firmwareapi/micropython/usocket/
# https://forum.pycom.io/topic/4068/json-posts


import urequests as requests
import ujson

humidityValue = 40.0
tempValue = 21.4
url = "http://192.168.100.100/i40Test/admin/InsertJsonRESTData.php" 



payload = '{ "RoomName" : "E223", "Humidity" : "%.2f", "Temperature": "%.2f" }'%(humidityValue,tempValue)
r = requests.post(url, data = payload)
print(r.text)
r.close()







