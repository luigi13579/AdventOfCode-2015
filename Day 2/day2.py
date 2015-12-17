def calcPaperAmount(dimensions):
	"""Calculate the amount of wrapping paper needed for these dimensions."""
	first = dimensions[0] * dimensions[1]
	second = dimensions[0] * dimensions[2]
	third = dimensions[1] * dimensions[2]
	extra = min([first, second, third])
	return 2 * (first + second + third) + extra

def calcRibbonAmount(dimensions):
	"""Calculate the amount of ribbon required for these dimensions."""
	shortestPerimeter = 2 * (sum(dimensions) - max(dimensions))
	volume = dimensions[0] * dimensions[1] * dimensions[2]
	return shortestPerimeter + volume

with open("input") as f:
	input = f.read().split()
totalPaperAmount, totalRibbonAmount = 0, 0
for present in input:
	dimensions = [int(dimension) for dimension in present.split("x")]
	totalPaperAmount += calcPaperAmount(dimensions)
	totalRibbonAmount += calcRibbonAmount(dimensions)
print "Amount of wrapping paper needed: %s square feet." % totalPaperAmount
print "Amount of ribbon needed: %s feet." % totalRibbonAmount