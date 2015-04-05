import sys
import serial
import time
import termo

def setup():
  if(len(sys.argv) != 2):
    print('Please provide 1 argument, the serial port')
    exit()
  global mootor
  mootor =  serial.Serial(sys.argv[1])

def close():
  mootor.close()

def goto(x,y):
  mootor.write("X%dgY%dg" % (x, y))


def scanArea(x0, y0, x1, y1):
  goto(x0, y0);
  for y in range(y0, y1, STEP):
    rang = (range(x0, x1, STEP) if y % 2*STEP == 0 else range(x1, x0, -STEP))
    for x in rang:
      goto(x,y)
      time.sleep(SLEEP_TIME)
      print termo.temp()

X, Y = 500, 500
X0, Y0 = 0,0
STEP = 100
SLEEP_TIME = 1

setup()
termo.setup()

scanArea(X0-X/2, Y0-Y/2, X0+X/2, Y0+Y/2)

close()
termo.close()
