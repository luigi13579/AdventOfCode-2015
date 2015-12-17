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

with open("input") as f:
	input = f.read().split()
	numNiceStrings = 0
	for str in input:
		if niceString(str) is True: numNiceStrings += 1
	print "%d strings are nice." % numNiceStrings