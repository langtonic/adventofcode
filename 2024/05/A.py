import sys

rules = {}
updates = []
total = 0

for line in sys.stdin:
	if '|' in line:
		a, b = line.strip().split('|')
		if b in rules:
			rules[b].add(a)
		else:
			rules[b] = {a}
	elif ',' in line:
		updates.append(line.strip().split(','))

for update in updates:
	correct = True
	for i in range(len(update) - 2, -1, -1):
		if update[i] not in rules:
			continue
		for j in range(i + 1, len(update)):
			if update[j] in rules[update[i]]:
				correct = False
	if correct:
		total += int(update[len(update) // 2])

print(total)