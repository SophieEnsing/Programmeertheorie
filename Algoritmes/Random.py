import random
from Functies.Score import *

tijd = 0
route = []

def randomRoute(station, trajectTijd, classname):
	global tijd
	global route

	route.append(station)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation 
						in classname.verbinding[station] if eindstation not in route ]

	if len(verbindingen) >= 1:
		gekozenVerbinding = random.choice(verbindingen)

	else:
		return route, tijd

	if tijd + int(gekozenVerbinding[0]) < trajectTijd:
		station = gekozenVerbinding[1]
		tijd += int(gekozenVerbinding[0])
		randomRoute(station, trajectTijd, classname)

	return route, tijd

def randomAlgoritme(iteraties, classname, maxMinutes, maxTrajecten, kritiek):
	global tijd
	global route

	lijnvoeringen = []

	for i in range(iteraties):
		trajectAantal = random.randint(1, (maxTrajecten - 2))
		randomStations = random.sample(classname.stations, trajectAantal)
		
		while 'Dordrecht' in randomStations or 'Den Helder' in randomStations:
			randomStations = random.sample(classname.stations, trajectAantal)

		beginstations = ['Dordrecht', 'Den Helder'] + randomStations

		lijnvoering = []

		for station in beginstations:
			tijd = 0
			route = []
			lijnvoering.append(randomRoute(station, maxMinutes, classname))

		score = scoreLijnvoering(lijnvoering, classname, kritiek)
		lijnvoeringen.append((lijnvoering, score))

	lijnvoeringen.sort(key=lambda tup: tup[1])
	
	return lijnvoeringen[-1]