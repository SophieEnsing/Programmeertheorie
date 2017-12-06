from Algoritmes.HillClimber import *
from Algoritmes.Random import *
from Algoritmes.SimulatedAnnealing import *
from Functies.ReadData import *

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
print("")

algoritme = raw_input("Welk algoritme wil je uitvoeren? ")
print("")
classKeuze = raw_input("Voor alleen Noord- en Zuid-Holland kies 1 en voor heel Nederland kies 2. ")

if algoritme == "1":
	if classKeuze == "1":
		print(randomAlgoritme(1000, Holland))
	elif classKeuze == "2":
		print(randomAlgoritme(1000, Nederland))

elif algoritme == "2":
	if classKeuze == "1":
		print(hillClimber(120, 7, Holland))
	elif classKeuze == "2":
		print(hillClimber(120, 7, Nederland))

elif algoritme == "3":
	if classKeuze == "1":
		print(simulatedAnnealing(120, 7, Holland))
	elif classKeuze == "2":
		print(simulatedAnnealing(120, 7, Nederland))

