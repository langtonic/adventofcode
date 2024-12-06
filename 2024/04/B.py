import sys

grid = []
for line in sys.stdin:
	grid.append(line.strip())
rows, cols = len(grid), len(grid[0])
total = 0

steps = [(-1, -1), (1, -1)]
opps = {'M':'S', 'S':'M'}

def legal(x, y, r, c):
	if y >= 0 and y < r and x >= 0 and x < c:
		return True
	return False

for i in range(rows):
	for j in range(cols):
		if grid[i][j] != 'A':
			continue
		xs = 0
		for dr, dc in steps:
			nr, nc = dr + i, dc + j
			if legal(nc, nr, rows, cols) and (grid[nr][nc] == 'M' or grid[nr][nc] == 'S'):
				opr, opc = i - dr, j - dc
				if legal(opc, opr, rows, cols) and grid[opr][opc] == opps[grid[nr][nc]]:
					xs += 1
		total += (xs // 2)
print(total)
