import random
from Functies.Score import *

tijd = 0
route = []

def randomRoute(station, trajectTijd, classname):
	global tijd
	global route

	route.append(station)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation in classname.verbinding[station] if eindstation not in route ]

	if len(verbindingen) >= 1:
		gekozenVerbinding = random.choice(verbindingen)
	else:
		return route, tijd

	if tijd + int(gekozenVerbinding[0]) < trajectTijd:
		station = gekozenVerbinding[1]
		tijd += int(gekozenVerbinding[0])
		randomRoute(station, trajectTijd, classname)

	return route, tijd

def randomAlgoritme(iteraties, classname):
	global tijd
	global route

	lijnvoeringen = []

	for i in range(iteraties):
		trajectAantal = random.randint(1,7)
		beginstations = random.sample(classname.stations, trajectAantal)

		lijnvoering = []

		for station in beginstations:
			tijd = 0
			route = []
			lijnvoering.append(randomRoute(station, 120, classname))

		score = scoreLijnvoering(lijnvoering, classname)

		lijnvoeringen.append((lijnvoering, score))

	lijnvoeringen.sort(key=lambda tup: tup[1])

	return lijnvoeringen[-1]

