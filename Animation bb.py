"""
This example displays the basic animations in sequence, at a five second interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example may not work on SAMD21 (M0) boards.
"""
import board
import neopixel
import digitalio as dio
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import PURPLE, WHITE, AMBER, JADE, TEAL, PINK, MAGENTA, ORANGE
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

bb = dio.DigitalInOut(board.D3)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP

# Update to match the pin connected to your NeoPixels
pixel_pin = board.D2
# Update to match the number of NeoPixels you have connected
pixel_num = 32

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

solid = Solid(pixels, color=PINK)
blink = Blink(pixels, speed=0.1, color=JADE)
colorcycle = ColorCycle(pixels, speed=0.5, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(pixels, speed=0.01, color=WHITE, size=3, spacing=6)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(pixels, speed=0.01, color=AMBER, period=3)


animations = AnimationSequence(
    comet,
    pulse,
    chase,
    advance_interval=5,
    auto_clear=True,
)

rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.1, tail_length=7, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations2 = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    if not bb.value:
        animations.animate()
    else:
        animations2.animate()


