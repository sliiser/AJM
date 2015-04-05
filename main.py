import sys
import serial
import time

def setup():
  if(len(sys.argv) != 2):
    print('Please provide 1 argument, the serial port')
    exit()

  return serial.Serial(sys.argv[1])

def goto(x,y):
  s.write("X%dgY%dg" % (x, y))


def scanArea(x0, y0, x1, y1, step):
  goto(x0, y0);
  for y in range(y0, y1, step):
    rang = (range(x0, x1, step) if y % 2*step == 0 else range(x1, x0, -step))
    for x in rang:
      goto(x,y)
      time.sleep(SLEEP_TIME)

X = 500
Y = 500
X0 = 0
Y0 = 0
SLEEP_TIME = 1

s = setup()

scanArea(X0-X/2, Y0-Y/2, X0+X/2, Y0+Y/2, 100)

s.close()
