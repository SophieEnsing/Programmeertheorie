import csv

# Inlezen van alle data
stations = []
stationsKritiek = []

with open('Data/StationsHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        stations.append(row[0])
        if row[3] == 'Kritiek':
        	# Voeg alle kritieke stations toe aan een lijst
        	stationsKritiek.append(row[0])

verbinding = {}
verbindingKritiek = []

with open('Data/ConnectiesHolland.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	# Alle verbindingen toevoegen per station in een dictionary
        verbinding[row[0]] = verbinding.get(row[0], []) + [(int(row[2]), row[1])]
        verbinding[row[1]] = verbinding.get(row[1], []) + [(int(row[2]), row[0])]

        # Maak een lijst van alle kritieke verbindingen
        if row[0] in stationsKritiek or row[1] in stationsKritiek:
        	verbindingKritiek.append((row[0], row[1]))