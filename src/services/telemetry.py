# services/telemetry.py
import urequests

def push(asset_id, timestamp, values):
    res = urequests.get(f"https://dweet.io/dweet/for/{asset_id}?ts={timestamp}&temp-e={values['temp_external']}&temp-i={values['temp_internal']}&hum={values['humidity']}", timeout=4)
    res.close()
    print(f"[ TELE ] Data Push Completed. HTTP {res.status_code}.")
