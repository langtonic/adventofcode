import sys

grid = []
emptyRows = []
emptyCols = []
galCoords = []
rows = 0

for line in sys.stdin:
	line = line.strip()
	if '#' in line:
		grid.append(line)
	else:
		grid.append(line)
		emptyRows.append(rows)
	rows += 1


for i in range(len(grid[0])):
	galInCol = False
	for row in grid:
		if row[i] == '#':
			galInCol = True
			break
	if not galInCol:
		emptyCols.append(i)

for row in range(len(grid)):
	for col in range(len(grid[0])):
		if grid[row][col] == '#':
			galCoords.append((row, col))

steps = 0
for i in range(len(galCoords)):
	for j in range(i + 1, len(galCoords)):
		rowSteps = 0
		colSteps = 0
		xDiff = galCoords[j][1] - galCoords[i][1]
		yDiff = galCoords[j][0] - galCoords[i][0]
		if yDiff > 0:
			for row in range(galCoords[i][0] + 1, galCoords[j][0] + 1, 1):
				if row in emptyRows:
					rowSteps += 1000000
				else:
					rowSteps += 1
		if yDiff < 0:
			for row in range(galCoords[i][0] - 1, galCoords[j][0] - 1, -1):
				if row in emptyRows:
					rowSteps += 1000000
				else:
					rowSteps += 1
		if xDiff > 0:
			for col in range(galCoords[i][1] + 1, galCoords[j][1] + 1, 1):
				if col in emptyCols:
					colSteps += 1000000
				else:
					colSteps += 1
		if xDiff < 0:
			for col in range(galCoords[i][1] - 1, galCoords[j][1] - 1, -1):
				if col in emptyCols:
					colSteps += 1000000
				else:
					colSteps += 1
		steps += rowSteps + colSteps
print(steps)