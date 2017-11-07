import csv
import random

stations = []
stationsKritiek = []

with open('StationsHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])
        if row[3] == 'Kritiek':
        	stationsKritiek.append(row[0])

verbinding = {}
verbindingKritiek = []


with open('ConnectiesHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        verbinding[row[0]] = verbinding.get(row[0], []) + [(int(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(int(row[2]), row[0])]
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
        	verbindingKritiek.append((row[0], row[1]))

tijd = 0
route = []

def shortroute(station):
	global tijd
	global route
	i = 0

	if tijd < 120:
		route.append(station)		
		kort = sorted(verbinding[station])[i]

		while kort[1] in route:
			if i == (len(verbinding[station]) - 1):
				break
			kort = sorted(verbinding[station])[i + 1]
			i += 1
		
		if kort[1] not in route:
			verbinding[station].remove(kort)
			station = kort[1]
			tijd += int(kort[0])
			shortroute(station)

	return route, tijd

print shortroute('Alkmaar')


