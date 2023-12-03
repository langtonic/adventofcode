import sys

sum = 0
grid = []
gearDict = {}
rowCursor = -1

for line in sys.stdin:
	grid.append(line.strip())
numRows = len(grid)
numCols = len(grid[0])


def gearCheck(row, column, readingNumber):
	if (row, column) in gearDict:
		gearDict[(row, column)].append(int(readingNumber))
	else:
		gearDict[(row, column)] = [int(readingNumber)]

def symbolSearch(startIndex, endIndex, readingNumber):
	if startIndex > 0:
		searchStart = startIndex - 1
		if grid[rowCursor][searchStart] == '*':
			gearCheck(rowCursor, searchStart, readingNumber)
	else:
		searchStart = startIndex
	if endIndex < numCols - 1:
		searchEnd = endIndex + 1
		if grid[rowCursor][searchEnd] == '*':
			gearCheck(rowCursor, searchEnd, readingNumber)
	else:
		searchEnd = endIndex
	if rowCursor > 0:
		for i in range(searchStart, searchEnd + 1, 1):
			if grid[rowCursor - 1][i] == '*':
				gearCheck(rowCursor - 1, i, readingNumber)
	if rowCursor < numRows - 1:
		for i in range(searchStart, searchEnd + 1, 1):
			if grid[rowCursor + 1][i] == '*':
				gearCheck(rowCursor	+ 1, i, readingNumber)
	return

for row in grid:
	readingNumber = None
	rowCursor += 1
	lineCursor = -1
	for char in row:
		lineCursor += 1
		if char.isdigit():
			if readingNumber == None:
				readingNumber = char
				startIndex = lineCursor
				if lineCursor == numCols - 1:
					endIndex = lineCursor
					symbolSearch(startIndex, endIndex, readingNumber)
			else:
				readingNumber += char
				if lineCursor == numCols - 1:
					endIndex = lineCursor
					symbolSearch(startIndex, endIndex, readingNumber)
		else:
			if readingNumber == None:
				continue
			else:
				endIndex = lineCursor - 1
				symbolSearch(startIndex, endIndex, readingNumber)
				readingNumber = None


for gear in gearDict:
	if len(gearDict[gear]) == 2:
		sum += (gearDict[gear][0] * gearDict[gear][1])
print(sum)