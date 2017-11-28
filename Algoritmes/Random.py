from __future__ import division
import random
import numpy as np
import csv


""" Alle code tot de hillclimber functie zelf is dubbelop met andere bestanden. Het is
de bedoeling dat deze code later geimporteerd wordt vanuit de andere bestanden.
"""

# Inlezen van alle data
stations = []
stationsKritiek = []

with open('../Data/StationsHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])
        if row[3] == 'Kritiek':
        	# Voeg alle kritieke stations toe aan een lijst
        	stationsKritiek.append(row[0])

verbinding = {}
verbindingKritiek = []
 
with open('../Data/ConnectiesHolland.csv', 'r') as csvfile:
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

def scoreLijnvoering(lijnvoering):
	""" Bereken de score van de lijnvoering
	Score functie S > S = p*10000 - (t*20 + min/100000)
	"""
	verbindingen = []
	aantalTrajecten = len(lijnvoering)
	aantalMinuten = 0

	for traject in lijnvoering:
		# Bijhouden van totale tijd in minuten van de lijnvoering
		aantalMinuten += traject[1]
		traject = traject[0]

		# Maak van een traject een lijst van verbindingen in dat traject
		trajectParen = [(traject[i], traject[i+1]) for i in range(0, len(traject)-1 ,1)]
		# Check voor elke verbinding of een van de stations kritiek is
		trajectParen2 = [traject for traject in trajectParen if traject[0] in stationsKritiek or traject[1] in stationsKritiek]
		# Voeg de kritieke verbindingen toe aan een lijst
		verbindingen += trajectParen2

	# Set van verbindingen om dubbele tuples te voorkomen
	setTrajectParen = list(set([ tuple(sorted(t)) for t in verbindingen]))
	percKritiek = len(setTrajectParen) / len(verbindingKritiek)

	S = (percKritiek * 1000) - ((aantalTrajecten * 20) + (aantalMinuten / 10))
	return S

def randomRoute(station, trajectTijd):
	global tijd
	global route

	route.append(station)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation in verbinding[station] if eindstation not in route ]

	if len(verbindingen) >= 1:
		gekozenVerbinding = random.choice(verbindingen)
	else:
		return route, tijd

	if tijd + int(gekozenVerbinding[0]) < trajectTijd:
		station = gekozenVerbinding[1]
		tijd += int(gekozenVerbinding[0])
		randomRoute(station, trajectTijd)

	return route, tijd

def RandomAlgo(x):
	global tijd
	global route

	lijnvoeringen = []

	for run in range(x):
		trajectAantal = random.randint(1,7)
		beginstations = random.sample(stations, trajectAantal)

		lijnvoering = []

		for station in beginstations:
			tijd = 0
			route = []
			lijnvoering.append(randomRoute(station, 120))

		score = scoreLijnvoering(lijnvoering)

		lijnvoeringen.append((lijnvoering, score))

	lijnvoeringen.sort(key=lambda tup: tup[1])
	print(lijnvoeringen[-1])

RandomAlgo(500000)


