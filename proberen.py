from __future__ import division
import csv
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Inlezen van alle data
stations = []
stationsKritiek = []

import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()
stationsKritiek = []


with open('data/StationsHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        G.add_node(row[0], pos=(float(row[1]), float(row[2])))
        if row[3] == 'Kritiek':
            stationsKritiek.append(row[0])

pos = {city:(long, lat) for city, (lat,long) in nx.get_node_attributes(G, 'pos').items()}

with open('data/ConnectiesHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
            G.add_edge(row[0], row[1], color='r', weight = int(row[2]))
        else:
            G.add_edge(row[0], row[1], color='b', weight = int(row[2]))

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
nx.draw(G, pos, with_labels = True, node_size = 50, edge_color=colors, font_size = 5)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size = 5)
#plt.show()
print (labels)

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
result = [scoreLijnvoering(testLijnvoering(100, 7)) for i in range(10000)]
print("mean:", np.mean(result), "max:", max(result)) 
