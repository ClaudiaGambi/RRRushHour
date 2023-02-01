# RRRushHour

Rush Hour is een ogenschijnlijk eenvoudig puzzeltje met een verrassend uitdagend karakter. In een veld van 6 hoog en 6 breed staat een rode auto 
en die moet naar de uitgang, die recht voor je ligt. Andere voertuigen versperren de weg; auto’s van twee eenheden lang en trucks van drie eenheden lang, 
die alleen in hun rijrichting bewogen mogen worden. Ze mogen niet draaien. De opdracht is simpel: beweeg de rode auto naar buiten.

## Experimenten

Dit script is geschreven met het doel om te onderzoeken hoe bepaalde algoritmen en heuristieken presteren bij verschillende startsituaties en de (eventuele) verschillen te verklaren. Er zijn verschillende algoritmen en heuristieken in het script te vinden: een Randomized search, een Breadth First search, een Breadth First search gecombineerd met een 'distance red car to exit' heuristiek, een Breadth First search gecombineerd met een 'number of blocking cars' heuristiek en A* gecombineerd met een 'distance to endstate' en een 'number of blocking cars' heuristiek.

De prestatie van de algoritmen is wordt verdeeld in drie onderdelen: voor hoeveel startsituaties er een oplossing wordt gevonden, hoe goed de gevonden oplossingen zijn en hoe efficient de zoektocht was.

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.9.2. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

### Gebruik

Voor de experimenten zijn alle algorimen met alle mogelijke borden gerunt. Deze worden gerunt met 4 argumenten: de naam van het algoritme, 
de naam van de inputfile (het bord), en een of twee outputfiles. Een voorbeeld hiervan is:

```
python main.py gameboards/Rushhour12x12_7.csv -m randomize -o1 output/end_board7.csv
```
De verschillende borden hebben de namen: gameboards/Rushhour6x6_1.csv, gameboards/Rushhour6x6_2.csv, gameboards/Rushhour6x6_3.csv, gameboards/Rushhour9x9_4.csv,
gameboards/Rushhour9x9_5.csv, gameboards/Rushhour9x9_6.csv, gameboards/Rushhour12x12_7.csv

De verschillende modes van het programma hebben de namen: Random, BreadthFirst, BF_Blocking, BF_NearExit, Astar, game en Visual.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/gameboards**: bevat de verschillende databestanden die nodig zijn om de verschillende spellen in te laden
- **/output**: bevat de outputfiles van de genomen stappen om een spel op te lossen en van de eindresultaten van borden (deze zijn weer nodig voor een ander algoritme)

## Auteurs
- Sveta Roopram
- Jennifer Batchelor
- Claudia Gambirasio
