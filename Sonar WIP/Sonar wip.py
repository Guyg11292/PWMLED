import time
import board
import neopixel
import random
from neopixel import NeoPixel
import digitalio as dio
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 1)
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D3)


red = (255, 0, 0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
purple = (255,0,255)
yellow = (255, 100, 0)
orangeT = (255, 80, 0)
orange = (255, 64, 0)
lightBlue = (87, 232, 255)
lightpurple = (227, 98, 255)
darkpurple = (18,0,18)
defaultcolor = [216, 231, 0]
defcolor = [orange, yellow, orangeT]
randcolor = random.choice(defcolor)
defcolor2 = [lightBlue, lightBlue, white]
randcolor2 = random.choice(defcolor2)

color1 = [defaultcolor[0],defaultcolor[1],defaultcolor[2]]
np.fill(color1)

def lightning(bgcolor = darkpurple, flash = randcolor2, numpix = np.n):
    for i in range(5):
        randomsleep = random.random()*10
        randompix = random.randrange(3,8)
        print("sleep", randomsleep)
        np.fill(bgcolor)
        np.show()
        time.sleep(randomsleep)
        for j in range(randompix):
            np.fill(flash)
            np.show()
            time.sleep(0.05)
            np.fill(bgcolor)
            np.show()
            time.sleep(0.01)

distance = sonar.distance
            
while True:
    try:
        if sonar.distance <= 75:
            print((sonar.distance))
            np.fill(green)
            np.show()
        elif distance <= 50:
            print((sonar.distance))
            np.fill(red)
            np.show()
        else:
            print((sonar.distance))
            np.fill(yellow)
            np.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
