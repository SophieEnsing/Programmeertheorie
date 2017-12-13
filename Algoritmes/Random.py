import random
from Functies.Score import *

def randomRoute(station, trajectTijd, classname, tijd, route):
	route.append(station)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation 
						in classname.verbinding[station] if eindstation not in route ]

	if len(verbindingen) >= 1:
		gekozenVerbinding = random.choice(verbindingen)

	else:
		return route, tijd

	if tijd + int(gekozenVerbinding[0]) <= trajectTijd:
		station = gekozenVerbinding[1]
		tijd += int(gekozenVerbinding[0])
		route, tijd = randomRoute(station, trajectTijd, classname, tijd, route)
	
	return route, tijd

def randomAlgoritme(iteraties, classname, maxMinutes, maxTrajecten, kritiek):
	lijnvoeringen = []

	for i in range(iteraties):
		trajectAantal = random.randint(1, (maxTrajecten))
		randomStations = random.sample(classname.stations, trajectAantal)
		
		# while 'Dordrecht' in randomStations or 'Den Helder' in randomStations:
		# 	randomStations = random.sample(classname.stations, trajectAantal)

		# beginstations = ['Dordrecht', 'Den Helder'] + randomStations

		lijnvoering = []

		for station in randomStations:
			tijd = 0
			route = []
			lijnvoering.append(randomRoute(station, maxMinutes, classname, tijd, route))

		score = scoreLijnvoering(lijnvoering, classname, kritiek)
		lijnvoeringen.append((lijnvoering, score))

	lijnvoeringen.sort(key=lambda tup: tup[1])
	
	return lijnvoeringen[-1]