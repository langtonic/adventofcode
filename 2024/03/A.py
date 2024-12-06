import sys

total = 0
for line in sys.stdin:
	parens = line.split(')')
	for segment in parens:
		seg = segment.split('mul(')[-1]
		try:
			a, b = (int(x) for x in seg.split(','))
		except:
			continue
		total += a*b

print(total)