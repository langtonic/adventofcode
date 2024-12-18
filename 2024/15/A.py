import sys

path = ''
grid = []
dirs = {'<':(0, -1), '>':(0, 1), '^':(-1, 0), 'v':(1, 0)}

r = 0
for line in sys.stdin:
	if line[0] == '#':
		row = []
		c = 0
		for char in line.strip():
			if char == '@':
				rob = (r, c)
			row.append(char)
			c += 1
		grid.append(row)
		r += 1
	else:
		path += line.strip()

for step in path:
	r, c = rob
	dr, dc = dirs[step]
	nr, nc = r + dr, c + dc
	if grid[nr][nc] == '.':
		grid[nr][nc], grid[r][c] = grid[r][c], grid[nr][nc]
		rob = (nr, nc)
	elif grid[nr][nc] == 'O':
		er, ec = nr, nc
		while grid[er][ec] == 'O':
			er += dr
			ec += dc
		if grid[er][ec] == '.':
			grid[er][ec], grid[r][c] = grid[r][c], grid[er][ec]
			grid[er][ec], grid[nr][nc] = grid[nr][nc], grid[er][ec]
			rob = (nr, nc)

total = 0
for r in range(len(grid)):
	for c in range(len(grid[0])):
		if grid[r][c] == 'O':
			total += ((100 * r) + c)
print(total)