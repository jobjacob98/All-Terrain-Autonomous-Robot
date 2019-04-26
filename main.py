from xbee import XBee
from serial import Serial

PORT = '/dev/ttyUSB1'
BAUD = 9600

ser = Serial(PORT, BAUD)

xbee = XBee(ser)

xbee.tx(dest_addr='\x00\x01', data='Hi Raspberry Pi')

print(xbee.wait_read_frame())

ser.close()
