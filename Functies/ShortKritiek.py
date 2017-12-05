import random

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

def lijnvoering(trajectTijd, beginStations):
	"""" Maakt een lijnvoering van verschillende trajecten
	Trajecttijd: maximale tijd in minuten per traject
	Aantaltrajecten: aantal trajecten in de lijnvoering"""

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
