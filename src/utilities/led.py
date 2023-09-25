# utilities/led.py
from machine import Pin

# uses the onboard LED
LED = Pin('LED', Pin.OUT)

def enable():
    global LED
    LED.value(1)

def disable():
    global LED
    LED.value(0)
