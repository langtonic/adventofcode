import sys

cardList = []
queue = []

def trimList(list):
	for i in range(len(list) - 1, -1, -1):
		if list[i] == '':
			list.pop(i)

for scratch in sys.stdin:
	card = scratch.replace(':', '|').strip().split('|')
	card[0] = int(card[0][5:])
	card[1] = card[1].split(' ')
	card[2] = card[2].split(' ')
	trimList(card[1])
	trimList(card[2])
	cardList.append(card)
	queue.append((card[0], 1))

cardTotal = queue[-1][0]

for card in queue:
	matches = 0
	currentCard = cardList[card[0] - 1]
	for number in currentCard[2]:
		for winner in currentCard[1]:
			if number == winner:
				matches += 1
	for i in range(card[0], card[0] + matches, 1):
		queue[i] = (queue[i][0], ((card[1]) + queue[i][1]))
	cardTotal += (matches * card[1])

print(cardTotal)