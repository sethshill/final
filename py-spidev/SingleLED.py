# File: Single LED
# Author: Seth Shill
# Date Created: 2/22/2017
# Description: Lights a single LED on the Dotstar matrix display

import spidev
import time

# Include predefined list of values
from array import array
data_stream = array('B')
data_stream = [0] * 12

# Setup SPI
spi = spidev.SpiDev()
spi.open(0,0)	# Open bus 0, CE0 (bus 1 is at open(0,1))

while True:
	# START
	data_stream[0] = data_stream[1] = data_stream[2] = data_stream[3] = 0x00
	# DATA (add 4 bytes for every LED)
	data_stream[4] = 0xFF
	data_stream[5] = 0x00
	data_stream[6] = 0xFF
	data_stream[7] = 0x00
	# END
	data_stream[8] = data_stream[9] = data_stream[10] = data_stream[11] = 0xFF
	# Send data
	spi.xfer(data_stream)
	
