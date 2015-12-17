import md5

def testHash(hash, digits, s):
	"""Return True if hash updated with digits begins with s."""
	hash.update(str(digits).encode('utf-8'))
	if hash.hexdigest().startswith(s):
		return True
	return False

def findDigits(key):
	"""Find digits such that hash of key + digits starts with 5/6 zeroes."""
	hash = md5.new()
	hash.update(key.encode('utf-8'))
	digits = 1
	answer1 = answer2 = 0
	while True:
		if answer1 == 0 and testHash(hash.copy(), digits, '00000') is True:
			answer1 = digits
		if testHash(hash.copy(), digits, '000000') is True:
			answer2 = digits
		if answer2 > 0: return (answer1, answer2)
		digits += 1

with open("input") as f:
	print "Digits to mine AdventCoin: %s, %s." % findDigits(f.read().rstrip())