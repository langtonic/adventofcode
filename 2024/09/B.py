diskmap = input().strip()

disk = []
empty = []
files = []
f = 0
for i in range(len(diskmap)):
	if i % 2 == 0:
		files.append((len(disk), int(diskmap[i]), f))
		disk.extend([f for _ in range(int(diskmap[i]))])
		f += 1
	else:
		empty.append((len(disk), int(diskmap[i])))
		disk.extend(['.' for _ in range(int(diskmap[i]))])

for file in reversed(files):
	for i in range(len(empty)):
		if file[1] <= empty[i][1] and file[0] > empty[i][0]:
			for j in range(file[1]):
				disk[empty[i][0] + j] = file[2]
				disk[file[0] + j] = '.'
			empty[i] = (empty[i][0] + file[1], empty[i][1] - file[1])
			break

total = 0
for i in range(len(disk)):
	if disk[i] != '.':
		total += (i * disk[i])
print(total)
