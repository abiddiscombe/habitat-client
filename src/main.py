# main.py
import mcron
import secrets
from utilities import led
from services import sensors, wireless, telemetry
 
wireless.enable()
wireless.connect(secrets.WLAN)
    
def callback_handler(callback_id, timestamp, callback_memory):
    led.enable()
    # check wifi still connected
    wireless.healthcheck(secrets.WLAN)
    values = sensors.query()
    telemetry.push(secrets.ASSET_ID, timestamp, values)
    led.disable()

mcron.init_timer()
mcron.insert(60, {0}, '60s', callback_handler, from_now=True)

