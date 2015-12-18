vowels = 'aeiou'
doubles = ["%s%s" % (l, l) for l in map(chr, range(97, 123))]
substrings = ['ab', 'cd', 'pq', 'xy']

def niceString(str):
	"""String is nice if it contains 3+ vowels, a letter that appears twice in a
	row and doesn't contain 'ab', 'cd', 'pq' or 'xy'."""
	numVowels = numDoubles = 0
	for i, c in enumerate(str):
		if numVowels < 3 and c in vowels: numVowels += 1
		if i < len(str)-1:
			substr = "%s%s" % (c, str[i+1])
			if numDoubles < 1 and substr in doubles: numDoubles += 1
			if substr in substrings: return False
	if numVowels >= 3 and numDoubles >= 1: return True
	return False

def nicerString(str):
	"""String is nicer if it contains matching pairs without overlap and one
	letter that repeats with a letter in between."""
	pairMatch = letterMatch = False
	for i, c in enumerate(str):
		if pairMatch is False and i < len(str)-3:
			pair = "%s%s" % (c, str[i+1])
			for j in xrange(i+2, len(str)-1):
				pair2 = "%s%s" % (str[j], str[j+1])
				if pair == pair2: pairMatch = True
		if letterMatch is False and i < len(str)-2:
			if c is str[i+2]: letterMatch = True
		if pairMatch and letterMatch: return True
	return False

with open("input") as f:
	input = f.read().split()
	numNiceStrings = 0
	numNicerStrings = 0

	for str in input:
		if niceString(str) is True: numNiceStrings += 1
		if nicerString(str) is True: numNicerStrings += 1
	print "%d strings are nice." % numNiceStrings
	print "%d strings are nicer." % numNicerStrings