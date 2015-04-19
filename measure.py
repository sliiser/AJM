import time
import termo
import motor
import sys
import numpy as np

def scanArea(x0, y0, x1, y1):
  motor.goto(x0, y0);
  temps = [x[:] for x in [[0]*(X/STEP)]*(Y/STEP)]
  ty = 0
  for y in range(y0, y1, STEP):
    rang = (range(x0, x1, STEP) if (((y-y0) % (2*STEP)) == 0) else range(x1, x0, -STEP))
    tx = 0
    for x in rang:
      motor.goto(x,y)
      time.sleep(SLEEP_TIME)
      temps[ty][tx] = termo.temp();
      tx += 1
    ty += 1
  return temps

X, Y = 500, 600
X0, Y0 = 0,0
STEP = 100
SLEEP_TIME = 0.1

motor.setup(sys.argv)
termo.setup()

np.save('array.npy', scanArea(X0-X/2, Y0-Y/2, X0+X/2, Y0+Y/2))

motor.close()
termo.close()
