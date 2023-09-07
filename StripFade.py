import time
import board
import neopixel

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.5)

color = [255, 0, 0]
decrease = 0
increase = 1
count = 0

while True:
    np.fill(color)
    np.show()
    time.sleep(0.03)
    if count == 255:
        decrease = (decrease + 1) % 3
        increase = (decrease + 1) % 3
    else:
        color[decrease] -= 1
        color[increase] += 1
    count = (count + 1) % 256

