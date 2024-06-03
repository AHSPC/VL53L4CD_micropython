## VL53L4CD

Pure MicroPython driver for the VL53L4CD ToF distance sensor, ported from [Adafruit's CircuitPython driver](https://github.com/adafruit/Adafruit_CircuitPython_VL53L4CD). (Tested on RPi Pico W)

Depends on [our port of](https://github.com/AHSPC/adafruit_i2c_device_micropython_port) Adafruit's i2c_device CircuitPython library (i2c_device.py must be in the same directory as vl53l4cd.py).

Example usage is in `./test.py`.

An additional `get_distance()` method is provided to hide the usage of clear_interrupt and waiting for new data in a loop (very specific to AHS Electronics Workshop class). It additionally ignores all OSErrors via try-catch, and calls get_distance() recursively if one is encountered.
