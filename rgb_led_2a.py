# this script will display a string of colors appending a new color each cycle
# Sensor(s) required: "RGB LED"
# initial approach for git tag v0.2.0

import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def loop():
    n = random.randint(0,3)
    color_sequence = [colors[n]]
    while True:
        for color in color_sequence:
            LED.setColor(color)
            time.sleep(0.5)
            LED.noColor()
            time.sleep(0.2)
        n = random.randint(0,3)
        color_sequence.append(colors[n])
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        LED.destroy()
