# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

from Algoritmes.HillClimber import *
from Algoritmes.Random import *
from Algoritmes.SimulatedAnnealing import *
from Functies.ReadData import *
from Visualisatie.Network import *
from Visualisatie.resultNetwork import *

logo = """\

    __ _           _   _   _   _   _     
   |  _ \    _ _  ( ) | | | \ | | | |    
   | |_) |  / _ | | | | | |  \| | | |    
   |  _ <  | (| | | | | | | |\  | | |__ 
   |_| \_\  \_,_| |_| |_| |_| \_| |____|

"""

print(logo)

continueVar = ""
classnaam = Holland
kritiekKeuze = False
maxTrajecten = 7
maxTijd = 120

while continueVar == "" or continueVar == "j":
	print("")
	print("1 = Random algoritme")
	print("2 = Hillclimber algoritme")
	print("3 = Hillclimber 2 algoritme")
	print("4 = Simulated Annealing algoritme")
	print("5 = Simulated Annealing 2 algoritme")
	print("6 = Visualiseer het gehele netwerk")
	print("")

	programmaKeuze = input("Welk programma wil je uitvoeren? ")
	print("")
	classKeuze = input("Voor alleen Noord- en Zuid-Holland kies 1 en voor heel Nederland kies 2: ")
	print("")
	kritiekKeuze = input("Om het programma normaal uit te voeren kies 1, om alle sporen als kritiek te behandelen kies 2: ")

	if classKeuze == 1:
		classnaam = Holland
		maxTijd = 120
		maxTrajecten = 7
	elif classKeuze == 2:
		classnaam = Nederland
		maxTijd = 180
		maxTrajecten = 20

	if kritiekKeuze == 1:
		kritiek = False
	elif kritiekKeuze == 2:
		kritiek = True

	if programmaKeuze == "1":
		print("")
		print("SCORE: ", randomAlgoritme(1000, classnaam, maxTijd, maxTrajecten, kritiekKeuze))
		print("")

	elif programmaKeuze == "2":
		print("")
		print("SCORE: ", hillClimber(maxTijd, maxTrajecten, classnaam, kritiekKeuze))
		print("")


	elif programmaKeuze == "3":
		print("")
		print("SCORE: ", hillClimber2(maxTijd, maxTrajecten, classnaam, kritiekKeuze))
		print("")
		
	elif programmaKeuze == "4":
		print("")
		print("SCORE: ", simulatedAnnealing(maxTijd, maxTrajecten, classnaam, kritiekKeuze))
		print("")

	elif programmaKeuze == "5":
		print("")
		print("SCORE: ", simulatedAnnealing2(maxTijd, maxTrajecten, classnaam, kritiekKeuze))
		print("")

	elif programmaKeuze == "6":
		visualisatie(classnaam)

	print("")
	continueVar = input("Druk 'j' om nog een algoritme te runnen, druk 'n' om te stoppen: ")