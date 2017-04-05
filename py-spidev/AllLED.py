# File: All LED
# Author: Seth Shill
# Date Created: 2/22/2017
# Description: Lights all LEDs on the Dotstar matrix display

import spidev
import time

numLEDs = 64

# Include predefined list of values
from array import array
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

def setOneColor(r, g, b, brightness):
	"""Sets the entire 64-LED matrix one color based on r, g, b value and brightness. The first 3 values are ints ranging 0-255, where 255 is full brightness. brightness is a variable 0 to 1.0"""
	
	index = 0;	# Set start index
	# Set led_info array brightness and colors
	for i in range(numLEDs):
		led_info[i][0] = 0xFF
		led_info[i][1] = b
		led_info[i][2] = g
		led_info[i][3] = r
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
