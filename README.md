# Programmeertheorie

Deze case gaat over het maken van de lijnvoering van intercity treinen in Nederland. Het is de bedoeling dat wij binnen een gegeven tijdsframe een aantal trajecten moeten uitzetten. In onze case wordt een traject gedefinieerd als een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag hierbij niet langer zijn dan een opgegeven tijdsframe.

## Opdracht deel 1: Noord- en Zuid-Holland

Voor onze case moeten wij als eerste een lijnvoering maken van de 22 belangrijkste intercitystations in Noord-Holland en Zuid-Holland. Van deze 22 stations zijn er 7 door RailNL als kritiek bestempeld: Alkmaar, Amsterdam Centraal, Den Haag Centraal, Gouda, Haarlem, Rotterdam Centraal en Zaandam. Alle verbindingen van en naar die kritieke stations zijn dus kritieke verbindingen.

Om de kwaliteit van de lijnvoering te berekenen is er een score functie opgesteld. Hierbij is de p het percentage bereden kritieke verbindingen, t het aantal trajecten en m het aantal minuten van alle trajecten in de lijnvoering.

S = p * 10000 - ( t * 20 + min / 100000 )

- Maak een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, waarbij zoveel mogelijk van de kritieke sporen bereden wordt. Als je 100% haalt heb je uiteraard de maximaal haalbare score bereikt.
- Maak wederom een lijnvoering voor Noord-Holland met maximaal zeven trajecten binnen een tijdsframe van twee uur, 
en probeer nu de score S zo hoog mogelijk te krijgen. 
- Ga er nu vanuit dat alle sporen in Holland kritiek zijn. Hoe hoog kun je nu de score maken?

## Opdracht deel 2: Nederland

- Maak wederom een lijnvoering voor heel Nederland met maximaal twintig trajecten binnen een tijdsframe van drie uur, en probeer nu 
de score S zo hoog mogelijk te krijgen. De scorefunctie blijft ongewijzigd. 
- Doe hetzelfde waarbij je alle sporen van Nederland als kritiek beschouwt. 
- Maak een aantrekkelijke visualisatie van je resultaten. Hoe je dat doet, mag je zelf bepalen.

## Advanced

- Utrecht Centraal gaat op de schop, en alle treinverbindingen van en naar Utrecht komen tijdelijk te vervallen omdat ze vervangen worden door bussen. Alle verbindingen tussen de stations die verbonden zijn met Utrecht zijn nu kritiek. Maak wederom een lijnvoering.
- Test voor uitval van andere stations hoe groot de impact is op je beste lijnvoering.

## Installeren

Voor het uitvoeren van het bestand Network.py is de python library networkx nodig. Dit bestand bevat een visualisatie van 
het eerste deel van de opdracht.

## Hulpfunctie

Een eerste functie die wij hebben geschreven is een de functie 'shortKritiekRoute'. Deze functie maakt vanuit een random 
beginstation een traject waarbij vanuit elk station het kortste kritieke pad wordt gekozen en als er geen kritiek pad is, het kortste niet kritieke pad. Deze functie krijgt een maximale tijd mee voor het traject. Daarnaast hebben wij een functie geschreven die verschillende trajecten combineert tot een lijnvoering, waarbij wordt aangegeven hoeveel trajecten in een lijnvoering mogen zitten. Als laatste hebben wij een functie geschreven waar de score van deze lijnvoering berekend wordt.

## Algoritmes

Voor ons eerste algoritme hebben wij een Hill Climber algoritme geschreven. Dit algoritme heeft als begin state een random combinatie van beginstations en hun bijhorende trajecten. Ons algoritme gaat dan telkens een beginstation vervangen voor een ander beginstation, waarna hij kijkt of de score verbeterd wordt na de verandering. Als de score beter is accepteert hij die combinatie als de nieuwe current state. Dit gaat door totdat hij 1000 keer geen verbetering heeft gevonden van de score.

## Auteurs

Sophie Ensing, Gavin Schipper en Rosalie Snijders.
