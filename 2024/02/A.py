import sys

total = 0
for line in sys.stdin:
	level = [int(x) for x in line.split()]
	vect = level[0] - level[1]
	safe = True

	for i in range(len(level) - 1):
		diff = level[i] - level[i + 1]
		if abs(diff) > 3 or diff * vect < 1:
			safe = False
			break
	if safe:
		total += 1

print(total)

