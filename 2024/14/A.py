import sys
import math

ROWS = 103
COLS = 101
quads = [0, 0, 0, 0]

for line in sys.stdin:
	loc, rate = (x.split('=')[1] for x in line.strip().split())
	c, r = (int(x) for x in loc.split(','))
	dc, dr = (int(x) * 100 for x in rate.split(','))
	fr, fc = (r + dr) % ROWS, (c + dc) % COLS

	if fr < ROWS // 2:
		if fc < COLS // 2:
			quads[0] += 1
		elif fc > COLS // 2:
			quads[2] += 1
	elif fr > ROWS // 2:
		if fc < COLS // 2:
			quads[1] += 1
		elif fc > COLS // 2:
			quads[3] += 1

print(math.prod(quads))