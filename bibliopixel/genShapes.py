# Python file for generator shapes

def genShapes(volumes, shape=None):
	output = [];
	if shape is None:
		shape = 'square'

	#~ if shape is 'square':
		for i in range(len(volumes)):
			if volumes[i] < 0.25:
				output.append([3, 3, 2, 2])
			elif volumes[i] >= 0.25 and volumes[i] < 0.5:
				output.append([2, 2, 4, 4])
			elif volumes[i] >= 0.5 and volumes[i] < 0.75:
				output.append([1, 1, 6, 6])
			elif volumes[i] >= 0.75:
				output.append([0, 0, 8, 8])
				
	#~ elif shape is 'circle':
		#~ for i in range(len(volumes)):
			#~ if volumes[i] < 0.25:
				#~ output.append([3, 3, 1])
			#~ elif volumes[i] >= 0.25 and volumes[i] < 0.5:
				#~ output.append([3, 3, 2])
			#~ elif volumes[i] >= 0.5 and volumes[i] < 0.75:
				#~ output.append([3, 3, 3])
			#~ elif volumes[i] >= 0.75:
				#~ output.append([3, 3, 4])
	return output
