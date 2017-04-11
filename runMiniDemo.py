# Test functions all together

#### Setup #####
# Setup configurations
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*
from bibliopixel.animation import*

# Global Vars
NUM = 8*8

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR) # 64 LEDs, 2 MHz speed using SPI, BRG order
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
		self.colorVal = color
		self.shapeVals = shapes
		
	def step(self, amt = 1):
		for i in range(len(self.shapeVals)):
			self._led.fillRect(self.shapeVals[i][0], self.shapeVals[i][1], self.shapeVals[i][2], self.shapeVals[i][3], self.colorVal)
		self._step += amt
	
	def testRect(self, x, y, w, h, color = None):
		self._led.fillRect(x, y, w, h, color)	
		print 'inside function'
		print x
		
def done():
	print 'Done'
			

# Create sample volumes
sampleVolumes = [0]*10
for i in range(0, 10):
	sampleVolumes[i] = random.random()
# Get color and shape from values
color = genColor(genMood(key='Cma'))
shapes = genShapes(sampleVolumes)
# Create object and set values
visualize = Visualize(led, color, shapes)
# Run object
#~ visualize.run(sleep = 500)
visualize.testRect(2,2,3,3,(255,0,0))
