import random

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