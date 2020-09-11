
import machine

from network import WLAN


# change this to match the wifi AP and password the device will connect to
wifi_ssid = 'MikroTik-SGHOME'
wifi_pass = 'GordonICT'

if machine.reset_cause() != machine.SOFT_RESET:
        
    wlan = WLAN(mode=WLAN.STA)
    
    wlan.connect(wifi_ssid, auth=(WLAN.WPA2, wifi_pass), timeout=5000)

    while not wlan.isconnected(): 
         machine.idle()

print('Connected to wifi')
print(wlan.ifconfig())
machine.main('main.py')