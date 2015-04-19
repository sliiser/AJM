import serial

def setup(argv):
  if(len(argv) != 2):
    print('Please provide 1 argument, the serial port')
    exit()
  global mootor
  mootor =  serial.Serial(argv[1])
  mootor.write("B1w0=")

def close():
  mootor.write("B0w0g")
  mootor.close()

def goto(x,y):
  mootor.write("X%dgY%dgBi  " % (x, y))
