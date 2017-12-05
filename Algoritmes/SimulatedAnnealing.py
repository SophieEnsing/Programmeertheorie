from __future__ import division
import random
import numpy as np
import csv
import math
import bigfloat 
import matplotlib.pyplot as plt 

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
        verbinding[row[0]] = verbinding.get(row[0], []) + [(float(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(float(row[2]), row[0])]

        # Maak een lijst van alle kritieke verbindingen
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
        	verbindingKritiek.append((row[0], row[1]))

tijd = 0
route = []

def shortKritiek(station, trajectTijd):
	""" Maak een traject vanuit een beginstation, vanuit dit
	station wordt het korste kritieke pad gekozen
	Trajecttijd: maximale tijd in minuten voor het traject
	Station: beginstation van het traject """
	global tijd
	global route
	
	route.append(station)	

	# Maak lijsten van normale verbindingen en kritieke verbindingen
	verbindingen = [ (afstand, eindstation) for afstand, eindstation in verbinding[station] 
						if eindstation not in route ]
	kritiekeVerbindingen = [ (afstand, eindstation) for afstand, eindstation in 
							verbindingen if eindstation in stationsKritiek or station in stationsKritiek ]

	# Kies eerst de kortste kritieke verbinding en anders de kortste verbinding
	if len(kritiekeVerbindingen) >= 1:
		kort = sorted(kritiekeVerbindingen)[0]

	elif len(verbindingen) >= 1:
		kort = sorted(verbindingen)[0]

	else:
		return route, tijd

	if tijd + int(kort[0]) < trajectTijd:
		station = kort[1]
		tijd += int(kort[0])
		shortKritiek(station, trajectTijd)

	return route, tijd

#print(shortKritiek("Leiden Centraal", 50))

def lijnvoering(trajectTijd, beginStations):
	"""" Maakt een lijnvoering van verschillende trajecten
	Trajecttijd: maximale tijd in minuten per traject"""

	# Genereer random beginstations
	trajecten = []
	global tijd
	global route

	# Maak voor elk beginstation een traject
	for stat in beginStations:
		traject = {}
		tijd = 0
		route = []
		traject[stat] = shortKritiek(stat, trajectTijd)
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

def grafiek(y_waardes, aantal_interaties):
	plt.plot(range(0,aantal_interaties), y_waardes)
	plt.axis([0, aantal_interaties, 0, 10000])
	plt.show()

def acceptance(old, new, T):
	a = bigfloat.exp(((old - new) / T),bigfloat.precision(100))
	return a


def SimulatedAnnealing(trajectTijd, aantalTrajecten):
	T = 1.0
	T_min = 0.00001
	alpha = 0.9

	beginStations = random.sample(stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations)
	currentScore = scoreLijnvoering(currentState)
	archief = [sorted(beginStations)]
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	c = 0
	aantal_interaties = 0
	y_waardes = []

	# Stop bij minimumtemperatuur
	while T > T_min:
		# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
		while c < 1000:
			aantal_interaties += 1
			y_waardes.append(currentScore)
			index = random.randint(0, (aantalTrajecten - 1)) 
			station = random.choice(stations)

			while station in beginStations:
				station = random.choice(stations)

			# Pas een van de stations aan van de beginstations
			nieuweStations = beginStations
			nieuweStations[index] = station
			nieuweStations = sorted(nieuweStations)

			# Check of de combinatie van stations niet in het archief staat
			if nieuweStations not in archief:
				archief.append(nieuweStations)
				newState = lijnvoering(trajectTijd, nieuweStations)
				newScore = scoreLijnvoering(newState)

				# Bereken acceptatiekans
				a = acceptance(currentScore, newScore, T)

				if a > random.random():
					currentState = newState
					currentScore = newScore
					beginStations = nieuweStations

			c += 1

		T = alpha * T

	#grafiek(y_waardes, aantal_interaties)

	return currentScore, beginStations

print(SimulatedAnnealing(180,10))