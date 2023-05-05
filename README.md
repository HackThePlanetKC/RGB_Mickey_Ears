# RGB_Mickey_Ears
This repo is for collecting the code I'm using to build a custom set of Mickey ears. 

I've based this idea on https://learn.adafruit.com/neopixel-led-mickey-ears/, but instead of only having one animation when you shake your head, I'm wanting to advance the animations through a whole list of them depending on what you do.

Currently, as of 5/3/23, I don't have an ADXL345 accelerometer, so I'm limited to just a simple ball tilt switch. I plan on upgrading this in the future to be able to determine which direction you tilt your head and act accordingly.

I have this built on a raspberry pi pico configured with circuitpython, and using the adafruit_ledanimation, adafruit_debouncer.mpy, adafruit_ticks.mpy, and neopixel.mpy libraries.
