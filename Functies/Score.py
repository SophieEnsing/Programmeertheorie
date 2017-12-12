from __future__ import division

def scoreLijnvoering(lijnvoering, classname, kritiek):
	""" Bereken de score van de lijnvoering
	Score functie S > S = p*10000 - (t*20 + min/100000)
	"""

	verbindingen = []
	aantalTrajecten = len(lijnvoering)
	aantalMinuten = 0

	for traject in lijnvoering:
		# Bijhouden van totale tijd in minuten van de lijnvoering
		aantalMinuten += traject[1]
		traject = traject[0]

		# Maak van een traject een lijst van verbindingen in dat traject
		trajectParen = [(traject[i], traject[i+1]) for i in range(0, len(traject)-1 ,1)]
		# Check voor elke verbinding of een van de stations kritiek is
		trajectParen2 = [traject for traject in trajectParen if traject[0] in classname.stationsKritiek or traject[1] in classname.stationsKritiek]
		# Voeg de kritieke verbindingen toe aan een lijst
		verbindingen += trajectParen2

	# Set van verbindingen om dubbele tuples te voorkomen
	setTrajectParen = list(set([ tuple(sorted(t)) for t in verbindingen]))
	percKritiek = len(setTrajectParen) / len(classname.verbindingKritiek)

	S = (percKritiek * 10000) - ((aantalTrajecten * 20) + (aantalMinuten / 100000))
	return S