from serial import Serial

PORT = '/dev/ttyUSB2'
BAUD = 9600

ser = Serial(PORT, BAUD)

if ser.isOpen:
  print("hello")

while True:
  data = ser.readline()
  print(data)

ser.close()
