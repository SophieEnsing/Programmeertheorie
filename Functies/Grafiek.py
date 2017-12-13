import matplotlib.pyplot as plt 

def grafiek(y_waardes, aantal_interaties):
	plt.plot(range(0,aantal_interaties), y_waardes)
	plt.axis([0, aantal_interaties, 0, 10000])
	plt.show()