from sense_hat import SenseHat
import time

# this script shows how to use the try:except structure

sense = SenseHat()
sense.clear()

def loop():
    while True:
       sense.set_pixel(1,6, (255, 0, 0))
       time.sleep(1)
       sense.set_pixel(1,6, (0, 0, 0))
       time.sleep(1)
if __name__== "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        sense.clear()
