import sys

sum = 0

for line in sys.stdin:
	digit1 = 0
	digit2 = 0
	length = len(line)
	for i in range (0, length, 1):
		if line[i].isdigit():
			digit1 = line[i]
			break
		if line[i] == 'o':
			if line[i+1] == 'n':
				if line[i+2] == 'e':
					digit1 = '1'
					break
		if line[i] == 't':
			if line[i+1] == 'w':
				if line[i+2] == 'o':
					digit1 = '2'
					break
			if line[i+1] == 'h':
				if line[i+2] == 'r':
					if line[i+3] == 'e':
						if line[i+4] == 'e':
							digit1 = '3'
							break
		if line[i] == 'f':
			if line[i+1] == 'o':
				if line[i+2] == 'u':
					if line[i+3] == 'r':
						digit1 = '4'
						break
			if line[i+1] == 'i':
				if line[i+2] == 'v':
					if line[i+3] == 'e':
						digit1 = '5'
						break
		if line[i] == 's':
			if line[i+1] == 'i':
				if line[i+2] == 'x':
					digit1 = '6'
					break
			if line[i+1] == 'e':
				if line[i+2] == 'v':
					if line[i+3] == 'e':
						if line[i+4] == 'n':
							digit1 = '7'
							break
		if line[i] == 'e':
			if line[i+1] == 'i':
				if line[i+2] == 'g':
					if line[i+3] == 'h':
						if line[i+4] == 't':
							digit1 = '8'
							break
		if line[i] == 'n':
			if line[i+1] == 'i':
				if line[i+2] == 'n':
					if line[i+3] == 'e':
						digit1 = '9'
						break	
	for i in range (length-1, -1, -1):
		if line[i].isdigit():
			digit2 = line[i]
			break
		if line[i] == 'o':
			if (i+1 < length) and (line[i+1] == 'n'):
				if (i+2 < length) and (line[i+2] == 'e'):
					digit2 = '1'
					break
		if line[i] == 't':
			if (i+1 < length) and (line[i+1] == 'w'):
				if (i+2 < length) and (line[i+2] == 'o'):
					digit2 = '2'
					break
			if (i+1 < length) and (line[i+1] == 'h'):
				if (i+2 < length) and (line[i+2] == 'r'):
					if (i+3 < length) and (line[i+3] == 'e'):
						if (i+4 < length) and (line[i+4] == 'e'):
							digit2 = '3'
							break
		if line[i] == 'f':
			if (i+1 < length) and (line[i+1] == 'o'):
				if (i+2 < length) and (line[i+2] == 'u'):
					if (i+3 < length) and (line[i+3] == 'r'):
						digit2 = '4'
						break
			if (i+1 < length) and (line[i+1] == 'i'):
				if (i+2 < length) and (line[i+2] == 'v'):
					if (i+3 < length) and (line[i+3] == 'e'):
						digit2 = '5'
						break
		if line[i] == 's':
			if (i+1 < length) and (line[i+1] == 'i'):
				if (i+2 < length) and (line[i+2] == 'x'):
					digit2 = '6'
					break
			if (i+1 < length) and (line[i+1] == 'e'):
				if (i+2 < length) and (line[i+2] == 'v'):
					if (i+3 < length) and (line[i+3] == 'e'):
						if (i+4 < length) and (line[i+4] == 'n'):
							digit2 = '7'
							break
		if line[i] == 'e':
			if (i+1 < length) and (line[i+1] == 'i'):
				if (i+2 < length) and (line[i+2] == 'g'):
					if (i+3 < length) and (line[i+3] == 'h'):
						if (i+4 < length) and (line[i+4] == 't'):
							digit2 = '8'
							break
		if line[i] == 'n':
			if (i+1 < length) and (line[i+1] == 'i'):
				if (i+2 < length) and (line[i+2] == 'n'):
					if (i+3 < length) and (line[i+3] == 'e'):
						digit2 = '9'
						break
	value = int(digit1+digit2)
	sum = sum + value
			
print(sum)