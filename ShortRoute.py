import csv
import random

stations = []

with open('StationsHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])

verbinding = {}

with open('ConnectiesHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        verbinding[row[0]] = verbinding.get(row[0], []) + [(int(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(int(row[2]), row[0])]

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
			kort = sorted(verbinding[station])[i + 1]
			break
		
		verbinding[station].remove(kort)
		station = kort[1]
		tijd += int(kort[0])
		shortroute(station)

	return route
print shortroute('Leiden Centraal')
