import sys

histories = []

for line in sys.stdin:
	history = [int(x) for x in line.strip().split(' ')]
	histories.append(history)

def nextValue(sequence):
	diffList = []
	nextDiff = None
	recur = False
	for i in range(len(sequence) - 1):
		diffList.append(sequence[i + 1] - sequence[i])
	for x in diffList:
		if not x == 0:
			recur = True
			break
	if recur:
		nextDiff = nextValue(diffList)
	else:
		nextDiff = 0
	return (sequence[-1] + nextDiff)

sum = 0
for history in histories:
	sum += nextValue(history)
print(sum)