import board
import time
import digitalio as dio
from neopixel import NeoPixel

np = NeoPixel(board.NEOPIXEL, 1, auto_write = False, brightness = 0.5)

led = dio.DigitalInOut(board.LED)
led.direction = dio.Direction.OUTPUT

pir = dio.DigitalInOut(board.D2)
pir.direction = dio.Direction.INPUT

purple = [255, 255, 0]
red = [255, 0, 0]
white = [255, 255,255]
while True:
    if pir.value:
        np.fill(purple)
        np.show()
        time.sleep(0.05)
    else:
        np.fill(white)
        np.show()
        time.sleep(0.05)
        print(pir.value)
