# Programmeertheorie

Deze case gaat over het maken van de lijnvoering. Meer specifiek: over de lijnvoering van intercitytreinen. 
Dat betekent dat je binnen een gegeven tijdsframe een aantal trajecten uitzet. Een traject is een route van sporen en 
stations waarover treinen heen en weer rijden. Een traject mag niet langer zijn dan het opgegeven tijdsframe.

## Opdracht deel 1: Noord- en Zuid-Holland

In de provincies Noord- en Zuid-Holland liggen in totaal 118 treinstations, waarvan de 22 belangrijkste intercitystations met 
de tussenliggende spoorverbindingen, in een .csv-bestand zijn opgeslagen. De getallen die achter een verbinding staan zijn de 
reistijden in minuten. Van deze 22 stations zijn er 7 door RailNL als kritiek bestempeld: Alkmaar, Amsterdam Centraal, 
Den Haag Centraal, Gouda, Haarlem, Rotterdam Centraal en Zaandam. Je vindt ze in dit csv-bestand samen met hun x/y-coordinaten. 
Als deze stations niet regelmatig aangedaan worden treden er in de Randstad enorme logistieke problemen op door de grote aantallen 
overstappers op deze stations. De spoorverbindingen van en naar deze stations worden daarom kritieke verbindingen genoemd.

Maak een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, waarbij zoveel mogelijk 
van de kritieke sporen bereden wordt. Als je 100% haalt heb je uiteraard de maximaal haalbare score bereikt.

S = p * 10000 - ( t * 20 + min / 100000 )

Maak wederom een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
en probeer nu de score S zo hoog mogelijk te krijgen. Ga er nu vanuit dat alle sporen in Holland kritiek zijn. 
Hoe hoog kun je nu de score maken?

## Opdracht deel 2: Nederland

Maak wederom een lijnvoering voor heel Nederland met maximaal twintig trajecten binnen een tijdsframe van drie uur, en probeer nu 
de score S zo hoog mogelijk te krijgen. De scorefunctie blijft ongewijzigd. Doe hetzelfde waarbij je alle sporen van Nederland als 
kritiek beschouwt.Maak een aantrekkelijke visualisatie van je resultaten. Hoe je dat doet, mag je zelf bepalen.

## Installing

Voor het uitvoeren van het bestand Network.py is de python library networkx nodig. Dit bestand bevat een visualisatie van 
het eerste deel van de opdracht.

## Algoritmes

Het eerste algoritme wat wij nu hebben geschreven is een random algoritme 'shortRoute'. Dit algoritme maakt vanuit een random 
beginstation een traject waar steeds de dichtstbijzijnde optie gekozen wordt. Deze functie krijgt een maximale tijd mee voor het 
traject. Daarna worden er verschillende trajecten gecombineerd tot lijnvoering en wordt de score van deze lijnvoering berekend 
in de laatste functie.
