from Algoritmes.HillClimber import *
from Algoritmes.Random import *
from Algoritmes.SimulatedAnnealing import *
from Functies.ReadData import *
from Visualisatie.Network import *

classnaam = Holland
kritiekKeuze = False

logo = """\

    __ _           _   _   _   _   _     
   |  _ \    _ _  ( ) | | | \ | | | |    
   | |_) |  / _ | | | | | |  \| | | |    
   |  _ <  | (| | | | | | | |\  | | |__ 
   |_| \_\  \_,_| |_| |_| |_| \_| |____|

"""

print(logo)

continueVar = ""

while continueVar == "" or continueVar == "j":
	print("")
	print("1 = Random algoritme")
	print("2 = Hillclimber algoritme")
	print("3 = Simulated Annealing algoritme")
	print("4 = Visualiseer het netwerk")
	print("")

	programmaKeuze = input("Welk programma wil je uitvoeren? ")
	print("")
	classKeuze = input("Voor alleen Noord- en Zuid-Holland kies 1 en voor heel Nederland kies 2: ")
	print("")
	kritiekKeuze = input("Om het programma normaal uit te voeren kies 1, om alle sporen als kritiek te behandelen kies 2: ")

	if classKeuze == 1:
		classnaam = Holland
	elif classKeuze == 2:
		classnaam = Nederland

	if kritiekKeuze == 1:
		kritiek = False
	elif kritiekKeuze == 2:
		kritiek = True

	if programmaKeuze == "1":
		print("")
		print("Score Holland: ", randomAlgoritme(1000, classnaam, 120, 7, kritiekKeuze))

	elif programmaKeuze == "2":
		print("")
		print("Score Holland: ", hillClimber(120, 7, classnaam, kritiekKeuze))

	elif programmaKeuze == "3":
		print("")
		print("Score Holland: ", simulatedAnnealing(120, 7, classnaam, kritiekKeuze))

	elif programmaKeuze == "4":
		visualisatie(classnaam)

	print("")
	continueVar = input("Druk 'j' om nog een algoritme te runnen, druk 'n' om te stoppen: ")