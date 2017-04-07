# For testing python functions
from shapeGen import*
import random
from interpretMood import*
# from /Users/Seth/repos/BiblioPixel/bibliopixel import*

# Test shape generation

#~ sampleVolumes = [0]*10
#~ for i in range(0, 10):
	#~ sampleVolumes[i] = random.random()
	#~ print sampleVolumes[i]
#~ 
#~ color = genColor(genMood(key='Cma'))
#~ makeDisplay(sampleVolumes, 33, color)

# Basic Test
import bibliopixel.colors as colors
Red = colors.Red

fillRect(2,2,1,1,red)
