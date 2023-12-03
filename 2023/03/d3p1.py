import sys

sum = 0
grid = []
partNumbers = []
rowCursor = -1
partNumber = False

for line in sys.stdin:
	grid.append(line.strip())
numRows = len(grid)
numCols = len(grid[0])

def symbolSearch(startIndex, endIndex):
	partNumber = False
	if startIndex > 0:
		searchStart = startIndex - 1
		if not grid[rowCursor][searchStart].isdigit() and not grid[rowCursor][searchStart] == '.':
			partNumber = True
	else:
		searchStart = startIndex
	if endIndex < numCols - 1:
		searchEnd = endIndex + 1
		if not grid[rowCursor][searchEnd].isdigit() and not grid[rowCursor][searchEnd] == '.':
			partNumber = True
	else:
		searchEnd = endIndex
	if rowCursor > 0:
		for i in range(searchStart, searchEnd + 1, 1):
			if not grid[rowCursor - 1][i].isdigit() and not grid[rowCursor - 1][i] == '.':
				partNumber = True
				break
	if rowCursor < numRows - 1:
		for i in range(searchStart, searchEnd + 1, 1):
			if not grid[rowCursor + 1][i].isdigit() and not grid[rowCursor + 1][i] == '.':
				partNumber = True
				break
	return partNumber

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
					if symbolSearch(startIndex, endIndex):
						partNumbers.append(int(readingNumber))
			else:
				readingNumber += char
				if lineCursor == numCols - 1:
					endIndex = lineCursor
					if symbolSearch(startIndex, endIndex):
						partNumbers.append(int(readingNumber))
		else:
			if readingNumber == None:
				continue
			else:
				endIndex = lineCursor - 1
				if symbolSearch(startIndex, endIndex):
					partNumbers.append(int(readingNumber))
				readingNumber = None

for part in partNumbers:
	sum += part
print(sum)
