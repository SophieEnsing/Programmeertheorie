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

print(randomRoute("Leiden Centraal", 120))


















	