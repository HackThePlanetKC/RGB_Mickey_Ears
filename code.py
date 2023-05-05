#Things left to do:

#Figure out how to get the tilt to advance animations - Done
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
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.SparklePulse import SparklePulse
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
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
#tilt.pull = Pull.DOWN

#Set up animation groups
strip_pixels_L = neopixel.NeoPixel(pixel_pin_L, pixel_num, brightness=0.25, auto_write=False)
strip_pixels_R = neopixel.NeoPixel(pixel_pin_R, pixel_num, brightness=0.25, auto_write=False)

clearL = strip_pixels_L.fill((0,0,0))
clearR = strip_pixels_R.fill((0,0,0))

#Set animation group animations
rainbow_sparkle = AnimationSequence(
	AnimationGroup(
		RainbowSparkle(strip_pixels_L, 0.1, num_sparkles=5),
		RainbowSparkle(strip_pixels_R, 0.1, num_sparkles=5),
		sync=False,
	),auto_clear=True
)

solid_sparkle_L = AnimationSequence(
	AnimationGroup(
		Sparkle(strip_pixels_L, 0.1, color=AMBER, num_sparkles=7),
		sync=True,
	),auto_clear=True
)

solid_sparkle_R = AnimationSequence(
	AnimationGroup(
		Sparkle(strip_pixels_R, 0.1, color=AMBER, num_sparkles=7),
		sync=True,
	),auto_clear=True
)

comets = AnimationSequence(
	AnimationGroup(
		Comet(strip_pixels_L, 0.1, color=GREEN, tail_length=5, bounce=True),
		Comet(strip_pixels_R, 0.1, color=GREEN, tail_length=5, bounce=True),
		sync=True,
	),auto_clear=True
)

rainbow_chase = AnimationSequence(
	AnimationGroup(
		RainbowChase(strip_pixels_L, speed=0.1, size=3, spacing=3),
		RainbowChase(strip_pixels_R, speed=0.1, size=3, spacing=3),
		sync=True,
	),auto_clear=True
)

rainbow_comet = AnimationSequence(
	AnimationGroup(
		RainbowComet(strip_pixels_L, speed=0.1, tail_length=6, bounce=False),
		RainbowComet(strip_pixels_R, speed=0.1, tail_length=6, bounce=False),
		sync=True,
	),
)

#List of animations
animations_list = [
	rainbow_sparkle,
	comets,
	rainbow_chase,
	solid_sparkle_L,
	solid_sparkle_R,
	rainbow_comet,
]

list_pos = 0
last_state = False
last_trigger_time = 0

#run it
while True:
    
  current_state = tilt.value

  # If the tilt switch is in the False state, iterate through the list.
  #if current_state == False and last_state == False: #and time.time() - last_trigger_time > 5.5:
  #Added an RC debounce circuit, had to swap the triggers. 
  if current_state == True:
    print(animations_list[list_pos])
    print(list_pos)
    list_pos = (list_pos + 1) % len(animations_list) 
    animations_list[0].fill((0,0,0))
    last_trigger_time = time.time()
    time.sleep(0.25)  
    
  #The following does work, but the tilt sensor I'm using is just too sensitive to be practical for this usage. Right now, it will clear the strips and start fresh with every animation. 
  #if current_state == True:# and time.time() - last_trigger_time > 2:
  if current_state == False and last_state == False:
      animations_list[list_pos].animate()

  last_state = current_state  
