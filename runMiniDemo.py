# Test functions all together

#### Setup #####
# Setup configurations
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*
from bibliopixel.animation import*

# Global Vars
NUM = 8*8

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR, SPISpeed = 16) # 64 LEDs, 2 MHz speed using SPI, BRG order
led = LEDMatrix(driver,rotation = 2,vert_flip = True) # Correct Orientation

##### Key Functions #####
# Import input generation functions
from bibliopixel.genShapes import genShapes
from bibliopixel.interpretMood import*
from time import sleep

# For testing
import random

class Visualize(BaseMatrixAnim):
	def __init__(self, led, color, shapes):
		super(Visualize, self).__init__(led)
		self._colorVal = color
		self._shapeVals = shapes
		self._numShapes = len(shapes)
		
	def step(self, amt = 1):
		# Set background
		for i in range(self._led.numLEDs):
			#~ self._led.fillScreen(colors.Blue)
			self._led.all_off()
		# Set shape
		for i in range(self._led.numLEDs):
			self._led.fillRect(self._shapeVals[self._step][0], self._shapeVals[self._step][1], self._shapeVals[self._step][2], self._shapeVals[self._step][3], self._colorVal)
		self._step += amt

# Create sample volumes
sampleVolumes = [0]*100
for i in range(0, 100):
	sampleVolumes[i] = random.random()
# Get color and shape from values
color = genColor(genMood(key='Cma'))
shapes = genShapes(sampleVolumes)
# Create object and set values
visualize = Visualize(led, color, shapes)
# Run object
visualize.run(sleep = 100, max_steps = visualize._numShapes)
