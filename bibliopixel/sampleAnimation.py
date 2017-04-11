# Sample animation example
from bibliopixel.led import*
from bibliopixel.drivers.APA102 import*
from animation import*
NUM = 8*8
driver = DriverAPA102(NUM, c_order = ChannelOrder.BGR)
led = LEDMatrix(driver, rotation = 2, vert_flip = True)

anim = MatrixChannelTest(led)
anim.run()
