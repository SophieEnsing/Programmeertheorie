import csv
import random

stations = []
stationsKritiek = []

with open('data/StationsHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])
        if row[3] == 'Kritiek':
        	stationsKritiek.append(row[0])

verbinding = {}
verbindingKritiek = []

with open('data/ConnectiesHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        verbinding[row[0]] = verbinding.get(row[0], []) + [(int(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(int(row[2]), row[0])]
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
        	verbindingKritiek.append((row[0], row[1]))


tijd = 0
route = []


def shortroute(station, trajectTijd):
	global tijd
	global route
	i = 0

	if tijd < trajectTijd:
		route.append(station)		
		kort = sorted(verbinding[station])[i]

		try:
			while kort[1] == route[-2]:
				if i == (len(verbinding[station]) - 1):
					break
				kort = sorted(verbinding[station])[i + 1]
				i += 1
		except:
			pass
		
		station = kort[1]
		tijd += int(kort[0])
		shortroute(station, trajectTijd)

	return route, tijd


def lijnvoering(stationLijst, trajectTijd):
	trajecten = {}
	global tijd
	global route

	for stat in stationLijst:
		tijd = 0
		route = []
		trajecten[stat] = shortroute(stat, trajectTijd)

	return trajecten

def scoreLijnvoering(lijnen, aantalLijnen):
	beginStations = random.sample(lijnen, aantalLijnen)
	trajecten = []
	for station in beginStations:
		trajecten.append(lijnen[station])

	return trajecten

print scoreLijnvoering(lijnvoering(stations, 120), 7)









