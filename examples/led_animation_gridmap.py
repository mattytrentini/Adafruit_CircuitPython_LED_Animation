"""
This example shows usage of the gridmap helper to easily treat a single strip as a horizontal or
vertical grid for animation purposes.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example does not work on SAMD21 (M0) boards.
"""
import board
import neopixel

import adafruit_led_animation.animation.comet as comet_animation
import adafruit_led_animation.animation.rainbowcomet as rainbowcomet_animation
import adafruit_led_animation.animation.rainbowchase as rainbowchase_animation
import adafruit_led_animation.animation.chase as chase_animation
import adafruit_led_animation.animation.rainbow as rainbow_animation
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation import helper
from adafruit_led_animation.color import PURPLE, JADE, AMBER


pixels = neopixel.NeoPixel(board.D6, 32, brightness=0.2, auto_write=False)

pixel_wing_vertical = helper.PixelMap.vertical_lines(
    pixels, 8, 4, helper.horizontal_strip_gridmap(8, alternating=False)
)
pixel_wing_horizontal = helper.PixelMap.horizontal_lines(
    pixels, 8, 4, helper.horizontal_strip_gridmap(8, alternating=False)
)

comet_h = comet_animation.Comet(
    pixel_wing_horizontal, speed=0.1, color=PURPLE, tail_length=3, bounce=True
)
comet_v = comet_animation.Comet(
    pixel_wing_vertical, speed=0.1, color=AMBER, tail_length=6, bounce=True
)
chase_h = chase_animation.Chase(
    pixel_wing_horizontal, speed=0.1, size=3, spacing=6, color=JADE
)
rainbow_chase_v = rainbowchase_animation.RainbowChase(
    pixel_wing_vertical, speed=0.1, size=3, spacing=2, wheel_step=8
)
rainbow_comet_v = rainbowcomet_animation.RainbowComet(
    pixel_wing_vertical, speed=0.1, tail_length=7, bounce=True
)
rainbow_v = rainbow_animation.Rainbow(pixel_wing_vertical, speed=0.1, period=2)
rainbow_chase_h = rainbowchase_animation.RainbowChase(
    pixel_wing_horizontal, speed=0.1, size=3, spacing=3
)

animations = AnimationSequence(
    rainbow_v,
    comet_h,
    rainbow_comet_v,
    chase_h,
    rainbow_chase_v,
    comet_v,
    rainbow_chase_h,
    advance_interval=5,
)

while True:
    animations.animate()