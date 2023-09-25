# pico-dht22-telemetry

The repo contains my code for connecting a `DHT22` temperature and humidity sensor to the internet via a [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) and [MicroPython](https://micropython.org/). You can think of it as a very early attempt at IoT / telemetry.

## Getting Started
I'm still learning MicroPython and Raspberry Pi Pico - so please expect these instructions to change as I learn better ways of programming the device!

1. Flash MicroPython onto the Pico. Here's the [official guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython).
2. Copy the contents of the `/src` directory to the root directory of the Pico's internal storage.
3. In [Thonny](https://thonny.org/), add the `micropython-mcron` package to the board. [View source](https://github.com/fizista/micropython-mcron). This package is used for accurate timekeeping between readings.
4. You'll need to tweak line 200 of `lib/mcron/__init__.py` to be `timer = machine.Timer()`. [This GitHub thread](https://github.com/fizista/micropython-mcron/issues/2) explains why.
5. In `secrets.py`, change the values for `WIFI` to match your network. You'll also need to reconfigure the HTTP request code in `/services/telemetry.py` to match your infrastructure.

## To-Do
- [x] Add temeprature data from the onboard temperature chip.
- [x] Improve handling of situations where the network connection is lost.
- [x] Better cron-like scheduling of sensor events.
- [ ] Better HTTP telemetry code. Dweet is for testing only.