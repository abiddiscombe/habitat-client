# main.py
import time
import urequests
from util import led, console
from sensors import query_dht22
from wireless import wlan_connect

# Define secrets for the target local network
# and endpoint(s) here, but take care not to
# commit them to GitHub! MicroPython does not
# seem to support Environment Variables :(
WIFI_SSID = ""
WIFI_PASS = ""
API_KEY = ""


wlan_connect(WIFI_SSID, WIFI_PASS)

while True:
    values = query_dht22()
    
    # define the target telemetry action in this file
    # instead of a seperate module - future implementations
    # of the code may alter this!
    res = urequests.get(f"https://dweet.io/dweet/for/x?t={values['t']}&h={values['h']}")
    console.write(f"X{res.status_code}", f"Data Publish: H = {values['h']} && T = {values['t']}")
    
    # fetch and send data every 5 mins
    time.sleep(300)