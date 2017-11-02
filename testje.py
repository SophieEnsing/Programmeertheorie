import networkx as nx
import matplotlib.pyplot as plt
import csv


print("hey")
print("dit is stom.")

G = nx.Graph()

with open('StationsHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        G.add_node(row[0], pos=(float(row[1]), float(row[2])))

pos = {city:(long, lat) for city, (lat,long) in nx.get_node_attributes(G, 'pos').items()}

with open('ConnectiesHolland.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        G.add_edge(row[0], row[1], weight = int(row[2]))

nx.draw(G, pos, with_labels = True, node_size = 50, font_size = 7)
plt.show()