import sys

sum = 0

for game in sys.stdin:
	validGame = True
	clueSet = game.replace(':', ';').strip().split(';')
	gameID = int(clueSet[0][5:])
	clueSet = clueSet[1:]
	for clue in clueSet:
		cubeNums = clue.split(',')
		for colour in cubeNums:
			number = colour.split(' ')
			if 'd' in number[2]:
				if int(number[1]) > 12:
					validGame = False
			if 'g' in number[2]:
				if int(number[1]) > 13:
					validGame = False
			if 'b' in number[2]:
				if int(number[1]) > 14:
					validGame = False
	if validGame:
		sum += gameID
print(sum)
