# Test Script for Monday Demo
from interpretMood import*
from time import sleep

# Mood Generation Demo
print('energy, stress \narousal,valence')

# Serious, magnificent and relaxed
displayMood( genMood(mood, 'Gmi', 90) ) 
sleep(2)
# Serious, pious, and intense
displayMood( genMood(mood, 'Dmi', 90) ) 
sleep(2)
# Obscure, plaintive, and intense
displayMood( genMood(mood, 'Fmi', 40) )
sleep(2)
# Joyful, pastoral, and relaxed
displayMood( genMood(mood, 'Ama', 40) )
sleep(2)

# To test LED colors
#~ values = [0]*7
#~ for i in range (7):
	#~ values[i] = 40 * i
#~ while True:
	#~ for r in values:
		#~ for g in values:
			#~ for b in values:
				#~ solid(r,g,b)
				#~ print r,g,b
				#~ sleep(1)
