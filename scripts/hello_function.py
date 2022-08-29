import time
# this script demonstrates how to use try:except structure
# with a function
def hello():
    print "Hello World!"
    time.sleep(10)

if __name__ == '__main__':
    try:
        hello()
    except KeyboardInterrupt:
        print 'Good Bye'
