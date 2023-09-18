import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 1)
purple = [255, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0,255,37]
times = 1

'''

Function: fadeOut

Description: The function has a set color across all of the LEDs and then reverts to black in a fade.

Parameters: (color, speed(float))

Return value: Prints the values of the colors.

'''
def fadeOut(color, speed=0.01):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: fadeIn

Description: Starts at black and fades into a set color

Parameters: (color, speed(float))

Return value: Prints the values of the colors.

'''
def fadeIn(color, speed=0.01):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        np.show()
        time.sleep(speed)
        print(color1)

'''

Function: chase

Description: A set color moves in intervals of 2 around the LEDs in a loop. The background and foreground colors differ.

Parameters: color(list), speed(float)

Return value: Prints both colors values. 

'''
        
def chase(color = [0,0,0], speed = 0.01):
    for j in range(30):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = green
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(speed)
            
'''

Function: sparkle

Description: Uses a random integer to have a set color appear in the foreground of the LED.

Parameters: color(list), times

Return value: none

'''

def sparkle(color = [0,0,0], times = 1):
    for i in range(times):
        np.fill(color)
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [255,0,255]
        np[led2] = [255,255,255]
        np[led3] = [0,0,0]
        np.show()
        time.sleep(0.9)

while True:
    fadeOut(purple)
    fadeIn(blue)
    fadeOut(blue)
    fadeIn(white)
    fadeOut(white)
    fadeIn(purple)
    sparkle(purple, 5)
    fadeOut(white)
    chase()
    fadeOut(green)
