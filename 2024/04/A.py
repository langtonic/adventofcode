import sys

grid = []
for line in sys.stdin:
	grid.append(line.strip())
rows, cols = len(grid), len(grid[0])
total = 0

steps = [(-1, -1), (0, -1), (1, -1),
		(-1, 0), (1, 0),
		(-1, 1), (0, 1), (1, 1)]

def legal(x, y, r, c):
	if y >= 0 and y < r and x >= 0 and x < c:
		return True
	return False

for i in range(rows):
	for j in range(cols):
		if grid[i][j] != 'X':
			continue
		for dr, dc in steps:
			nr, nc = dr + i, dc + j
			if legal(nc, nr, rows, cols) and grid[nr][nc] == 'M':
				nr, nc = dr + nr, dc + nc
				if legal(nc, nr, rows, cols) and grid[nr][nc] == 'A':
					nr, nc = dr + nr, dc + nc
					if legal(nc, nr, rows, cols) and grid[nr][nc] == 'S':
						total += 1
print(total)
