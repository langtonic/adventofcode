import sys

# Inverted brute force solution designed to be faster by going from the end
# point of location values and working up from the lowest
# Has a hole in that it will not check any location values not represented by one
# of the ranges (luckily this doesn't actually affect this problem input)

def valueMatch(value, mapList):
	mapped = False
	for map in mapList:
		if value >= map[0] and value <= (map[0] + map[2] - 1):
			mappedVal = map[1] + (value - map[0])
			mapped = True
			break
	if not mapped:
		mappedVal = value
	return mappedVal

seedRanges = []
seedToSoil = []
soilToFert = []
fertToWater = []
waterToLight = []
lightToTemp = []
tempToHumid = []
humidToLoc = []
activeList = None

for line in sys.stdin:
	if line[:6] == 'seeds:':
		seeds = [int(value) for value in line[6:].strip().split(' ')]
	if line.isspace():
		continue
	if line[:5] == 'seed-':
		activeList = seedToSoil
	if line[:5] == 'soil-':
		activeList = soilToFert
	if line[:5] == 'ferti':
		activeList = fertToWater
	if line[:5] == 'water':
		activeList = waterToLight
	if line[:5] == 'light':
		activeList = lightToTemp
	if line[:5] == 'tempe':
		activeList = tempToHumid
	if line[:5] == 'humid':
		activeList = humidToLoc
	if line[0].isdigit():
		activeList.append([int(value) for value in line.strip().split(' ')])

for i in range(0, len(seeds), 2):
	seedRanges.append((seeds[i], seeds[i + 1]))

humidToLoc.sort()
notFound = True


for mapping in humidToLoc:
	for i in range(0, mapping[3], 1):
		if notFound:
			location = mapping[0] + i
			humidNum = valueMatch(location, humidToLoc)
			tempNum = valueMatch(humidNum, tempToHumid)
			lightNum = valueMatch(tempNum, lightToTemp)
			waterNum = valueMatch(lightNum, waterToLight)
			fertNum = valueMatch(waterNum, fertToWater)
			soilNum = valueMatch(fertNum, soilToFert)
			seedNum = valueMatch(soilNum, seedToSoil)
			for seed in seedRanges:
				if seedNum >= seed[0] and seedNum <= (seed[0] + seed[1] - 1):
					print(location)
					notFound = False
					break
