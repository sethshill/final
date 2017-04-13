# Just contains function to turn off LEDs
import spidev
from array import array


# Set global variables
numLEDs = 64

# Include predefined list of values
data_stream = array('B')
data_stream = [0] * (4*numLEDs + 8)
led,data = numLEDs, 4;
led_info = array('B')
led_info = [[0 for x in range(data)] for y in range(led)]


# Setup SPI
spi = spidev.SpiDev()
spi.open(0,0)	# Open bus 0, CE0 (bus 1 is at open(0,1))
# Settings
spi.max_speed_hz = 1000000
spi.mode = 0b01



def off():
	"""Turns off all LEDs."""
	
	index = 0;	# Set start index
	# Set led_info array brightness and colors
	for i in range(numLEDs):
		led_info[i][0] = 0xE0
		led_info[i][1] = 0x00
		led_info[i][2] = 0
		led_info[i][3] = 0
	# Set START bytes
	for start in range(4):
		data_stream[index] = 0x00 
		index += 1
	# Set DATA bytes
	for i in range(numLEDs):
		for j in range(4):
			data_stream[index] = led_info[i][j]
			index += 1
	# Set END bytes
	for i in range(4):
		data_stream[index] = 0xFF
		index += 1
	# Send data
	spi.xfer(data_stream)

