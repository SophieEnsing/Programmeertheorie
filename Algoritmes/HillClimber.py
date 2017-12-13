import random
from Functies.ShortKritiek import *
from Functies.Score import *
from Functies.Staart import *
from Functies.Grafiek import *
from Algoritmes.Random import *

#
# HILLCLIMBER 1
#

def hillClimber(trajectTijd, aantalTrajecten, classname, kritiek):
	""" Maak een random combinate van trajecten als start state
	en verander elke keer 1 beginstation. Neem de verandering aan
	als het beter is en anders door naar een volgende optie. In het
	archief wordt bijgehouden of niet dezelfde combinaties geprobeerd
	worden. 
	"""
	beginStations = random.sample(classname.stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations, classname)
	currentScore = scoreLijnvoering(currentState, classname, kritiek)
	archief = [sorted(beginStations)]
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	c = 0
	aantal_iteraties = 0
	scores = []

	# Stop als er 1000 keer achter elkaar geen betere oplossing is gevonden
	while c < 1000:
		aantal_iteraties += 1
		scores.append(currentScore)

		index = random.randint(0, (aantalTrajecten - 1)) 
		station = random.choice(classname.stations)

		while station in beginStations:
			station = random.choice(classname.stations)

		# Pas een van de stations aan van de beginstations
		nieuweStations = beginStations
		nieuweStations[index] = station
		nieuweStations = sorted(nieuweStations)

		# Check of de combinatie van stations niet in het archief staat
		if nieuweStations not in archief:
			archief.append(nieuweStations)
			newState = lijnvoering(trajectTijd, nieuweStations, classname)
			newScore = scoreLijnvoering(newState, classname, kritiek)

			# Check of de score beter is
			if newScore > currentScore:
				currentState = newState
				currentScore = newScore
				beginStations = nieuweStations
				c = 0

			else:
				c += 1

	return currentScore

#
# HILLCLIMBER 2
#

def hillClimber2(trajectTijd, aantalTrajecten, classname, kritiek):
	""" Maak een random begin status door middel van het random 
	algoritme. Vervolgens wordt er door middel van de hulpfunctie
	staart in een van de trajecten een aanpassing gemaakt. Van de 
	nieuwe staat wordt de score berekend. Neem de verandering aan
	als het beter is en anders door naar een volgende optie.
	"""

	# Maak een begin state en archief aan
	beginState = randomAlgoritme(1, classname, trajectTijd, aantalTrajecten, kritiek)
	currentState = beginState[0]
	currentScore = beginState[1]

	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	aantal_interaties = 0
	y_waardes = []
	c = 0

	# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
	while c < 10000:
		aantal_interaties += 1
		y_waardes.append(currentScore)
		newState = staart(currentState, classname, trajectTijd)
		newScore = scoreLijnvoering(newState, classname, kritiek)

		if newScore > currentScore:
			currentState = newState
			currentScore = newScore
			c = 0

		else:
			c += 1

	return currentState, currentScore

