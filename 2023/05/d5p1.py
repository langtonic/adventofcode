import sys

def valueMatch(value, mapList):
	mapped = False
	for map in mapList:
		if value >= map[1] and value <= (map[1] + map[2] - 1):
			mappedVal = map[0] + (value - map[1])
			mapped = True
	if not mapped:
		mappedVal = value
	return mappedVal

seedToSoil = []
soilToFert = []
fertToWater = []
waterToLight = []
lightToTemp = []
tempToHumid = []
humidToLoc = []
locations = []
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

for seed in seeds:
	seedNum = seed
	soilNum = valueMatch(seedNum, seedToSoil)
	fertNum = valueMatch(soilNum, soilToFert)
	waterNum = valueMatch(fertNum, fertToWater)
	lightNum = valueMatch(waterNum, waterToLight)
	tempNum = valueMatch(lightNum, lightToTemp)
	humidNum = valueMatch(tempNum, tempToHumid)
	locNum = valueMatch(humidNum, humidToLoc)
	locations.append(locNum)

locations.sort()
print(locations[0])