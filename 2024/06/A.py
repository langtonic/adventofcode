import sys

grid = []
r = 0
guard = None
for line in sys.stdin:
	row = []
	c = 0
	for char in line.strip():
		row.append(char)
		if char == '^':
			guard = (r, c)
		c += 1
	grid.append(row)
	r += 1

grid[guard[0]][guard[1]] = 'X'
moves = {'U': (-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
rotation = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
coverage = 1
direction = 'U'

while(True):
	dr, dc = moves[direction]
	r, c = guard
	nr, nc = dr + r, dc + c
	if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
		if grid[nr][nc] == '#':
			direction = rotation[direction]
		else:
			guard = (nr, nc)
			if grid[nr][nc] == '.':
				grid[nr][nc] = 'X'
				coverage += 1
	else:
		print(coverage)
		break
