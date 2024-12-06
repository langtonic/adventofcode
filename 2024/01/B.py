import sys

l, d = [], {}
for line in sys.stdin:
	left, right = line.split()
	l.append(left)
	if right in d:
		d[right] += 1
	else:
		d[right] = 1

total = 0
for num in l:
	if num in d:
		total += (int(num) * d[num])
print(total)