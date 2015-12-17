def calcFloorAndBasementIndex(input):
	"""Calculate floor and first basement index."""
	floor = index = found = 0
	for c in input:
		if c is '(':
			floor += 1
		elif c is ')':
			floor -= 1
		if not found:
			index += 1
			if floor < 0:
				found = 1
	return (floor, index)

with open("input") as f:
	input = f.read()
print "Santa is on floor %s and entered basement at %s." % \
	(calcFloorAndBasementIndex(input))