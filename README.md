# Programmeertheorie

Deze case gaat over het maken van de lijnvoering van intercity treinen in Nederland. Het is de bedoeling dat wij binnen een gegeven tijdsframe een aantal trajecten moeten uitzetten. In onze case wordt een traject gedefinieerd als een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag hierbij niet langer zijn dan een opgegeven tijdsframe.

## Installeren

Voor het uitvoeren van het bestand Network.py is de python library networkx nodig. Dit bestand bevat een visualisatie van 
het eerste deel van de opdracht.

## Functies

Een eerste functie die wij hebben geschreven is een de functie 'shortKritiek'. Deze functie maakt vanuit een random 
beginstation een traject waarbij vanuit elk station het kortste kritieke pad wordt gekozen en als er geen kritiek pad is, het kortste niet kritieke pad. Deze functie krijgt een maximale tijd mee voor het traject. Daarnaast hebben wij een functie geschreven die verschillende trajecten combineert tot een lijnvoering, waarbij wordt aangegeven hoeveel trajecten in een lijnvoering mogen zitten. Als laatste hebben wij een functie geschreven waar de score van deze lijnvoering berekend wordt.

## Algoritmes

Voor ons eerste algoritme hebben wij een Hill Climber algoritme geschreven. Dit algoritme heeft als begin state een random combinatie van beginstations en hun bijhorende trajecten. Ons algoritme gaat dan telkens een beginstation vervangen voor een ander beginstation, waarna hij kijkt of de score verbeterd wordt na de verandering. Als de score beter is accepteert hij die combinatie als de nieuwe current state. Dit gaat door totdat hij 1000 keer geen verbetering heeft gevonden van de score.

## Visualisatie

Voor de visualisatie van de verbindingen hebben wij de python library networkx gebruikt. In dit netwerk zijn alle stations nodes en alle verbindingen tussen de stations de edges. De kritieke verbindingen zijn aangegeven door de rode kleur van de edges. De niet kritieke verbindingen zijn blauw. Bij alle edges wordt de tijd tussen de twee nodes als weight meegegeven en ook aangegeven in de grafiek.

## Auteurs

Sophie Ensing, Gavin Schipper en Rosalie Snijders.
