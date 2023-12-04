import sys

pointTotal = 0

def trimList(list):
	for i in range(len(list) - 1, -1, -1):
		if list[i] == '':
			list.pop(i)

for scratch in sys.stdin:
	card = scratch.replace(':', '|').strip().split('|')
	card[1] = card[1].split(' ')
	card[2] = card[2].split(' ')
	matches = 0
	trimList(card[1])
	trimList(card[2])
	for number in card[2]:
		for winner in card[1]:
			if number == winner:
				matches += 1
	if matches == 0:
		continue
	else:
		points = 2 ** (matches - 1)
		pointTotal += points

print(pointTotal)