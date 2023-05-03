#Things left to do:

#Figure out how to get the tilt to advance animations
#buy good accelerometer
#Get side light strips
#Get a lipo battery pack

import board
import neopixel
import time
#from machine import Pin

#Import ALL THE THINGS
from adafruit_led_animation.color import RED, GREEN, AMBER, JADE, BLUE
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.multicolor_comet import MulticolorComet
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup
from digitalio import DigitalInOut, Direction, Pull

#Set board pin and count
pixel_pin_L = board.GP15
pixel_pin_R = board.GP0
pixel_num = 15

#Set Tilt Switch
tilt = DigitalInOut(board.GP10)
tilt.direction = Direction.INPUT
tilt.pull = Pull.DOWN

#Set up animation groups
strip_pixels_L = neopixel.NeoPixel(pixel_pin_L, pixel_num, brightness=0.5, auto_write=False)
strip_pixels_R = neopixel.NeoPixel(pixel_pin_R, pixel_num, brightness=0.5, auto_write=False)

#Set up pixels
#pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

#Set variables for all effects
#blink = Blink(pixels, speed=0.5, color=GREEN)
#comet = Comet(pixels, speed=0.1, color=RED, tail_length=5, bounce=True)
#pulse = Pulse(pixels, speed=0.1, color=BLUE, period=20)
#sparkle = Sparkle(pixels, speed=0.5, color=AMBER, num_sparkles=5)
#parkle_pulse = SparklePulse(pixels, speed=0.05, period=1, color=JADE)
#rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=5)

#Set animation sequence and timing
#animations = AnimationSequence(
#	blink,
#	pulse,
#	comet,
#	sparkle,
#	sparkle_pulse,
#	rainbow_sparkle,
#	advance_interval=5,
#	auto_clear=True,
#)

#Set animation group animations
rainbow_sparkle = AnimationSequence(
	AnimationGroup(
		RainbowSparkle(strip_pixels_L, 0.1, num_sparkles=5),
		RainbowSparkle(strip_pixels_R, 0.1, num_sparkles=5),
		sync=True,
	),
)

solid_sparkle_L = AnimationSequence(
	AnimationGroup(
		Sparkle(strip_pixels_L, 0.1, num_sparkles=5),
		sync=True,
	),
)

solid_sparkle_R = AnimationSequence(
	AnimationGroup(
		Sparkle(strip_pixels_R, 0.1, num_sparkles=5),
		sync=True,
	),
)

comets = AnimationSequence(
	AnimationGroup(
		Comet(strip_pixels_L, 0.1, color=GREEN, tail_length=5, bounce=True),
		Comet(strip_pixels_R, 0.1, color=GREEN, tail_length=5, bounce=True),
		sync=True,
	),
)

chase = AnimationSequence(
	AnimationGroup(
		Chase(strip_pixels_L, 0.1, size=3, spacing=4, color=BLUE),
		Chase(strip_pixels_R, 0.1, size=3, spacing=4, color=BLUE),
		sync=True,
	),
)

#run it
while True:
    #blink.animate()
    #pulse.animate()
    #comet.animate()
    #sparkle.animate()
    #sparkle_pulse.animate()
    #animations.animate()
    group_animations.animate(),
    #print(tilt.value)
    if tilt.value == False:
    	print("Tilted")
