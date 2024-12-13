import sys

grid = []
for line in sys.stdin:
	grid.append(line.strip())
	rows, cols = len(grid), len(grid[0])
checked = [[0 for _ in range(cols)] for _ in range(rows)]
adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]

plotnum = 0
for i in range(rows):
	for j in range(cols):
		if not checked[i][j]:
			plotnum += 1
			checked[i][j] = plotnum
			queue = [(i, j)]
			for r, c in queue:
				for dr, dc in adj:
					nr, nc = r + dr, c + dc
					if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
						if grid[nr][nc] == grid[i][j] and not checked[nr][nc]:
							checked[nr][nc] = plotnum
							queue.append((nr, nc))

plotar = [0 for _ in range(plotnum + 1)]
plotper = [0 for _ in range(plotnum + 1)]
for r in range(rows):
	for c in range(cols):
		k = checked[r][c]
		plotar[k] += 1
		for dr, dc in adj:
			nr, nc = r + dr, c + dc
			if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
				if checked[r][c] == checked[nr][nc]:
					continue
				else:
					plotper[k] += 1
			else:
				plotper[k] += 1

value = 0
for a, p in zip(plotar, plotper):
	value += (a * p)
print(value)