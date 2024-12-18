ROWS = 103
COLS = 101
robots = []

startgrid = [['.' for _ in range(COLS)] for _ in range(ROWS)]

with open('input', 'r') as file:
	for line in file:
		loc, rate = (x.split('=')[1] for x in line.strip().split())
		c, r = (int(x) for x in loc.split(','))
		dc, dr = (int(x) for x in rate.split(','))
		fr, fc = (r + dr) % ROWS, (c + dc) % COLS
		robots.append((r, c, dr, dc))
		startgrid[r][c] = 'X'

calcrobots = robots.copy()
maxadj = []
for i in range(ROWS * COLS):
	grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
	for j in range(len(calcrobots)):
		r, c, dr, dc = calcrobots[j]
		nr, nc = (r + dr) % ROWS, (c + dc) % COLS
		grid[nr][nc] = 'X'
		calcrobots[j] = (nr, nc, dr, dc)
	seen = [[0 for _ in range(COLS)] for _ in range(ROWS)]
	steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	counts = []
	for j, k, _, _ in calcrobots:
		if not seen[j][k]:
			if grid[j][k] == '.':
				seen[j][k] = 1
				continue
			count = 0
			queue = [(j, k)]
			for r, c in queue:
				if not seen[r][c]:
					count += 1
					seen[r][c] = 1
					for dr, dc in steps:
						nr, nc = r + dr, c + dc
						if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and not seen[nr][nc]:
							if grid[nr][nc] == '.':
								seen[nr][nc] = 1
								continue
							queue.append((nr, nc))
			counts.append(count)
	maxadj.append((max(counts), i + 1))
maxadj.sort(reverse=True)
print(maxadj[0][1])

## VERIFICATION OF IMAGE
# for c, t in maxadj:
# 	if c > 50:
# 		print(t)
# 		grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
# 		for j in range(len(robots)):
# 			r, c, dr, dc = robots[j]
# 			nr, nc = (r + (dr * t)) % ROWS, (c + (dc * t)) % COLS
# 			grid[nr][nc] = 'X'
# 		for row in grid:
# 			for char in row:
# 				if char == '.':
# 					print(f'\33[30m{char}\33[0m', end="")
# 				else:
# 					print(f'\33[32m{char}\33[0m', end="")
# 			print()