from Functies.ReadData import *
from Functies.Score import *
from Functies.ShortKritiek import *
import random

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

def randomAlgoritme(x):
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

	return lijnvoeringen[-1]