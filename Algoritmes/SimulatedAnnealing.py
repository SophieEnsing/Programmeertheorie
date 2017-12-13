from __future__ import division
import random
import numpy as np
import csv
import math
from Functies.Score import *
from Functies.ShortKritiek import *
from Functies.Staart import *
from Functies.Grafiek import *

def acceptance(old, new, T):
	a = np.exp((new - old) / T)
	return a

#
# SIMULATED ANNEALING 1
#

def simulatedAnnealing(trajectTijd, aantalTrajecten, classname, kritiek):
	"""BESCHRIJVING"""	
	T = 1
	T_min = 0.0001

	beginStations = random.sample(classname.stations, aantalTrajecten)

	# Maak een begin state en archief aan
	currentState = lijnvoering(trajectTijd, beginStations, classname)
	currentScore = scoreLijnvoering(currentState, classname, kritiek)
	archief = [sorted(beginStations)]
	maxScore = 0
	newScore = 0
	bestStations = []
	
	# C houdt bij hoevaak achter elkaar er geen betere oplossing is
	aantal_iteraties = 0
	y_waardes = []
	max_waardes = []

	# Stop bij minimumtemperatuur
	while T > T_min:
		# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
		c = 0
		aantal_iteraties += 1
		y_waardes.append(newScore)
		max_waardes.append(maxScore)

		while c < 100:
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

				# Bereken acceptatiekans
				a = acceptance(currentScore, newScore, T)
				print(a, currentScore, newScore)

				if a > random.random():
					currentState = newState
					currentScore = newScore
					beginStations = nieuweStations

					if newScore > maxScore:
						maxScore = newScore
						bestStations = nieuweStations

			c += 1

		T = T - 0.01
	
	return maxScore

#
# SIMULATED ANNEALING 1
#

def simulatedAnnealing2(trajectTijd, aantalTrajecten, classname, kritiek):
	"""BESCHRIJVING"""
	T = 1
	T_0 = 1
	T_min = 0.0001

	beginState = randomAlgoritme(1, classname, trajectTijd, aantalTrajecten, kritiek)
	currentState = beginState[0]
	currentScore = beginState[1]

	maxScore = 0
	newScore = 0
	besteLijnvoering = []
	aantalIteraties = 0

	# Stop bij minimumtemperatuur
	while T > T_min:
		# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden
		c = 0
		aantalIteraties += 1
		while c < 1000:
			newState = staart(currentState, classname, trajectTijd)
			newScore = scoreLijnvoering(newState, classname, kritiek)

			# Bereken acceptatiekans
			a = acceptance(currentScore, newScore, T)
			print(a, currentScore, newScore)

			if a > random.random():
				currentState = newState
				currentScore = newScore

				if newScore > maxScore:
					maxScore = newScore
					besteLijnvoering = newState

			c += 1

		T = T_0 - ( aantalIteraties * ( (T_0 - T_min) / 1000) )
	
	return maxScore, besteLijnvoering