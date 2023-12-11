import sys

grid = []
galCoords = []

for line in sys.stdin:
	line = line.strip()
	if '#' in line:
		grid.append(line)
	else:
		grid.append(line)
		grid.append(line)

for i in range(len(grid[0]) - 1, -1, -1):
	galInCol = False
	for row in grid:
		if row[i] == '#':
			galInCol = True
			break
	if not galInCol:
		for row in grid:
			grid[grid.index(row)] = row[:i] + '.' + row[i:]

for row in range(len(grid)):
	for col in range(len(grid[0])):
		if grid[row][col] == '#':
			galCoords.append((row, col))

steps = 0
for i in range(len(galCoords)):
	for j in range(i + 1, len(galCoords)):
		steps += abs(galCoords[j][1] - galCoords[i][1]) + abs(galCoords[j][0] - galCoords[i][0])
print(steps)