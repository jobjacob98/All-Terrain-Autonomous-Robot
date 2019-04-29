from serial import Serial
import sys, tty, termios
import _thread
import time
 

def getch():   
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def keypress():
	global char
	char = getch()
 
def main():
	ser = Serial('/dev/ttyUSB0', 9600)

	global char
	char = None
	_thread.start_new_thread(keypress, ())
 
	while True:
		if char is not None:
			_thread.start_new_thread(keypress, ())
			if char == 'w':
				print("up")
				ser.write(str.encode("UP"))
			if char == 's':
				print("down")
				ser.write(str.encode("DOWN"))
			if char == 'd':
				print("right")
				ser.write(str.encode("RIGHT"))
			if char == 'a':
				print("left")
				ser.write(str.encode("LEFT"))


			if char == 'q':
				exit()

			char = None
			time.sleep(1)


if __name__ == "__main__":
    main()








'''
from serial import Serial
import time
import sys, tty, termios
import _thread

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def keypress():
	global char
	char = getch()

def main():
	ser = Serial('/dev/ttyUSB0', 9600)

	global char
	char = None
	_thread.start_new_thread(keypress, ())

	while 1:
		if char is not None:
			_thread.start_new_thread(keypress, ())
			if char == 'q' or char == '\x1b':
				exit()
			char = None
		time.sleep(1)

'''






'''
	inkey = _Getch()

	while 1:
		key = inkey()

		print(key)
		if key == '\x1b[A':
			#print("up")
			ser.write(str.encode("UP"))
		if key == '\x1b[B':
			print("down")
			#ser.write(str.encode("DOWN"))
		if key == '\x1b[C':
			print("right")
			#ser.write(str.encode("RIGHT"))
		if key == '\x1b[D':
			print("left")
			#ser.write(str.encode("LEFT"))
		if key == '\x1b':
			exit()
'''
			
			
			
'''
			if event.type == pygame.QUIT:
				ser.close()
				break

			if event.type == pygame.KEYDOWN:		
				if event.key == pygame.K_UP:
					ser.write(str.encode("UP"))

				if event.key == pygame.K_DOWN:
					ser.write(str.encode("DOWN"))

				if event.key == pygame.K_LEFT:
					ser.write(str.encode("LEFT"))

				if event.key == pygame.K_RIGHT:
					ser.write(str.encode("RIGHT"))

				time.sleep(1)
'''


if __name__ == '__main__':
	main()