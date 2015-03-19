import sys
import serial
import time

if(len(sys.argv) != 2):
  print('Please provide 1 argument, the serial port')
  exit()

s = serial.Serial(sys.argv[1])

while(True):
  cmd = input()
  if(cmd == 'exit'):
    s.close()
    exit()
  s.write(bytearray(cmd,'ascii'))

  time.sleep(0.1)
  out = ''
  while s.inWaiting() > 0:
    out += str(s.read(1).decode('ascii'))
  if(out != ''):
    print(out)