# ref - https://docs.python.org/3/howto/sockets.html
import socket
import json
import random   #used for sensor simulation

host = '192.168.100.100'   # VM STATIC IP in SG HOME Network
port = 80

# read sensors (simulated)
def readTempSensorSim():                # simulate reading temp sensor
    return (random.uniform(19,26))      # return a random value within specified range

def readHumiditySensorSim():            # simulate reading humidity sensor
    return (random.uniform(20,80))      # return a random value within specified range

tempValue = readTempSensorSim()
humidityValue = readHumiditySensorSim()

# construct post data
contentStr='{ "RoomName" : "E223", "Humidity" : "%.2f", "Temperature": "%.2f" }'%(humidityValue,tempValue)
#contentStr='{ "RoomName" : "E223", "Humidity" : "%0.2f", "Temperature": "%.2f" }'%(40.0,21.6)
postStr = 'POST /i40Test/admin/InsertJsonRESTData.php HTTP/1.1\r\n'
hostStr = 'Host: %s:%s\r\n'%(str(host),str(port))
contentTypeStr = 'Content-Type: application/json\r\n'
contentLengthStr = 'Content-Length: %s\r\n\r\n'%str(len(contentStr))
         
        # format HTTP post payload string for sending to the PHP / mySQL server
payload =  postStr + hostStr+ contentTypeStr + contentLengthStr  + contentStr
print(payload)      #debugging
        
        # connect to php / database server, send the payload data and recieve the server response
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(payload.encode())
    svrResponse = s.recv(4096)
    s.close()
    print(svrResponse)   
except Exception as e:
    print("host unreachable {0} ".format(e))     
        # extract the json string from the recieved data based on byte location (could use content length and trim off from end of string)
try:
    strJsonResponse = ""
    for b in range(148,192):    # json string location in recieved data (148,192) - this may change
        strJsonResponse += chr(svrResponse[b])
    print(strJsonResponse)
         
    # convert recieved json string to a python object (dictionary)
    obJsRecieved = json.loads(strJsonResponse)      #dictionary object
    #print(json.dumps(obJsRecieved))

    code = obJsRecieved['code']                    #key for code value in dictionary
    message = obJsRecieved['message']              # key for message value in dictionary
    print("code = {0} : message = {1}".format(code,message))

except Exception as e :
    print("Json Decode error {0} ".format(e)) 


