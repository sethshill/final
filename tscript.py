# For testing python functions
# Test writing my own animation
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*
import bibliopixel.colors as colors
from bibliopixel.animation import*
from time import sleep

#### Setup #####
# Global Vars
NUM = 8*8

#create driver for a 8*8 grid, use the size of your display
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR) # 64 LEDs, 2 MHz speed using SPI, BRG order
led = LEDMatrix(driver,rotation = 2,vert_flip = True) # Correct Orientation

class MatrixTest(BaseMatrixAnim):
	def __init__(self, led):
		super(MatrixTest, self).__init__(led)
		self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]
		
	def step(self, amt = 1):
		if self._step % 2 == 0:
			self._led.drawRect(2,2,4,4,colors.Indigo)
			#~ for i in range(self._led.numLEDs):
				#~ self._led.drawRect(-1, -1, i+1, i+1, self._colors[(self._step + i) % len(self._colors)])
		else:
			self._led.fillRect(1,1,6,6,colors.Orange)
		self._step += amt
		
def done():
	print 'Done'
			
anim = MatrixTest(led)
#~ anim.run(untilComplete = True, max_cycles = 1, callback = done)
anim.run(sleep = 500)
