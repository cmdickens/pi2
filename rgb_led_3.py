# this script will display a string of colors appending a new color each cycle
# Sensors required: "RGB LED", "Passive Buzzer"
# for git tag v0.3.0

import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass

GPIO.setwarnings(False)

# RGB LED setup
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

# Passive Buzzer setup
frequencies = [220, 440, 880, 1760]
buzz_pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

def validate_guess(color_sequence_string, guess):
    if guess != color_sequence_string:
        print ("== incorrect ==")
        print ("The correct sequence is  ", color_sequence_string)
        print ("your incorrect guess was ", guess)
        Buzz.ChangeFrequency(55)
        Buzz.start(50)
        LED.setColor(colors[0])
        time.sleep(0.5)
        LED.setColor(colors[1])
        time.sleep(0.5)
        LED.setColor(colors[2])
        time.sleep(0.5)
        LED.setColor(colors[3])
        time.sleep(0.5)
        Buzz.stop()
        LED.destroy()
        exit()
    else:
        print ("correct, here is the next sequence")

def loop():
        n = random.randint(0,3)
        color_sequence = [colors[n]]
        frequency_sequence = [frequencies[n]]
        print ('Input the color sequence like: rbbgyg where r=red, b=blue, g=green, y=yellow')
        print ('press Enter to continue...')
        keypress = raw_input()
        time.sleep(1)

        while True:
            for i in range(0, len(color_sequence)):
                Buzz.ChangeFrequency(frequency_sequence[i])
                Buzz.start(50)
                LED.setColor(color_sequence[i])
                time.sleep(0.5)
                Buzz.stop()
                LED.noColor()
                time.sleep(0.5)
            guess = getpass('Guess the color sequence: ')
            color_sequence_string = ''.join(color_sequence)
            validate_guess(color_sequence_string, guess.upper())
            n = random.randint(0,3)
            color_sequence.append(colors[n])
            frequency_sequence.append(frequencies[n])
            time.sleep(2)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        LED.destroy()
