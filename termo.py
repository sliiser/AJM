import u12
import time

d = u12.U12()

def mV(n):
  return str(v(n)*1000) + " mV"

def v(n):
  return d.eAnalogIn(channel=n, gain=7)['voltage']

def avg(n):
  summa = 0
  for i in range(10):
    summa += v(n)
  return summa/10.0

while(1):
  print avg(8)
  print
  time.sleep(1)

