import random
from Algoritmes.Random import *

def somTijd(traject, classname):
	tijdLijst = []

	for i in range(len(traject) - 1):
		verbindingen = classname.verbinding[traject[i]]
		tijdLijst += [item[0] for item in verbindingen if item[1] == traject[i + 1] ]

	trajectTijd = sum(tijdLijst)
	return trajectTijd

def staart(lijnvoering, classname, trajectTijd):
	beginTraject = []

	indexTraject = random.randint(0, (len(lijnvoering) - 1))
	indexStation = random.randint(0, (len(lijnvoering[indexTraject][0]) - 2))

	veranderTraject = lijnvoering[indexTraject][0]
	veranderStation = veranderTraject[indexStation]
	beginTraject = veranderTraject[:indexStation+1]

	tijd = somTijd(beginTraject, classname)

	verbindingen = [ (afstand, eindstation) for afstand, eindstation in 
			classname.verbinding[veranderStation] if eindstation != veranderTraject[indexStation + 1] and eindstation not in beginTraject]

	if len(verbindingen) >= 1:
		route, tijd = randomRoute(veranderStation, trajectTijd, classname, tijd, beginTraject[:-1])
		lijnvoering[indexTraject] = (route, tijd)

	return lijnvoering