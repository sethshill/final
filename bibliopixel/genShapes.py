# Python file for generator shapes

#Global Vars
square = 0 #arbitrary

def genShapes(volumes, shape=None):
	output = [];
	if shape is None:
		shape = square # I may add different shapes later

	for i in range(len(volumes)):
		# assume shape is square
		if volumes[i] < 0.5:
			output.append([3, 3, 2, 2])
		elif volumes[i] >= 0.5 and volumes[i] < 0.7:
			output.append([2, 2, 4, 4])
		elif volumes[i] >= 0.7 and volumes[i] < 0.9:
			output.append([1, 1, 6, 6])
		elif volumes[i] >= 0.9:
			output.append([0, 0, 8, 8])
	return output
