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
from adafruit_debouncer import Debouncer

#Set board pin and count
pixel_pin_L = board.GP15
pixel_pin_R = board.GP0
pixel_num = 15

#Set Tilt Switch
tilt = DigitalInOut(board.GP10)
tilt.direction = Direction.INPUT

#debounce it
tilt_switch = Debouncer(tilt)

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
  
  #debouncing stuff
  tilt_switch.update()

  # If the tilt switch is in the True state, iterate through the list.
  #Added an RC debounce circuit
  #Attempt to add debounced trigger, it works! It only changes animations when it tilts for >0.5s
  if tilt_switch.value == True and tilt_switch.current_duration > 0.5:
    print("Tilted. Was up for ", tilt_switch.last_duration, tilt_switch.value)
    print(animations_list[list_pos])
    print(list_pos)
    list_pos = (list_pos + 1) % len(animations_list) 
    animations_list[0].fill((0,0,0))
    last_trigger_time = time.time()
    time.sleep(0.25)  
    
  #Okie, this works to debounce it and only run when it's upright _and_ only changes when you tilt it for more than 0.5s
  elif tilt_switch.value == False:
      print("Should be up now, was tilted for ", tilt_switch.last_duration)
      print(tilt_switch.value)
      animations_list[list_pos].animate()
  else:
      #print("Stable")
      animations_list[list_pos].animate()

  last_state = current_state  
