# this script will display a string of colors with sound appending a new color each cycle
# Sensor(s) required: "RGB LED", "Passive Buzzer"
# for git tag v0.3.0

import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

GPIO.setwarnings(False)

# RGB LED setup
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Passive Buzzer setup
buzz_pin = 32
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

frequencies = [220, 440, 880, 1760]

def loop():
        n = random.randint(0,3)
        color_sequence = [colors[n]]
        frequency_sequence = [frequencies[n]]

        while True:
            for i in range(0, len(color_sequence)):
                Buzz.ChangeFrequency(frequency_sequence[i])
                Buzz.start(50)
                LED.setColor(color_sequence[i])
                time.sleep(0.5)
                Buzz.stop()
                LED.noColor()
                time.sleep(0.3)
            n = random.randint(0,3)
            color_sequence.append(colors[n])
            frequency_sequence.append(frequencies[n])
            time.sleep(1)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        LED.destroy()
