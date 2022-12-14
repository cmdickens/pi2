# this script will randomly display a color on the RGB LED sensor
# Sensor(s) required: "RGB LED"
# for git tag v0.1.0

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
    while True:
        n = random.randint(0,3)
        LED.setColor(colors[n])
        time.sleep(0.5)
        LED.noColor()
        time.sleep(0.5)

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:
		LED.destroy()
