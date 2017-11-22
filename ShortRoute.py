from __future__ import division
import csv
import random
import numpy as np

# Inlezen van alle data
stations = []
stationsKritiek = []

with open('data/StationsHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])
        if row[3] == 'Kritiek':
        	# Voeg alle kritieke stations toe aan een lijst
        	stationsKritiek.append(row[0])

verbinding = {}
verbindingKritiek = []

with open('data/ConnectiesHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	# Alle verbindingen toevoegen per station in een dictionary
        verbinding[row[0]] = verbinding.get(row[0], []) + [(int(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(int(row[2]), row[0])]

        # Maak een lijst van alle kritieke verbindingen
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
        	verbindingKritiek.append((row[0], row[1]))

tijd = 0
route = []

# Algoritme 1: Greedy algorithm
def shortroute(station, trajectTijd):
	""" Maak een traject vanuit een beginstation, vanuit dit
	station wordt het dichtsbijzijnde station gekozen
	Trajecttijd: maximale tijd in minuten voor het traject
	Station: beginstation van het traject """
	global tijd
	global route
	i = 0

	if tijd < trajectTijd:
		route.append(station)	

		verbindingen = [ (tijd, eindstation) for tijd, eindstation in verbinding[station] if eindstation not in route ]
		kritiekeVerbindingen = [ (tijd, eindstation) for tijd, eindstation in verbindingen if eindstation in stationsKritiek ]

		if len(kritiekeVerbindingen) >= 1:
			kort = sorted(kritiekeVerbindingen)[i]
		elif len(verbindingen) >= 1:
			kort = sorted(verbindingen)[i]
		else:
			return route, tijd

		'''try:
			# Ga niet terug naar het voorgaande station
			while kort[1] == route[-2]:
				if i == (len(verbinding[station]) - 1):
					break
				kort = sorted(verbinding[station])[i + 1]
				i += 1
		except:
			pass'''
		
		station = kort[1]
		tijd += int(kort[0])

		shortroute(station, trajectTijd)

	return route, tijd

def testLijnvoering(trajectTijd, aantalTrajecten):
	"""" Maakt een lijnvoering van verschillende trajecten
	Trajecttijd: maximale tijd in minuten per traject
	Aantaltrajecten: aantal trajecten in de lijnvoering"""

	# Genereer random beginstations
	beginStations = random.sample(stations, aantalTrajecten)
	trajecten = []
	global tijd
	global route

	# Maak voor elk beginstation een traject
	for stat in beginStations:
		traject = {}
		tijd = 0
		route = []
		traject[stat] = shortroute(stat, trajectTijd)
		trajecten.append(traject)

	return trajecten