# sensors.py
import dht
from machine import Pin
from util import led

def query_dht22():
    DHT22 = dht.DHT22(Pin(13))
    led.toggle(True)
    DHT22.measure()
    led.toggle(False)
    return {
        "h": DHT22.humidity(),
        "t": DHT22.temperature()
    }
