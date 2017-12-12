import random
import matplotlib.pyplot as plt 
from Functies.ShortKritiek import *
from Functies.Score import *

def grafiek(y_waardes, aantal_interaties):
	plt.plot(range(0,aantal_interaties), y_waardes)
	plt.axis([0, aantal_interaties, 0, 10000])
	plt.show()

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

lijnvoering1 = [{'Alphen a/d Rijn': (['Alphen a/d Rijn', 'Gouda', 'Rotterdam Alexander', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Zaandam'], 110)}, {'Amsterdam Amstel': (['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Castricum', 'Alkmaar'], 87)}, {'Dordrecht': (['Dordrecht', 'Rotterdam Centraal', 'Schiedam Centrum', 'Delft', 'Den Haag Centraal', 'Leiden Centraal', 'Schiphol Airport', 'Amsterdam Zuid', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk'], 118)}, {'Heemstede-Aerdenhout': (['Heemstede-Aerdenhout', 'Haarlem', 'Amsterdam Sloterdijk', 'Zaandam', 'Hoorn', 'Alkmaar', 'Den Helder'], 109)}]

traject1 = ['Amsterdam Amstel', 'Amsterdam Centraal', 'Amsterdam Sloterdijk', 'Haarlem', 'Beverwijk', 'Zaandam', 'Castricum', 'Alkmaar']

def somTijd(traject, classname):
	tijdLijst = []

	for i in range(len(traject) - 1):
		verbindingen = classname.verbinding[traject[i]]
		tijdLijst += [item[0] for item in verbindingen if item[1] == traject[i + 1] ]

	trajectTijd = sum(tijdLijst)
	return trajectTijd

def staart(lijnvoering, classname, trajectTijd):
	indexTraject = random.randint(0, (len(lijnvoering) - 1))
	indexStation = random.randint(0, (len(lijnvoering[indexTraject].values()[0][0]) - 2))

	veranderTraject = lijnvoering[indexTraject].values()[0][0]
	veranderStation = veranderTraject[indexStation]
	beginTraject = veranderTraject[:indexStation+1]

	print veranderTraject
	print beginTraject

	tijd = somTijd(beginTraject, classname)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation in 
			classname.verbinding[veranderStation] if eindstation != veranderTraject[indexStation + 1] and eindstation not in beginTraject]

	if len(verbindingen) >= 1:
		nieuweVerbinding = random.choice(verbindingen)
		route = randomRoute(nieuweVerbinding[1], trajectTijd - tijd, classname, beginTraject)
		beginTraject = route[0]
		tijd += route[1]

	return beginTraject, tijd

def hillClimber2(trajectTijd, aantalTrajecten, classname):
	""" Maak een random combinate van trajecten als start state
	en verander elke keer 1 beginstation. Neem de verandering aan
	als het beter is en anders door naar een volgende optie. In het
	archief wordt bijgehouden of niet dezelfde combinaties geprobeerd
	worden. 
	"""
	beginStations = random.sample(classname.stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations)
	currentScore = scoreLijnvoering(currentState)
	archief = [sorted(beginStations)]
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	aantal_interaties = 0
	y_waardes = []
	c = 0

	# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
	while c < 1000:
		aantal_interaties += 1
		y_waardes.append(currentScore)
		newState = staart(currentState, classname, trajectTijd)
		newScore = scoreLijnvoering(newState)

		if newScore > currentScore:
			currentState = newState
			currentScore = newScore
			beginStations = nieuweStations
			c = 0

		else:
			c += 1

	return currentState, currentScore
