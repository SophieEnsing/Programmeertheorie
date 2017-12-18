# Resultaten

## CSV-files
* OutputSA2Holland.csv
  * SARandom2HollandFalse t/m SARandom7HollandFalse
    
    *Het random simulated annealing algoritme uitgevoerd met een verschillend aantal trajecten voor Holland. 
    Per aantal trajecten (2 t/m 7) is het algoritme 10 keer uitgevoerd.* 
    
  * SARandom2HollandTrue t/m SARandom7HollandTrue
    
    *Het random simulated annealing algoritme uitgevoerd met een verschillend aantal trajecten voor Holland. 
    Per aantal trajecten (2 t/m 7) is het algoritme 10 keer uitgevoerd. Hierbij waren alle sporen gemarkeerd als **krtiek**.*
    
* OutputSA2Nederland.csv
    
  * NL10False t/m NL20False
  
    *Het random simulated annealing algoritme uitgevoerd met een verschillend aantal trajecten voor Nederland. 
    Per aantal trajecten (10 t/m 20) is het algoritme 5 keer uitgevoerd.*
    
  * SARandom10NederlandTrue t/m SARandom20NederlandTrue
  
    *Het random simulated annealing algoritme uitgevoerd met een verschillend aantal trajecten voor Nederland. 
    Per aantal trajecten (10 t/m 20) is het algoritme 5 keer uitgevoerd. Hierbij waren alle sporen gemarkeerd als **krtiek**.*
  
## Hill Climber: Shortkritiek vs Random
<img src=https://github.com/SophieEnsing/Programmeertheorie/blob/master/Resultaten/doc/1.png width="800">

We hebben zowel de Random Hill Climber als de ShortKritiek Hill Climber voor ieder aantal trajecten (2 t/m 7) 100 keer uitgevoerd. De algoritmes zijn uitgevoerd voor Holland en met de normale kritieke sporen. Dit heeft geresulteerd in de bovenstaande grafiek, waarin duidelijk de spreidingen van de twee algoritmes te zien zijn. De piek van hill climber met shortkritiek ligt tussen 8.750 en 9.000. De maximale score die gevonden is bij shortkritiek ligt onder de 9.500.

Bij de hill climber met de random instelling ligt de piek hoger, namelijk tussen de 9.750 en 10.000. De laagst gevonden score van dit algoritme ligt ongeveer gelijk met de hoogst gevonden score van de hill climber met shortkritiek. Kijkend naar deze resulaten kan geconcludeerd wordend dat de hill climber met het random algoritme beter werkt voor deze case. 

## Simulated Annealing: ShortKritiek vs. Random
### Holland
<img src=https://github.com/SophieEnsing/Programmeertheorie/blob/master/Resultaten/doc/3.png width="400"> <img src=https://github.com/SophieEnsing/Programmeertheorie/blob/master/Resultaten/doc/2.png width="400">

### Nederland
<img src=https://github.com/SophieEnsing/Programmeertheorie/blob/master/Resultaten/doc/4.png width="400"> <img src=https://github.com/SophieEnsing/Programmeertheorie/blob/master/Resultaten/doc/5.png width="400">

De vier grafieken hierboven vormen samen een representatie van hoe de twee verschillende versies van het simulated annealing algoritme werken ten opzichte van elkaar. Het gaat hierbij om het random simulated annealing algoritme en het simulated annealing algoritme dat gebruikt maakt van shortkritiek. Er is verder onderscheid gemaakt tussen Holland of Nederland en de normale kritieke verbindingen of alles kritiek. 

De verschillende combinaties van situaties zijn allemaal voor verschillende aantallen trajecten meerdere keren uitgevoerd. Uit de grafieken valt op te maken dat het random simulated annealing algoritme in alle combinaties beter presteert dan het simulated annealing algoritme met shortkritiek. Daarom kan geconcludeerd worden dat het random simulated annealing algoritme beter werkt voor deze case.
