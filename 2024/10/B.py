import sys

topomap = []
heads = []
queue = []
rows = 0
for line in sys.stdin:
	row = []
	cols = 0
	for t in line.strip():
		if t == '0':
			heads.append((rows, cols))
		elif t == '9':
			queue.append((rows, cols))
		row.append(int(t))
		cols += 1
	topomap.append(row)
	rows += 1


ratings = [[0 for _ in range(cols)] for _ in range(rows)]

paths = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r, c in queue:
	ratings[r][c] = 1
for r, c in queue:
	for dr, dc in paths:
		nr, nc = r + dr, c + dc
		if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
			if topomap[nr][nc] == topomap[r][c] - 1:
				if not ratings[nr][nc]:
					queue.append((nr, nc))
				ratings[nr][nc] += ratings[r][c]

score = 0
for r, c in heads:
	score += ratings[r][c]
print(score)