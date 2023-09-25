# services/wireless.py
import network
import time
from utilities import led

wlan = None
 
def enable():
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print('[ WLAN ] Wireless Enabled')


def connect(wlan_metadata):
    global wlan
    wlan.connect(wlan_metadata['ssid'], wlan_metadata['pass'])
    max_wait = 20
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(1)
    
    if wlan.status() != 3:
        print("[ WLAN ] Connection Failed.")
        while True:
            led.enable()
            time.sleep(0.1)
            led.disable()
            time.sleep(0.4)
        
    else:
        print("[ WLAN ] Connection Established.")
        print(f"[ WLAN ] IP: {wlan.ifconfig()[0]}")


def healthcheck(wlan_metadata):
    global wlan
    if not wlan.isconnected():
        print("[ WLAN ] Network Connection Lost. Reconnecting...")
        connect(wlan_metadata)


