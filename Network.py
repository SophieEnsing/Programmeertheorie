import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()
stationsKritiek = []


with open('StationsHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        G.add_node(row[0], pos=(float(row[1]), float(row[2])))
        if row[3] == 'Kritiek':
        	stationsKritiek.append(row[0])

pos = {city:(long, lat) for city, (lat,long) in nx.get_node_attributes(G, 'pos').items()}

with open('ConnectiesHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
    	if row[0] in stationsKritiek or row[1] in stationsKritiek:
    		G.add_edge(row[0], row[1], color='r', weight = int(row[2]))
        else:
        	G.add_edge(row[0], row[1], color='b', weight = int(row[2]))

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
nx.draw(G, pos, with_labels = True, node_size = 50, edge_color=colors, font_size = 5)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size = 5)
plt.show()