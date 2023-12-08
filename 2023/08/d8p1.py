import sys

path = input()
nodes = {}
steps = 0
currentNode = 'AAA'
journeyEnd = False

input() #junk input to remove whitespace line without having to do if/else horseshit

for line in sys.stdin:
	info = line.strip().split('=')
	nodes[info[0].rstrip()] = (info[1][2:5], info[1][7:10])

print(currentNode)
while not journeyEnd:
	for step in path:
		match step:
			case 'L':
				currentNode = nodes[currentNode][0]
			case 'R':
				currentNode = nodes[currentNode][1]
		print(currentNode)
		steps += 1
		if currentNode == 'ZZZ':
			print(steps)
			journeyEnd = True
			break
