import sys

sum = 0

for line in sys.stdin:
	digit1 = 0
	digit2 = 0
	for i in range (0, len(line), 1):
		if line[i].isdigit():
			digit1 = line[i]
			break
	for i in range (len(line)-1, -1, -1):
		if line[i].isdigit():
			digit2 = line[i]
			break
	value = int(digit1+digit2)
	sum = sum + value
			
print(sum)   
	