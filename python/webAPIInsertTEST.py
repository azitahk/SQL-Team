# ref - https://www.w3schools.com/python/ref_requests_post.asp
# >python -m pip install requests
# $python3 -m pip install -U requests


import urllib.parse 
import requests 


contentStr='{ "RoomName" : "E223", "Humidity" : "%0.2f", "Temperature": "%.2f" }'%(75.0,33.3)
#contentStr='{ "RoomName" : "E223", "Humidity" : "40.0", "Temperature": "21.6" }'

url = 'http://192.168.100.100/i40Test/admin/InsertJsonRESTData.php' 
# note change the URL to match your server IP address


json_data = requests.post(url,data = contentStr).json()
print(json_data)
code = json_data['code']
message = json_data['message']
print("code = {0} : message = {1}".format(code,message))
