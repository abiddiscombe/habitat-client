# util/led.py
from time import sleep
from machine import Pin

def toggle(to_be_enabled):
    # use onboard LED
    LED = Pin('LED', Pin.OUT)
    LED.value(1 if to_be_enabled else 0)