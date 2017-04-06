# For testing python functions
from shapeGen import*
import random
from interpretMood import*
# from /Users/Seth/repos/BiblioPixel/bibliopixel import*

# Test shape generation

sampleVolumes = [0]*10
for i in range(0, 10):
	sampleVolumes[i] = random.random()

color = genColor(genMood(key='Cma'))
animationInputs = makeDisplay(sampleVolumes, color)
#~ display(1, animationInputs)
