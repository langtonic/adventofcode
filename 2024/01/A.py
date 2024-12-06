import sys

listA, listB = [], []
for line in sys.stdin:
	locs = line.split()
	listA.append(int(locs[0]))
	listB.append(int(locs[1]))
listA.sort()
listB.sort()

total = 0
for i in range(len(listA)):
	diff = abs(listA[i] - listB[i])
	total += diff

print(total)
