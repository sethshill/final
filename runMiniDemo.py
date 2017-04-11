# Test functions all together
# Import input generation functions
from bibliopixel.shapeGen import*
import random
from bibliopixel.interpretMood import*
from time import sleep

# Setup configurations
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*

#### Setup #####
# Global Vars
NUM = 8*8

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR) # 64 LEDs, 2 MHz speed using SPI, BRG order
led = LEDMatrix(driver,rotation = 2,vert_flip = True) # Correct Orientation

class Visualize(BaseMatrixAnim):
	def __init__(self, led):
		super(MatrixTest, self).__init__(led)
		
	def step(self, amt = 1):
		self._step += amt
		
def done():
	print 'Done'
			

# Create sample volumes
sampleVolumes = [0]*10
for i in range(0, 10):
	sampleVolumes[i] = random.random()
# make functions
color = genColor(genMood(key='Cma'))
makeDisplay(sampleVolumes, 100, color)
