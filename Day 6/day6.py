import re

regex = re.compile('[0-9]+,[0-9]+')

def sanitizeInput(line):
	if line.startswith('to'): action = 'tog'
	elif line.startswith('turn on'): action = 'on'
	else: action = 'off'
	coords = regex.findall(line)
	coord1 = map(int, coords[0].split(','))
	coord2 = map(int, coords[1].split(','))
	return (action, (coord1, coord2))

def performAction(action, state, x, y, coord1, coord2):
	"""Determines whether the light will be on or off after this action."""
	if x < coord1[0] or x > coord2[0]: return state
	if y < coord1[1] or y > coord2[1]: return state
	if action == 'on': return True
	elif action == 'off': return False
	else:
		if state == False: return True
		else: return False

def performActionB(action, state, x, y, coord1, coord2):
	"""Determines brightness of light after this action."""
	if x < coord1[0] or x > coord2[0]: return state
	if y < coord1[1] or y > coord2[1]: return state
	if action == 'on': return state + 1
	elif action == 'off':
		state -= 1
		if state < 0: return 0
		else: return state
	else: return state + 2

with open("input") as f:
	actions = []
	for line in f:
		actions.append(sanitizeInput(line))

mode = raw_input('Check the number of lights that are on (1) or the total'
	' brightness (2)?')
if mode == '1':
	default = False
	actionFunction = performAction
else:
	default = 0
	actionFunction = performActionB
lightStatus = 0
for x in xrange(0, 1000):
	for y in xrange(0, 1000):
		on = default
		for action in actions:
			on = actionFunction(action[0], on, x, y, action[1][0], action[1][1])
		lightStatus += on

if mode == '1': print "There are %i lights on." % lightStatus
else: print "Total light brightness: %i." % lightStatus