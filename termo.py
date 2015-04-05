import u12

def setup():
  global termomeeter
  termomeeter = u12.U12()

def close():
  termomeeter.close()

def v(n):
  return termomeeter.eAnalogIn(channel=n, gain=7)['voltage']

def avg(n, count):
  summa = 0
  for i in range(count):
    summa += v(n)
  return summa/float(count)

def temp(n = 20):
  return avg(8, n)*1000
