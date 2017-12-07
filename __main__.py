from Algoritmes.HillClimber import *
from Algoritmes.Random import *
from Algoritmes.SimulatedAnnealing import *
from Functies.ReadData import *
from Visualisatie.Network import *

logo = """\

    __ _           _   _   _   _   _     
   |  _ \    _ _  ( ) | | | \ | | | |    
   | |_) |  / _ | | | | | |  \| | | |    
   |  _ <  | (| | | | | | | |\  | | |__ 
   |_| \_\  \_,_| |_| |_| |_| \_| |____|

  
"""

print(logo)

print("1 = Random algoritme")
print("2 = Hillclimber algoritme")
print("3 = Simulated Annealing algoritme")
print("4 = Visualiseer het netwerk")
print("")

programmaKeuze = input("Welk programma wil je uitvoeren? ")
print("")
classKeuze = input("Voor alleen Noord- en Zuid-Holland kies 1 en voor heel Nederland kies 2. ")

if programmaKeuze == "1":
	if classKeuze == "1":
		print(randomAlgoritme(1000, Holland))
	elif classKeuze == "2":
		print(randomAlgoritme(1000, Nederland))

elif programmaKeuze == "2":
	if classKeuze == "1":
		print(hillClimber(120, 7, Holland))
	elif classKeuze == "2":
		print(hillClimber(120, 7, Nederland))

elif programmaKeuze == "3":
	if classKeuze == "1":
		print(simulatedAnnealing(120, 7, Holland))
	elif classKeuze == "2":
		print(simulatedAnnealing(120, 7, Nederland))

elif programmaKeuze == "4":
	if classKeuze == "1":
		visualisatie('Data/StationsHolland.csv', 'Data/ConnectiesHolland.csv')
	elif classKeuze == "2":
		visualisatie('Data/StationsNationaal.csv', 'Data/ConnectiesNationaal.csv')
