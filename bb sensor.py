import time
import board
import neopixel
import random
import digitalio as dio

bb = dio.DigitalInOut(board.D3)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP


while True:
    if not bb.value:

    else:



