# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

import random
from Algoritmes.Random import *

def somTijd(traject, classname):
	
	"""Bereken wat de totale tijd is van een bepaald traject. """
	
	tijdLijst = []
	
	# Maak een lijst van de tijden van elke verbinding in een traject.
	for i in range(len(traject) - 1):
		verbindingen = classname.verbinding[traject[i]]
		tijdLijst += [item[0] for item in verbindingen if item[1] == traject[i + 1] ]
	
	trajectTijd = sum(tijdLijst)
	return trajectTijd

def staart(lijnvoering, classname, trajectTijd):
	
	""" Kies een random traject in een lijnvoering en kies
	binnen dat traject een random station om vanuit dat 
	station andere verbindingen te maken als dat mogelijk is.
	Hierdoor verandert de staart van een traject"""
	
	beginTraject = []
	
	# Kies een random traject en een random station binnen dat traject.
	indexTraject = random.randint(0, (len(lijnvoering) - 1))
	indexStation = random.randint(0, (len(lijnvoering[indexTraject][0]) - 2))

	veranderTraject = lijnvoering[indexTraject][0]
	veranderStation = veranderTraject[indexStation]
	beginTraject = veranderTraject[:indexStation+1]

	# Bereken de tijd van het traject tot het station waarvandaan de verbindingen gaan veranderen.
	tijd = somTijd(beginTraject, classname)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation in 
			classname.verbinding[veranderStation] if eindstation != veranderTraject[indexStation + 1] and eindstation not in beginTraject]
	
	# Maak een nieuwe route vanaf het random gekozen station als het station een andere mogelijke verbinding heeft.
	if len(verbindingen) >= 1:
		route, tijd = randomRoute(veranderStation, trajectTijd, classname, tijd, beginTraject[:-1])
		lijnvoering[indexTraject] = (route, tijd)

	return lijnvoering
