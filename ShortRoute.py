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
		kort = sorted(verbinding[station])[i]

		try:
			# Ga niet terug naar het voorgaande station
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

def scoreLijnvoering(lijnvoering):
	""" Bereken de score van de lijnvoering
	Score functie S > S = p*10000 - (t*20 + min/100000)
	"""
	verbindingen = []
	aantalTrajecten = len(lijnvoering)
	aantalMinuten = 0

	for traject in lijnvoering:
		# Bijhouden van totale tijd in minuten van de lijnvoering
		aantalMinuten += list(traject.values())[0][1]
		traject = list(traject.values())[0][0]

		# Maak van een traject een lijst van verbindingen in dat traject
		trajectParen = [(traject[i], traject[i+1]) for i in range(0, len(traject)-1 ,1)]
		# Check voor elke verbinding of een van de stations kritiek is
		trajectParen2 = [traject for traject in trajectParen if traject[0] in stationsKritiek or traject[1] in stationsKritiek]
		# Voeg de kritieke verbindingen toe aan een lijst
		verbindingen += trajectParen2

	# Set van verbindingen om dubbele tuples te voorkomen
	setTrajectParen = list(set([ tuple(sorted(t)) for t in verbindingen]))
	percKritiek = len(setTrajectParen) / len(verbindingKritiek)

	S = (percKritiek * 10000) - ((aantalTrajecten * 20) + (aantalMinuten / 100000))
	return S

# Gemiddelde en hoogste score bij 10,000 keer uitvoeren van de functie
result = [scoreLijnvoering(testLijnvoering(100, 7)) for i in range(10000000)]
print("mean:", np.mean(result), "max:", max(result)) 
