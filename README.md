# Programmeertheorie

Deze case gaat over het maken van de lijnvoering van intercity treinen in Nederland. Het is de bedoeling dat wij binnen een gegeven tijdsframe een aantal trajecten moeten uitzetten. In onze case wordt een traject gedefinieerd als een route van sporen en stations waarover treinen heen en weer rijden. Een traject mag hierbij niet langer zijn dan een opgegeven tijdsframe.

## Installeren

* Networkx
* Numpy
* Matplotlib

Om deze libraries te installeren moet je de onderstaande code runnen.
```python
pip install -r requirements.txt
```

## Structuur

In onze git zijn meerdere mappen te vinden met bestanden. In de map Data staan de csv bestanden waarin de gegevens staan van de stations en de connecties. In de map Algoritmes staan bestanden met de python code voor de algoritmes. In de map Functies staan de python functies die nodig zijn om de algoritmes uit te voeren. Hierin is worden tevens classes aangemaakt die door alle python bestanden geïmporteerd kunnen worden. Als laatste hebben we ook nog een map Visualisaties waarin de visualisaties van de station en verbindingen gemaakt kunnen worden. Uiteindelijk komen alle bestanden uit die mappen samen in de __main__.py. Daarnaast is er nog de Resultaten map, waarin we een aantal csv bestanden hebben staan met scores van onze algoritmes. 

## Running

Voor het testen en uitvoeren van de verschillende algoritmes is het alleen nodig om het bestand __main__.py uit te voeren met Python 3. Dit bestand zal om input vragen, waardoor een keuze gemaakt kan worden voor een van de algoritmes en de verschillende delen van de opdracht.

Om de aparte algoritmes zelf uit te voeren met verschillende variabelen moet je eerst de onderstaande code runnen in de terminal.

```python 
python -i __main__.py
```

Hierna kan je alle algoritmes apart aanroepen. De functies hillClimber en simulatedAnnealing hebben 2 versies: de eerste gebruikt shortKritiek om trajecten te maken en verandert telkens hele beginstations en de tweede versie gebruikt een random traject en verandert telkens de staart binnen een traject. De parameters van de functies zijn: classnaam, maxTijd, maxTrajecten en kritiekKeuze. De classnaam is Holland of Nederland, de maxTijd het maximale aantal minuten per traject, maxTrajecten het maximale aantal trajecten en kritiekKeuze is True als alle verbindingen kritiek zijn en False als niet alle verbindingen kritiek zijn. Bij het randomalgoritme is de eerste parameter hoeveel iteraties je wil doen.

```python
randomAlgoritme (1000, classnaam, maxTijd, maxTrajecten, kritiekKeuze))

hillClimber (maxTijd, maxTrajecten, classnaam, kritiekKeuze))

simulatedAnnealing (maxTijd, maxTrajecten, classnaam, kritiekKeuze))

hillClimber2 (maxTijd, maxTrajecten, classnaam, kritiekKeuze))

simulatedAnnealing2 (maxTijd, maxTrajecten, classnaam, kritiekKeuze))
```

## Auteurs

Sophie Ensing, Gavin Schipper en Rosalie Snijders.

## Acknowledgements

Yannick Vinkesteijn & Bas Terwijn
