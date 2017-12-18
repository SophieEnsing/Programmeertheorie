# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

import random
from Algoritmes.Random import *

def shortKritiek(station, trajectTijd, classname, tijd, route):
	""" Maak een traject vanuit een beginstation, vanuit dit
	station wordt het korste kritieke pad gekozen
	Trajecttijd: maximale tijd in minuten voor het traject
	Station: beginstation van het traject """
	route.append(station)	

	# Maak lijsten van normale verbindingen en kritieke verbindingen.
	verbindingen = [ (afstand, eindstation) for afstand, eindstation in classname.verbinding[station] 
						if eindstation not in route ]
	kritiekeVerbindingen = [ (afstand, eindstation) for afstand, eindstation in 
							verbindingen if eindstation in classname.stationsKritiek or station in classname.stationsKritiek ]

	# Kies eerst de kortste kritieke verbinding en anders de kortste verbinding.
	if len(kritiekeVerbindingen) >= 1:
		kort = sorted(kritiekeVerbindingen)[0]

	elif len(verbindingen) >= 1:
		kort = sorted(verbindingen)[0]

	else:
		return route, tijd
	
	# Controleer of de maximale trajectijd niet wordt overschreden.
	if tijd + int(kort[0]) < trajectTijd:
		station = kort[1]
		tijd += int(kort[0])
		route, tijd = shortKritiek(station, trajectTijd, classname, tijd, route)

	return route, tijd

def lijnvoering(trajectTijd, beginStations, classname):
	"""" Maakt een lijnvoering van verschillende trajecten
	Trajecttijd: maximale tijd in minuten per traject
	Aantaltrajecten: aantal trajecten in de lijnvoering"""
	trajecten = []

	# Maak voor elk beginstation een traject en voeg dat dan samen tot een lijnvoering.
	for station in beginStations:
		tijd = 0
		route = []
		trajecten.append(shortKritiek(station, trajectTijd, classname, tijd, route))

	return trajecten
