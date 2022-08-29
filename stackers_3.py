import time
import sys
import pygame
from sense_hat import SenseHat
from pygame.locals import *

sense = SenseHat()
sense.clear()
# this script moves a pixel across the bottom row and then stays lit and then
# moves to the next row when the spacebar is pressed
# for git tag v0.3.0
class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 400)
        speed = 0.3
        column = 0
        row = 7
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    sense.set_pixel((column - 1), row, (0, 255, 255))
                    column = 0
                    row-= 1
                    if (row < 0):
                        sense.show_message("Winner")
                        print ("game over")
                        self.gaming = False
                else:
                    sense.set_pixel(column, row, (0, 255, 0))
                    time.sleep(speed)
                    sense.set_pixel(column, row, (0, 0, 0))
                    column+= 1
                    if (column == 8):
                        column = 0
                    if (row == 4):
                        speed = 0.3
                    if (row == 0):
                        speed = 0.1

if __name__== "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
