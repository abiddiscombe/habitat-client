# pico-dht22-telemetry
The repo contains my code for connecting a `DHT22` temperature and humidity sensor to the internet via a [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) and [MicroPython](https://micropython.org/). You can think of it as a very early attempt at IoT / telemetry.

> This code *will* have bugs, I'm learning as-I-go for this project and will fix things as they cause issues for me. Feel free to fork and adjust this code as you wish.

## Getting Started
I'm still learning MicroPython and Raspberry Pi Pico - so please expect these instructions to change as I learn better ways of programming the device!

1. Flash MicroPython onto the Pico. Here's the [official guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython).
2. Copy the contents of the `/src` directory to the Pico's internal storage.
3. In `main.py`, change the values for `WIFI_SSID`, `WIFI_PASS`. If you're writing code to your own service, you'll also need to reconfigure the HTTP request code (via `urequest`).
4. Further customise the code as required, it will auto-run on device boot.

## To-Do
I *might* need to:
- [ ] Add temeprature data from the onboard temperature chip.
- [ ] Improve handling of situations where the network connection is lost.
- [ ] Store a stream of recent data to memory for debug purposes.
