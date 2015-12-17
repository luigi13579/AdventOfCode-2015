from sets import Set

def move(x, y, direction, visited):
	if direction is '<': x -= 1
	elif direction is '>': x += 1
	elif direction is 'v': y -= 1
	elif direction is '^': y += 1
	visited.add( (x, y) )
	return (x, y)

def calcNumHouses(directions):
	"""Calculate the number of unique houses santa visits."""
	x = y = 0
	visited = Set()
	visited.add( (0, 0) )
	for d in directions:
		x, y = move(x, y, d, visited)
	return len(visited)

with open("input") as f:
	input = f.read()
print "Santa visited %s unique houses." % calcNumHouses(input)