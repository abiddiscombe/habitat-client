# wireless.py
import network
import time
from util import led, console
 
def wlan_connect(ssid, passkey):
    console.write("INFO", "Connecting to WLAN")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, passkey)
    max_wait = 20
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        led.toggle(True)
        time.sleep(0.6)
        led.toggle(False)
        time.sleep(0.6)
    
    if wlan.status() != 3:
        _connect_fail()
    else:
        _connect_success(wlan.ifconfig()[0])


def _connect_fail():
    console.write("FAIL", "WLAN Connection Failed")
    
    # Place device into an infinite loop instead of throwing
    # an error, this is to provide a visual indication of
    # connection failure to a non-console user.
    
    while True:
        led.toggle(True)
        time.sleep(0.2)
        led.toggle(False)
        time.sleep(0.2)


def _connect_success(ip_addr):
    led.toggle(True)
    console.write("INFO", "WLAN Connection Established")
    console.write("INFO", "WLAN IP: " + ip_addr)
    time.sleep(2)
    led.toggle(False)
    time.sleep(1)
