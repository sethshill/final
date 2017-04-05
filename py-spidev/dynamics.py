# Dynamic function
# March 16, 2017
# Seth Shill
import numpy
from interpretMood import*

# Globals
dynamics = numpy.random.rand(100)
key = 'Amin';
mood = Mood(44,80);
rhythm = 44;


def displayDynamics( deltaT = 100, dynamics = None, key = None, mood = None, rythm = None, tempo = None):
"""Takes in a time delta, array of values corresponding to song dynamics (on a scale from 0.0 - 1.0), and an object called mood (the mood of the song). returns nothing but simulates a light show set to COLOR from genMood."""
	color = genMood(mood, key, rythm, dynamics, tempo)
