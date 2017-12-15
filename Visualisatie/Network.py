import networkx as nx
import matplotlib.pyplot as plt
import csv

def visualisatie(classname):
    G = nx.Graph()
    for station in classname.stations:
        G.add_node(station, pos=(float(classname.coordinaten[station][0]), float(classname.coordinaten[station][1])))

    pos = {city:(lon, lat) for city, (lat, lon) in nx.get_node_attributes(G, 'pos').items()}

    for edge in classname.edges:
        if edge[0] in classname.stationsKritiek or edge[1] in classname.stationsKritiek:
            G.add_edge(edge[0], edge[1], color='r', weight = float(edge[2]))
        else:
            G.add_edge(edge[0], edge[1], color='b', weight = float(edge[2]))

    graphEdges = G.edges()
    colors = [G[u][v]['color'] for u,v in graphEdges]
    nx.draw(G, pos, with_labels = True, node_size = 10, edge_color=colors, font_size = 5)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size = 5)
    plt.show()