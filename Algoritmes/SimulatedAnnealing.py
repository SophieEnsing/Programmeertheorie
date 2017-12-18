# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

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
	""" Deze functie berekent aan de hand van de temperatuur,
	de oude en de nieuwe score wat de acceptatiekans is van
	de situatie.
	"""
	a = np.exp((new - old) / T)
	return a

#
# SIMULATED ANNEALING 1
#

def simulatedAnnealing(trajectTijd, aantalTrajecten, classname, kritiek):
	""" Maak een random combinatie van trajecten als start state
	en verander steeds 1 beginstation en daarmee ook dat traject. Op
	basis van de acceptatiekans wordt bepaald of de verandering wordt
	aangenomen of niet, de verandering kan ook een verslechtering 
	betekenen. In het archief wordt bijgehouden of niet dezelfde 
	combinaties geprobeerd worden. Returned de beste score.
	"""	
	T = 1
	T_0 = 1
	T_min = 0.0001
	
	# Kies random beginstations.
	beginStations = random.sample(classname.stations, aantalTrajecten)

	# Maak een begin state en archief aan.
	currentState = lijnvoering(trajectTijd, beginStations, classname)
	currentScore = scoreLijnvoering(currentState, classname, kritiek)
	archief = [sorted(beginStations)]
	
	# Hou bij wat de best gevonden score is.
	maxScore = 0
	newScore = 0
	bestState = []
	aantalIteraties = 0

	# Stop bij minimumtemperatuur.
	while T > T_min:
		c = 0
		aantalIteraties += 1
		
		# Voer 100 iteraties uit per temperatuur.
		while c < 100:
			index = random.randint(0, (aantalTrajecten - 1)) 
			station = random.choice(classname.stations)

			# Als het nieuw gekozen station al in de beginstations staat.
			# kies een nieuw station.
			while station in beginStations:
				station = random.choice(classname.stations)

			# Pas een van de stations aan van de beginstations.
			nieuweStations = beginStations
			nieuweStations[index] = station
			nieuweStations = sorted(nieuweStations)

			# Check of de combinatie van stations niet in het archief staat.
			if nieuweStations not in archief:
				archief.append(nieuweStations)
				newState = lijnvoering(trajectTijd, nieuweStations, classname)
				newScore = scoreLijnvoering(newState, classname, kritiek)

				# Bereken acceptatiekans.
				a = acceptance(currentScore, newScore, T)
				
				# Als de situatie geaccepteerd wordt.
				if a > random.random():
					currentState = newState
					currentScore = newScore
					beginStations = nieuweStations
					
					# Hou bij wat het beste is tot nu toe.
					if newScore > maxScore:
						maxScore = newScore
						bestState = newState

			c += 1
			
		# Update de temperatuur lineair.
		T = T_0 - ( aantalIteraties * ( (T_0 - T_min) / 1000) )
	
	return maxScore, bestState

#
# SIMULATED ANNEALING 2
#

def simulatedAnnealing2(trajectTijd, aantalTrajecten, classname, kritiek):
	"""" Maak een random begin status door middel van het random 
	algoritme. Vervolgens wordt er door middel van de hulpfunctie
	staart in een van de trajecten een aanpassing gemaakt. Van de 
	nieuwe staat wordt de score berekend. Op basis van de acceptatiekans 
	wordt bepaald of de verandering wordt aangenomen of niet, de 
	verandering kan ook een verslechtering betekenen. Returned de 
	beste score. 
	"""
	T = 1
	T_0 = 1
	T_min = 0.0001
	
	# Maak een begin state aan.
	beginState = randomAlgoritme(1, classname, trajectTijd, aantalTrajecten, kritiek)
	currentState = beginState[0]
	currentScore = beginState[1]
	
	# Hou de maximale score en nieuwe score bij.
	maxScore = 0
	newScore = 0
	bestState = []
	aantalIteraties = 0

	# Stop bij minimumtemperatuur.
	while T > T_min:
		# Stop als er 100 keer achter elkaar geen betere oplossing is gevonden.
		c = 0
		aantalIteraties += 1
		while c < 100:
			# De staart functie verandert in een van de trajecten de staart van het traject.
			newState = staart(currentState, classname, trajectTijd)
			newScore = scoreLijnvoering(newState, classname, kritiek)

			# Bereken acceptatiekans.
			a = acceptance(currentScore, newScore, T)

			# Als de situatie geaccepteerd wordt.
			if a > random.random():
				currentState = newState
				currentScore = newScore

				# Hou bij wat het beste is tot nu toe.
				if newScore > maxScore:
					maxScore = newScore
					bestState = newState

			c += 1
		
		# Update de temperatuur lineair.
		T = T_0 - ( aantalIteraties * ( (T_0 - T_min) / 1000) )
	
	return maxScore, bestState
