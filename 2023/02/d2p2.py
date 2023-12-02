import sys

sum = 0

for game in sys.stdin:
	redMinimum = 0
	greenMinimum = 0
	blueMinimum = 0
	clueSet = game.replace(':', ';').strip().split(';')
	gameID = int(clueSet[0][5:])
	clueSet = clueSet[1:]
	for clue in clueSet:
		cubeNums = clue.split(',')
		for colour in cubeNums:
			number = colour.split(' ')
			if 'red' == number[2]:
				if int(number[1]) > redMinimum:
					redMinimum = int(number[1])
			if 'green' == number[2]:
				if int(number[1]) > greenMinimum:
					greenMinimum = int(number[1])
			if 'blue' == number[2]:
				if int(number[1]) > blueMinimum:
					blueMinimum = int(number[1])
	power = redMinimum * greenMinimum * blueMinimum
	sum += power
print(sum)
