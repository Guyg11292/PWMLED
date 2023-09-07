import time
import board
import neopixel

np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness = 0.5)

color = [255, 0, 255]
decrease = 0
increase = 1
count = 0

while True:
    for i in range(0, 30, 2):
        np[i] = [255, 0, 255]
        time.sleep(0.05)
        np[i] = [0, 0, 0]
        time.sleep(0.1)
        np[i] = [255, 255, 255]

