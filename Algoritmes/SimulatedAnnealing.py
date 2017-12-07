from __future__ import division
import random
import numpy as np
import csv
import math
import matplotlib.pyplot as plt 
from Functies.Score import *
from Functies.ShortKritiek import *

# def grafiek(y_waardes, aantal_interaties):
# 	plt.plot(range(0,aantal_interaties), y_waardes)
# 	plt.axis([0, aantal_interaties, 0, 10000])
# 	plt.show()

def acceptance(old, new, T):
	a = np.exp((new - old) / T)
	return a

def simulatedAnnealing(trajectTijd, aantalTrajecten, classname, trajectFunctie):
	T = 1
	T_min = 0.0001
	#alpha = 0.999

	beginStations = random.sample(classname.stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations, classname)
	currentScore = scoreLijnvoering(currentState, classname)
	archief = [sorted(beginStations)]
	maxScore = 0
	bestStations = []
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	aantal_iteraties = 0
	y_waardes = []

	# Stop bij minimumtemperatuur
	while T > T_min:
		# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
		c = 0
		y_waardes.append(maxScore)
		#aantal_iteraties += 1

		while c < 100:
			#aantal_iteraties += 1
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
				newState = lijnvoering(trajectTijd, nieuweStations, classname, trajectFunctie)
				newScore = scoreLijnvoering(newState, classname)

				# Bereken acceptatiekans
				a = acceptance(currentScore, newScore, T)
				#print currentScore, newScore, a

				if a > random.random():
					currentState = newState
					currentScore = newScore
					beginStations = nieuweStations

					if newScore > maxScore:
						maxScore = newScore
						bestStations = nieuweStations

			c += 1

		T = T - 0.01

	#grafiek(y_waardes, aantal_iteraties)
	return maxScore