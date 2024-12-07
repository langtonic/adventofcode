import sys
import itertools

total = 0
for line in sys.stdin:
	target, vals = line.strip().split(':')
	target = int(target)
	vals = [int(x) for x in vals.split()]
	length = len(vals) - 1
	operators = [x for x in itertools.product('012', repeat=length)]
	
	for order in operators:
		attempt = vals[0]
		for i in range(length):
			match order[i]:
				case '0':
					attempt += vals[i + 1]
				case '1':
					attempt *= vals[i + 1]
				case '2':
					attempt = int(str(attempt) + str(vals[i + 1]))
		if attempt == target:
			total += target
			break
print(total)