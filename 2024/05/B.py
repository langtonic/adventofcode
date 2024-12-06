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
		for j in range(i + 1, len(update)):
			if update[i] not in rules:
				continue
			if update[j] in rules[update[i]]:
				correct = False
	if not correct:
		adj = {x:[] for x in update}
		for i in update:
			if i not in rules:
				adj[i] = [x for x in update if x != i]
				continue
			for j in update:
				if i != j and j not in rules[i]:
					adj[i].append(j)
		lens = []
		for num, adjs in adj.items():
			if len(adjs) == len(update) // 2:
				total += int(num)

print(total)