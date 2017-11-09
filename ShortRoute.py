from __future__ import division
import csv
import random
import numpy as np

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


def testLijnvoering(trajectTijd, aantalTrajecten):
	beginStations = random.sample(stations, aantalTrajecten)
	trajecten = []
	global tijd
	global route

	for stat in beginStations:
		traject = {}
		tijd = 0
		route = []
		traject[stat] = shortroute(stat, trajectTijd)
		trajecten.append(traject)

	return trajecten

def scoreLijnvoering(lijnvoering):
	verbindingen = []
	aantalTrajecten = len(lijnvoering)
	aantalMinuten = 0

	for traject in lijnvoering:
		aantalMinuten += traject.values()[0][1]
		traject = traject.values()[0][0]

		trajectParen = [(traject[i], traject[i+1]) for i in range(0, len(traject)-1 ,1)]
		trajectParen2 = [traject for traject in trajectParen if traject[0] in stationsKritiek or traject[1] in stationsKritiek]
		verbindingen += trajectParen2

	setTrajectParen = list(set([ tuple(sorted(t)) for t in verbindingen]))
	percKritiek = len(setTrajectParen) / len(verbindingKritiek)

	S = (percKritiek * 10000) - ((aantalTrajecten * 20) + (aantalMinuten / 100000))

	# Score functie S:
	# S = p*10000 - (t*20 + min/100000)

	return S


result = [scoreLijnvoering(testLijnvoering(100, 7)) for i in range(10000)]
print "mean:", np.mean(result), "max:", max(result)



