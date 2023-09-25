# services/sensors.py
import dht
from machine import ADC, Pin

def query():
    results = {}
    results.update(query_dht22())
    results.update(query_onboard())
    return results

def query_dht22():
    DHT22 = dht.DHT22(Pin(13))
    DHT22.measure()
    return {
        "humidity": DHT22.humidity(),
        "temp_external": DHT22.temperature()
    }

def query_onboard():
    adc = ADC(4)
    adc_voltage = adc.read_u16() * (3.3 / (65536))
    adc_temp = 27 - (adc_voltage - 0.706)/0.001721
    return {
        "temp_internal": round(adc_temp, 2)
    }
