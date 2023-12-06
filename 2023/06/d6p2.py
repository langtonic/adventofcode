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

def digitConcat(list):
	fullNum = ''
	for i in range(1, len(list), 1):
		fullNum += list[i]
	return int(fullNum)	

trimList(times)
trimList(records)
time = digitConcat(times)
record = digitConcat(records)

print(recordBreak((time, record)))