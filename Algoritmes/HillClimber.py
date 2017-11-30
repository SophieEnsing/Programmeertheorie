import random

def hillClimber(trajectTijd, aantalTrajecten):
	""" Maak een random combinate van trajecten als start state
	en verander elke keer 1 beginstation. Neem de verandering aan
	als het beter is en anders door naar een volgende optie. In het
	archief wordt bijgehouden of niet dezelfde combinaties geprobeerd
	worden. 
	"""
	beginStations = random.sample(stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations)
	currentScore = scoreLijnvoering(currentState)
	archief = [sorted(beginStations)]
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	c = 0

	# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
	while c < 1000:
		index = random.randint(0, (aantalTrajecten - 1)) 
		station = random.choice(stations)

		while station in beginStations:
			station = random.choice(stations)

		# Pas een van de stations aan van de beginstations
		nieuweStations = beginStations
		nieuweStations[index] = station
		nieuweStations = sorted(nieuweStations)

		# Check of de combinatie van stations niet in het archief staat
		if nieuweStations not in archief:
			archief.append(nieuweStations)
			newState = lijnvoering(trajectTijd, nieuweStations)
			newScore = scoreLijnvoering(newState)

			# Check of de score beter is
			if newScore > currentScore:
				currentState = newState
				currentScore = newScore
				beginStations = nieuweStations
				c = 0

			else:
				c += 1

	return currentScore, beginStations