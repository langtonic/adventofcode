diskmap = input().strip()

disk = []
f = 0
for i in range(len(diskmap)):
	if i % 2 == 0:
		disk.extend([f for _ in range(int(diskmap[i]))])
		f += 1
	else:
		disk.extend(['.' for _ in range(int(diskmap[i]))])

i = 0
total = 0
while i < len(disk):
	if disk[i] == '.':
		while(True):
			if i >= len(disk):
				break
			end = disk.pop()
			if end != '.':
				disk[i] = end
				break
	if i >= len(disk):
		break
	total += (i * disk[i])
	i += 1

print(total)