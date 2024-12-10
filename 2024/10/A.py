import sys

topomap = []
heads = []
rows = 0
for line in sys.stdin:
	row = []
	cols = 0
	for t in line.strip():
		if t == '0':
			heads.append((rows, cols))
		row.append(int(t))
		cols += 1
	topomap.append(row)
	rows += 1

score = 0
paths = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for head in heads:
	seen = [[False for _ in range(cols)] for _ in range(rows)]
	seen[head[0]][head[1]] = True
	queue = [head]
	for r, c in queue:
		for dr, dc in paths:
			nr, nc = r + dr, c + dc
			if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
				if not seen[nr][nc] and topomap[nr][nc] == topomap[r][c] + 1:
					seen[nr][nc] = True
					queue.append((nr, nc))
					if topomap[nr][nc] == 9:
						score += 1
print(score)
