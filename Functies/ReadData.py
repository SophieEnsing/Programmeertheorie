import csv

def inlezenStations(csvBestand):
    stations = []
    stationsKritiek = []
    with open(csvBestand, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            stations.append(row[0])
            if row[3] == 'Kritiek':
                # Voeg alle kritieke stations toe aan een lijst
                stationsKritiek.append(row[0])

    return stations, stationsKritiek

# Class voor Noord- en Zuid-Holland aanmaken
class hollandClass:
    stations = inlezenStations('Data/StationsHolland.csv')[0]
    stationsKritiek = inlezenStations('Data/StationsHolland.csv')[1]

    def __init__(self):
        self.verbinding = {}
        self.verbindingKritiek = {}

    def addVerbinding(self, verbindingen):
        self.verbinding = verbindingen

    def addVerbindingKritiek(self, verbindingen):
        self.verbindingKritiek = verbindingen

# Class voor Nederland aanmaken
class nederlandClass:
    stations = inlezenStations('Data/StationsNationaal.csv')[0]
    stationsKritiek = inlezenStations('Data/StationsNationaal.csv')[1]

    def __init__(self):
        self.verbinding = {}
        self.verbindingKritiek = {}

    def addVerbinding(self, verbindingen):
        self.verbinding = verbindingen

    def addVerbindingKritiek(self, verbindingen):
        self.verbindingKritiek = verbindingen

def inlezenVerbindingen(csvBestand, classname):
    verbinding = {}
    verbindingKritiek = []
    with open(csvBestand, 'r') as csvfile:    
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # Alle verbindingen toevoegen per station in een dictionary
            verbinding[row[0]] = verbinding.get(row[0], []) + [(float(row[2]), row[1])]
            verbinding[row[1]] = verbinding.get(row[1], []) + [(float(row[2]), row[0])]

            # Maak een lijst van alle kritieke verbindingen
            if row[0] in classname.stationsKritiek or row[1] in classname.stationsKritiek:
                verbindingKritiek.append((row[0], row[1]))

    return verbinding, verbindingKritiek

# Verbindingen toevoegen aan classes
Holland = hollandClass()
Holland.addVerbinding(inlezenVerbindingen('Data/ConnectiesHolland.csv', Holland)[0])
Holland.addVerbindingKritiek(inlezenVerbindingen('Data/ConnectiesHolland.csv', Holland)[1])

Nederland = nederlandClass()
Nederland.addVerbinding(inlezenVerbindingen('Data/ConnectiesNationaal.csv', Nederland)[0])
Nederland.addVerbindingKritiek(inlezenVerbindingen('Data/ConnectiesNationaal.csv', Nederland)[1])