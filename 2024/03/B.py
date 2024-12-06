import sys

total = 0
wholeblock = ''
for line in sys.stdin:
	wholeblock += line.strip()

blocks = wholeblock.split('do()')
for block in blocks:
	do = block.split('don\'t()')[0]
	parens = do.split(')')
	for segment in parens:
		seg = segment.split('mul(')[-1]
		try:
			a, b = (int(x) for x in seg.split(','))
			total += (a * b)
		except:
			continue
print(total)
