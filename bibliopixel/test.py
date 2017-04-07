# Configuration test file

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

#########################################################################################
# Test script

#~ # For calibrating orientation & colors
#~ anim = MatrixCalibrationTest(led)
#~ anim.run()

# Matrix Channel Test
anim = MatrixChannelTest(led)
anim.run()

fillRect(2,2,1,1,orange)
#~ # Set Brightness
#~ led.setMasterBrightness(255)

#~ # Set one LED
#~ led.set(3,3,(255,255,255))	# Set LED @ x=3,y=3, to color (255,255,255)

# Set all LEDs 1 color
#~ tex = []
#~ for i in range(0,8):
	#~ row = []
	#~ for j in range(0,8):
		#~ row.append((255,0,0))
	#~ tex.append(row)
	
#~ w, h = 8, 8
#~ tex = [[(0,255,0) for x in range(w)] for y in range(h)]
#~ led.setTexture(tex)
#~ print "test"
#~ led.update()

# Create a circle with white background
#~ led.setTexture(tex = Blue)
#~ print led.get(1,1)
#~ print led.texture
#~ led.update()
#~ sleep(1)
#~ off()
#~ sleep(1)
#~ led.drawCircle(3,3,2,Blue)
#~ led.update()
#~ anim = MatrixChannelTest(led)
#~ anim.run()

#~ # Make Animation with Growing Rectangle
#~ while True:
#~ led.drawRect(3, 3, 2, 2, Red)
#~ led.update()
#~ sleep(1)
#~ led.drawRect(2, 2, 4, 4, Red)
#~ led.update()
#~ sleep(1)
#~ led.drawRect(1, 1, 6, 6, Red)
#~ led.update()
#~ sleep(1)
#~ led.drawRect(0, 0, 8, 8, Red)
#~ led.update()
#~ off()
#~ sleep(1)	
	
#~ # Use base animation
#~ class MatrixTest(BaseMatrixAnim):
	#~ def __init__(self, led):
		#~ #The base class MUST be initialized by calling super like this
		#~ super(MatrixTest, self).__init__(led)
		#~ #Create a color array to use in the animation
		#~ self._colors = [Red, Orange, Yellow, Green, Blue]
		#~ 
	#~ def step(self, amt = 1):
		#~ #Fill the strip, with each successive color
		#~ for i in range(self._led.numLEDs):
			#~ self._led.drawRect(-1, -1, i+1, i+1, self._colors[(self._step + i) % len(self._colors)])
		#~ #Increment the internal step by the given amount
		#~ self._step += amt
	#~ def step(self, amt = 1):
		#~ self._led.fill((self._step, 0, 0))
		#~ self._step += amt
		#~ if self._step > 255:
			#~ self._step = 0
			#~ 
#~ anim = MatrixTest(led)
#~ anim.run()

array = numpy.random.rand(100)
