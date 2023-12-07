import sys

cardPower = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hands = []
totalBet = 0

def handStrength(hand):
	cardCount = []
	for i in range(5):
		cardCount.append(hand[0].count(hand[0][i]))
	cardCount.sort()
	match cardCount[4]:
		case 5:
			hand.append(6)
		case 4:
			hand.append(5)
		case 3:
			if cardCount[1] == 1:
				hand.append(4)
			else:
				hand.append(3)
		case 2:
			if cardCount[1] == 2:
				hand.append(2)
			else:
				hand.append(1)
		case 1:
			hand.append(0)

def handSort(parent):
	if len(parent) > 1:
		middle = len(parent) // 2
		leftHalf = parent[:middle]
		rightHalf = parent[middle:]
		handSort(leftHalf)
		handSort(rightHalf)
		i = j = k = 0
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i][2] == rightHalf[j][2]:
				for l in range(5):
					if cardPower.index(leftHalf[i][0][l]) < cardPower.index(rightHalf[j][0][l]):
						parent[k] = rightHalf[j]
						j += 1
						break
					if cardPower.index(leftHalf[i][0][l]) > cardPower.index(rightHalf[j][0][l]):
						parent[k] = leftHalf[i]
						i += 1
						break
				k += 1
			else: 
				if leftHalf[i][2] < rightHalf[j][2]:
					parent[k] = leftHalf[i]
					i += 1
				else:
					parent[k] = rightHalf[j]
					j += 1
				k += 1
		for m in range(k, len(parent), 1):
			if i < len(leftHalf):
				parent[k] = leftHalf[i]
				i += 1
				k += 1
			else:
				parent[k] = rightHalf[j]
				j += 1
				k += 1
	return



for line in sys.stdin:
	hand = line.strip().split(' ')
	hand[1] = int(hand[1])
	handStrength(hand)
	hands.append(hand)

hands.sort(key = lambda x: x[2])
handSort(hands)

for i in range(len(hands)):
	totalBet += ((i + 1) * hands[i][1])
	print(hands[i][0], hands[i][2], i, hands[i][1], totalBet)
print(totalBet)