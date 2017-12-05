import random
import math

def acceptance(old, new, T):
	a = math.exp( ( old - new ) / T )
	return a


def SimulatedAnnealing():
	T = 1.0
    T_min = 0.00001
    alpha = 0.9

	beginStations = random.sample(stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations)
	currentScore = scoreLijnvoering(currentState)
	archief = [sorted(beginStations)]
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	c = 0

	# Stop bij minimumtemperatuur
	while T > T_min:
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

				# Bereken acceptatiekans
				a = acceptance(currentScore, newScore, T)

				if a > random():
					currentState = newState
					currentScore = newScore
					beginStations = nieuweStations

			c += 1

		T = alpha * T

	return currentScore, beginStations