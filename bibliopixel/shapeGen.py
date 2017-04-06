# Python file for generator shapes
from bibliopixel.led import*
from bibliopixel.animation import MatrixCalibrationTest
from bibliopixel.drivers.APA102 import*
import bibliopixel.colors as colors
from LEDfuncs import*
from time import sleep
from animation import*
import numpy

# Global Vars
NUM = 8*8
rainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo, colors.Violet]
Red = colors.Red
Orange = colors.Orange
Yellow = colors.Yellow
Green = colors.Green
Blue = colors.Blue
Indigo = colors.Indigo
Violet = colors.Violet

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR) # 64 LEDs, 2 MHz speed using SPI, BRG order
led = LEDMatrix(driver,rotation = 2,vert_flip = True) # Correct Orientation

# class MakeShape:
# 	def __init__(self, array, arrayo):
# 		self.array = [];
# 		self.arrayOfRectangles = [];

# 	def makeInputs(self):

square = 0

def makeDisplay(volumes, color, shape=None):
	""" 
	- Takes in a string, shape to be generated (e.g. square, circle, etc.) - default is square
	- Takes in an array of ints, time series data of the rhythmic intensity or volume level
	- Takes in a tuple, the color corresponding to mood from color module
	- Returns an array of tuples, each corresponding to an appropriate input to the appropriate function
	"""
	if shape is None:
		shape = square

	animationInputs = [0]*len(volumes);		
	for i in range(0, len(volumes)):
		# assume shape is square
		if volumes[i] < 0.5:
			animationInputs[i] = (3, 3, 2, 2, color)
		elif volumes[i] >= 0.5 and volumes < 0.7:
			animationInputs[i] = (2, 2, 4, 5, color)
		elif volumes[i] >= 0.7 and volumes < 0.9:
			animationInputs[i] = (1, 1, 6, 6, color)
		elif volumes[i] >= 0.9:
			animationInputs[i] = (0, 0, 8, 8, color)
	
	return animationInputs;
	
def display(deltaT, animationInputs):
	for i in animationInputs:
		led.fillRect(animationInputs[i])
		sleep(deltaT)
