import time
import random
colors = ['R', 'G', 'B', 'Y']
# this script appends a value to a list
def append_list():
    n = random.randint(0,2)
    colors.append(colors[n])
    color_string = ''.join(colors)
    for i in range(0, len(colors)):
        print colors[i].lower()
        time.sleep(1)

if __name__ == '__main__':
    try:
        append_list()
    except KeyboardInterrupt:
        print 'Good bye'
