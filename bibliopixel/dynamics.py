# Dynamic function
# March 16, 2017
# Seth Shill
import numpy
from interpretMood import*
import bibliopixel.colors as colors
from LEDfuncs import*
from time import sleep
from animation import*

# Globals
dynamics = numpy.random.rand(100)
key = 'Amin';
mood = Mood(44,80);
rhythm = 44;


def displayDynamics( deltaT = 100, dynamics = None, moo:
	"""Takes in a time delta, array of values corresponding to song dynamics (on a scale from 0.0 - 1.0), and an object called mood (the mood of the song). Returns nothing but simulates a light show set to COLOR from genMood."""
	
	#~ color = genMood(mood, key, rythm, tempo)
	color = colors.Red
	
	for i in range(dynamics.length):
		if (0 < dynamics[i] < 0.25):
			led.drawRect(3, 3, 2, 2, color)
		if ( 0.25 < dynamics[i] < 0.5 ):
			led.drawRect(2, 2, 4, 4, color)
		if ( 0.5 < dynamics[i] < 0.75 ):
			led.drawRect(1, 1, 6, 6, color)
		else:
			led.drawRect(0, 0, 8, 8, color)
		led.update()
		sleep(1)
