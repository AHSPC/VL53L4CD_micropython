## VL53L4CD

Pure MicroPython driver for the VL53L4CD ToF distance sensor. Ported from Adafruit's CircuitPython driver. (Tested on RPi Pico)

Depends on [our port of Adafruit's i2c_device CircuitPython library](https://github.com/AHSPC/adafruit_i2c_device_micropython_port).

Example usage is in `./test.py`.

An additional `get_distance()` method is provided to hide the usage of clear_interrupt and waiting for new data in a loop (specific to AHS Electronics Workshop class). It additionally ignores all OSErrors via try-catch 
