times = input().strip().split(' ')
records = input().strip().split(' ')

def trimList(list):
	for i in range(len(list) - 1, -1, -1):
		if list[i] == '':
			list.pop(i)

def recordBreak(race):
	timeLimit = race[0]
	record = race[1]
	winningStrat = 0
	stratFound = False
	for i in range(0, timeLimit + 1, 1):
		distance = (timeLimit - i) * i
		if distance > record:
			winningStrat += 1
			stratFound = True
		elif stratFound:
			break
	return winningStrat

trimList(times)
trimList(records)

races = []
for i in range(1, len(times), 1):
	races.append((int(times[i]), int(records[i])))

product = 1
for race in races:
	product = product * recordBreak(race)

print(product)