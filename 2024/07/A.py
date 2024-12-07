import sys
import itertools

total = 0
for line in sys.stdin:
	target, vals = line.strip().split(':')
	target = int(target)
	vals = [int(x) for x in vals.split()]
	length = len(vals) - 1
	operators = [x for x in itertools.product('01', repeat=length)]
	
	for order in operators:
		attempt = vals[0]
		for i in range(length):
			if int(order[i]):
				attempt += vals[i + 1]
			else:
				attempt *= vals[i + 1]
		if attempt == target:
			total += target
			break
print(total)