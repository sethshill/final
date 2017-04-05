#from animation import StripChannelTest
#anim = StripChannelTest()
#anim.run()

from bibliopixel.led import*
from bibliopixel.animation import MatrixCalibrationTest
from bibliopixel.drivers.LDP8806 import*

#create driver for a 8*8 grid, use the size of your display
driver = DriverLDP8806(8*8)
led = LEDMatrix(driver)

anim = MatrixCalibrationTest(led)
anim.run()
