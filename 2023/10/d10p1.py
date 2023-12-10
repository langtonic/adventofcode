import sys

grid = []
startLoc = None
startFound = False
prevA = None
prevB = None
steps = 0

for line in sys.stdin:
	grid.append(line.strip())
width = len(grid[0])
height = len(grid)

while not startFound:
	for row in range(height):
		if startFound:
			break
		for column in range(width):
			if grid[row][column] == 'S':
				startLoc = (row, column)
				startFound = True
				break

def nextPipe(coords, prev):
	row = coords[0]
	col = coords[1]
	currentPipe = grid[row][col]
	match currentPipe:
		case '-':
			if col < width - 1:
				match grid[row][col + 1]:
					case 'J'|'-'|'7':
						if not (row, col + 1) == prev:
							return (row, col + 1), (row, col)
			if col > 0:
				match grid[row][col - 1]:
					case 'F'|'-'|'L':
						if not (row, col - 1) == prev:
							return (row, col - 1), (row, col)
		case '|':
			if row > 0:
				match grid[row - 1][col]: 
					case '7'|'|'|'F':
						if not (row - 1, col) == prev:
							return (row - 1, col), (row, col)
			if row < height - 1:
				match grid[row + 1][col]:
					case 'L'|'|'|'J':
						if not (row + 1, col) == prev:
							return (row + 1, col), (row, col)				
		case '7':
			if row < height - 1:
				match grid[row + 1][col]:
					case 'L'|'|'|'J':
						if not (row + 1, col) == prev:
							return (row + 1, col), (row, col)
			if col > 0:
				match grid[row][col - 1]:
					case 'F'|'-'|'L':
						if not (row, col - 1) == prev:
							return (row, col - 1), (row, col)
		case 'F':	
			if col < width - 1:
				match grid[row][col + 1]:
					case 'J'|'-'|'7':
						if not (row, col + 1) == prev:
							return (row, col + 1), (row, col)
			if row < height - 1:
				match grid[row + 1][col]:
					case 'L'|'|'|'J':
						if not (row + 1, col) == prev:
							return (row + 1, col), (row, col)
		case 'L':
			if row > 0:
				match grid[row - 1][col]: 
					case '7'|'|'|'F':
						if not (row - 1, col) == prev:
							return (row - 1, col), (row, col)
			if col < width - 1:
				match grid[row][col + 1]:
					case 'J'|'-'|'7':
						if not (row, col + 1) == prev:
							return (row, col + 1), (row, col)
		case 'J':
			if row > 0:
				match grid[row - 1][col]: 
					case '7'|'|'|'F':
						if not (row - 1, col) == prev:
							return (row - 1, col), (row, col)
			if col > 0:
				match grid[row][col - 1]:
					case 'F'|'-'|'L':
						if not (row, col - 1) == prev:
							return (row, col - 1), (row, col)

def firstPipe(start):
	firstFound = False
	pathA = None
	pathB = None
	row = start[0]
	col = start[1]
	if row > 0:
		match grid[row - 1][col]: 
			case '7'|'|'|'F':
					pathA = (row - 1, col)
					firstFound = True
	if col < width - 1:
		match grid[row][col + 1]:
			case 'J'|'-'|'7':
				if not firstFound:
					pathA = (row, col + 1)
					firstFound = True
				else:
					pathB = (row, col + 1)
	if row < height - 1:
		match grid[row + 1][col]:
			case 'L'|'|'|'J':
				if not firstFound:
					pathA = (row + 1, col)
					firstFound = True
				else:
					pathB = (row + 1, col)
	if col > 0:
		match grid[row][col - 1]:
			case 'F'|'-'|'L':
				pathB = (row, col - 1)
	return pathA, pathB

pathA, pathB = firstPipe(startLoc)
steps += 1
prevA = prevB = startLoc
while not pathA == pathB:
	pathA, prevA = nextPipe(pathA, prevA)
	pathB, prevB = nextPipe(pathB, prevB)
	steps += 1
print(steps)