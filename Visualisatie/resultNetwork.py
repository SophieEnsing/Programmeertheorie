# RailNL
# Namen: Rosalie Snijders, Gavin Schipper & Sophie Ensing
# Groepsnaam: Brogrammers

import networkx as nx
import matplotlib.pyplot as plt
import csv

def resultaatVisualisatie(classname, lijnvoering):
    """ Maakt afhankelijk van de classname een netwerk 
    visualisatie van Holland/Nederland.
    """
    G = nx.Graph()
    
    for station in classname.stations:
        # Voeg alle stations als nodes toe met exacte coordinaten.
        G.add_node(station, pos = (float(classname.coordinaten[station][0]), float(classname.coordinaten[station][1])))
    
    # Dit zorgt ervoor dat de nodes correct geplaatst worden.
    pos = {city:(lon, lat) for city, (lat, lon) in nx.get_node_attributes(G, 'pos').items()}

    # Voeg alle verbindingen tussen stations toe als edges met de tijd als gewicht.
    for edge in classname.edges:
        # Als een van de stations kritiek is, is de verbinding kritiek -> rood.
        if (edge[0], edge[1]) in lijnvoering or (edge[1], edge[0]) in lijnvoering:
            G.add_edge(edge[0], edge[1], color='#31FD37', weight = float(edge[2]))
        
        # Als de stations niet kritiek zijn, is de verbinding niet kritiek -> blauw.
        else:
            G.add_edge(edge[0], edge[1], color='#FD9828', weight = float(edge[2]))
    
    # Teken alle edges met kleuren
    graphEdges = G.edges()
    colors = [G[u][v]['color'] for u,v in graphEdges]
    nx.draw(G, pos, node_size = 10, edge_color=colors, font_size = 5)
    
    # Geef de gewichten weer in de visualisatie
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size = 5)
    plt.show()
