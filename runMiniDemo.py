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
off = (0,0,0)

class Visualize(BaseMatrixAnim):
	def __init__(self, led, color, shapes):
		super(Visualize, self).__init__(led)
		self._colorVal = color
		self._shapeVals = shapes
		self._numShapes = len(shapes)
		self._colors = [colors.Red, colors.Orange, colors.Green, colors.Blue, colors.Indigo]
		self._testShapes = [[1,1,6,6,colors.Green], [3,3,1,1,colors.Red], [2,2,4,4,colors.Orange]]
		
	def step(self, amt = 1):
		for i in range(self._led.numLEDs):
			self._led.fillRect(self._shapeVals[self._step][0], self._shapeVals[self._step][1], self._shapeVals[self._step][2], self._shapeVals[self._step][3], self._colorVal)
		self._step += amt
	
	#~ def step(self, amt = 1):
		#~ for i in range(self._led.numLEDs):
			#~ self._led.fillRect(1,1,6,6,self._colors[self._step])
		#~ if self._step % 2 == 0:
			#~ for i in range(self._led.numLEDs):
				#~ self._led.fillScreen(colors.Blue)
		#~ else:
			#~ for i in range(self._led.numLEDs):
				#~ self._led.fillRect(2,2,4,4,colors.Red)
		#~ self._step += amt

# Create sample volumes
sampleVolumes = [0]*10
for i in range(0, 10):
	sampleVolumes[i] = random.random()
# Get color and shape from values
color = genColor(genMood(key='Cma'))
shapes = genShapes(sampleVolumes)
# Create object and set values
visualize = Visualize(led, color, shapes)
print color, shapes
# Run object
visualize.run(sleep = 500, max_steps = len(visualize._colors))
