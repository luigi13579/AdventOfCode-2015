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
	santa_x = santa_y = robo_x = robo_y = 0
	visited = Set()
	santa = True
	visited.add( (0, 0) )
	for d in directions:
		if santa == True:
			santa_x, santa_y = move(santa_x, santa_y, d, visited)
		else:
			robo_x, robo_y = move(robo_x, robo_y, d, visited)
		santa = not santa
	return len(visited)

with open("input") as f:
	input = f.read()
print "Santa visited %s unique houses." % calcNumHouses(input)