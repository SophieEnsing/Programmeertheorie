# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

import csv

# Class voor netwerk van verbindingen en stations.
class netwerkClass:
    def __init__(self):
        self.stations = []
        self.stationsKritiek = []
        self.verbinding = {}
        self.verbindingKritiek = []
        self.coordinaten = {}
        self.edges = []

    def inlezenStations(self, csvBestand):
        with open(csvBestand, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.stations.append(row[0])
                self.coordinaten[row[0]] = (float(row[1]), float(row[2]))

                if row[3] == 'Kritiek':
                    # Voeg alle kritieke stations toe aan een lijst.
                    self.stationsKritiek.append(row[0])

    def inlezenVerbindingen(self, csvBestand, classname):
        with open(csvBestand, 'r') as csvfile:    
            reader = csv.reader(csvfile, delimiter=',')
            
            for row in reader:
                # Alle verbindingen toevoegen per station in een dictionary.
                self.verbinding[row[0]] = self.verbinding.get(row[0], []) + [(float(row[2]), row[1])]
                self.verbinding[row[1]] = self.verbinding.get(row[1], []) + [(float(row[2]), row[0])]
                self.edges.append((row[0], row[1], row[2]))

                # Maak een lijst van alle kritieke verbindingen.
                if row[0] in classname.stationsKritiek or row[1] in classname.stationsKritiek:
                    self.verbindingKritiek.append((row[0], row[1]))

# Aanmaken van Holland Class.
Holland = netwerkClass()
Holland.inlezenStations('Data/StationsHolland.csv')
Holland.inlezenVerbindingen('Data/ConnectiesHolland.csv', Holland)

# Aanmaken van Nederland Class.
Nederland = netwerkClass()
Nederland.inlezenStations('Data/StationsNationaal.csv')
Nederland.inlezenVerbindingen('Data/ConnectiesNationaal.csv', Nederland)
