# Python file for generator shapes
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*

import time
from animation import*
from interpretMood import*
import random
# Global Vars
NUM = 8*8

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR) # 64 LEDs, 2 MHz speed using SPI, BRG order
led = LEDMatrix(driver,rotation = 2,vert_flip = True) # Correct Orientation

square = 0

def makeDisplay(volumes, deltaT, color, shape=None):
	""" 
	- Takes in a string, shape to be generated (e.g. square, circle, etc.) - default is square
	- Takes in an array of ints, time series data of the rhythmic intensity or volume level
	- Takes in a tuple, the color corresponding to mood from color module
	- Returns an array of tuples, each corresponding to an appropriate input to the appropriate function
	"""
	if shape is None:
		shape = square

	for i in range(0, len(volumes)):
		millis = int(round(time.time() * 1000))
		# assume shape is square
		if volumes[i] < 0.5:
			led.fillRect(3, 3, 2, 2, color)
		elif volumes[i] >= 0.5 and volumes < 0.7:
			led.fillRect(2, 2, 4, 5, color)
		elif volumes[i] >= 0.7 and volumes < 0.9:
			led.fillRect(1, 1, 6, 6, color)
		elif volumes[i] >= 0.9:
			led.fillRect(0, 0, 8, 8, color)
		while (int(round(time.time() * 1000)) - millis < deltaT):
			pass 
