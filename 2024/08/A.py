import sys

antennae = {}
antinodes = set()
r = 0

for line in sys.stdin:
	c = 0
	for char in line.strip():
		if char != '.':
			if char in antennae:
				antennae[char].append((r, c))
			else:
				antennae[char] = [(r, c)]
		c += 1
	r += 1

def legal(r, c, rlim, clim):
	if r >= 0 and r < rlim and c >= 0 and c < clim:
		return True
	return False

rows, cols = r, c
for network in antennae.values():
	for i in range(len(network) - 1):
		ir, ic = network[i]
		for j in range(i + 1, len(network)):
			jr, jc = network[j]

			dr, dc = ir - jr, ic - jc
			air, aic = ir + dr, ic + dc
			ajr, ajc = jr - dr, jc - dc

			if legal(air, aic, rows, cols):
				antinodes.add((air, aic))
			if legal(ajr, ajc, rows, cols):
				antinodes.add((ajr, ajc))

print(len(antinodes))
