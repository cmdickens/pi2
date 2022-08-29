import time
import sys
import pygame
from sense_hat import SenseHat
from pygame.locals import *
# this script moves a pixel across the bottom row of the Pi Sense HAT
# and stops when the spacebar is pressed
# for git tag v0.2.0
sense = SenseHat()
sense.clear()

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 600)
        speed = 0.3
        column = 0
        row = 7
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    sense.set_pixel((column - 1), row, (0, 255, 255))
                    self.gaming = False
                else:
                    sense.set_pixel((column), row, (0, 255, 255))
                    time.sleep(speed)
                    sense.set_pixel((column), row, (0, 0, 0))
                    time.sleep(speed)
                    column += 1
                    if (column == 8):
                        column = 0
if __name__== "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
