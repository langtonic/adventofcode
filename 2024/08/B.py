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

			ilegal = jlegal = True
			itr = jtr = 0
			while(ilegal):
				air, aic = ir + (dr * itr), ic + (dc * itr)
				if ilegal := legal(air, aic, rows, cols):
					antinodes.add((air, aic))
				itr += 1
			while(jlegal):
				ajr, ajc = jr - (dr * jtr), jc - (dc * jtr)
				if jlegal := legal(ajr, ajc, rows, cols):
					antinodes.add((ajr, ajc))
				jtr += 1

print(len(antinodes))
