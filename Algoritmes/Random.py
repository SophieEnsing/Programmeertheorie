# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

import random
from Functies.Score import *

def randomRoute(station, trajectTijd, classname, tijd, route):
	""" Deze functie kiest vanaf een station een random volgend
	station. Als er geen opties meer over zijn of als de maximale
	tijd bereikt is, worden de route en tijd gereturned.
	"""
	route.append(station)
	
	# Aantal mogelijke verbindingen vanaf het station. Het is niet 
	# mogelijk om naar een station te gaan dat al eerder bezocht is.
	verbindingen = [ (afstand, eindstation) for afstand, eindstation 
		in classname.verbinding[station] if eindstation not in route ]
	
	# Check of er nog verbindingen zijn en kies er willekeurig een.
	if len(verbindingen) >= 1:
		gekozenVerbinding = random.choice(verbindingen)

	else:
		return route, tijd
	
	# Check of de maximale tijd niet overschreden wordt.
	if tijd + int(gekozenVerbinding[0]) <= trajectTijd:
		station = gekozenVerbinding[1]
		tijd += int(gekozenVerbinding[0])
		route, tijd = randomRoute(station, trajectTijd, classname, tijd, route)
	
	return route, tijd

def randomAlgoritme(iteraties, classname, maxMinutes, maxTrajecten, kritiek):
	""" Dit algoritme maakt met behulp van randomRoute een lijnvoering. 
	De functie randomRoute wordt aangeroepen met random gekozen beginstations. 
	Er worden zoveel random stations gekozen als bij maxTrajecten aangegeven wordt.
	Dit gebeurt zo vaak als het aantal iteraties, de best gevonden lijnvoering
	wordt gereturned.
	"""
	lijnvoeringen = []

	for i in range(iteraties):
		# Kies random beginstations.
		randomStations = random.sample(classname.stations, maxTrajecten)
		lijnvoering = []

		# Maak vanuit elk beginstation een random traject.
		for station in randomStations:
			tijd = 0
			route = []
			lijnvoering.append(randomRoute(station, maxMinutes, classname, tijd, route))

		score = scoreLijnvoering(lijnvoering, classname, kritiek)
		lijnvoeringen.append((lijnvoering, score))

	lijnvoeringen.sort(key=lambda tup: tup[1])
	
	# Return de beste lijnvoering.
	return lijnvoeringen[-1]
