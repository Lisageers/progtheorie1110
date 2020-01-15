# Programmeertheorie

## Chips & circuits - Sjips

### Auteurs: Marte van der Wijk, Lisa Geers, Emma Caarls

## Week 1

### Maandag

Project gekozen: chips & circuits

Stap 1 - datastructuur voor het grid
  - grid als matrix lijkt visueel logisch, maar is mensendenken en niet computerdenken
  - gekozen voor een dictionary van coördinaten gekoppeld aan gates, want dat is minder complex. (wel minder visueel, maar dat maakt niet uit.)

  todo:
    - dictionary voor grid maken
    - csv file voor gates inlezen en die in het grid zetten
    - maak dit geheel als een class die de gevulde dictionary returned

### Dinsdag

Stap 2 - datastructuur voor wiring en cost function
  - csv file met netlist inlezen
  - We definiëren wiring als de groep coördinaten waar je kabel langs legt om twee gates met elkaar te verbinden.
  - is dat dan gewoon een lijst? (zoals in example_output?) daarin moeten ook de coördinaten van begin- en eindpunt
  - cost function: aantal punten in lijst - 1

  todo:
    - netlist (csv-file) inlezen
    - wat is een handige datastructuur voor de netlist? hoe willen we hem gebruiken? -> lijst met tuples, makkelijk op te halen, niet te complex
    - output moet een csv-file met de wiring zijn. schrijven naar een dictionary, zodat we zo nodig makkelijk met de output verder kunnen werken (bijvoorbeeld om resultaten te vergelijken voor optimaliseren)
    - maak het hele algoritme dat het probleem oplost
    - wire bevat sowieso start en eind
    - hoe loop je tussen start en eind? kijk om je heen, wat is de value van de coördinaten naast je? hoe ligt eind ten opzichte van current
    - vergelijk eind en current eerst op x en beweeg in de goede richting (dus verander current), als ze dan gelijk liggen ga je in y bewegen, totdat de manhattan distance 1/-1 is. Daarna ben je klaar.

    ! we weten dat hij nu dwars door gates heen gaat en niet op gaat letten op kruisen, maar het begin is er.

  dingen geleerd uit debuggen:
    - tuples zijn immutable. dat is eigenlijk wel handig, want de coordinaten van het grid en de gates mogen niet (per ongeluk) veranderen. De current_cor moet wel kunnen veranderen, dus die zetten we om naar een list.

  TODO: mmaak alles anders, matrix ipv dict!!!!!!!!!!!!!!!!!

### Woensdag

Visualisatie
  - matplotlib
  - assenstelsel met stippen voor gates en dikkere lijnen voor wires

Stap 2 verder
  - we hebben de classes aangepast en het grid is nu wel gewoon een matrix, want we hadden een denkfout maandag.
  - een eerste versie met constraints is gemaakt. Niet alle opgaven hebben daarmee een oplossing, want hij zal soms vast komen te zitten door de constraints en niet meer kunnen uitkomen bij het eindpunt.

  todo:
    - presentatie maken
    - visualisatie maken
    - proberen door randomisen betere oplossingen te bedenken. (dus de bekende error voorkomen)

### Donderdag

Vandaag
  - visualisatie gedaan en daarin ook bugs gefixt. Eerst werden teveel lijntjes getrokken (want alles één lijn) en nu niet meer. Ze krijgen allemaal los een kleurtje.
  - bugs gefixt in grid
  - hele nieuwe mappenstructuur, want dat hebben we gister in college geleerd. Het is nu overzichtelijker en losse onderdelen zijn beter herbruikbaar.
  - begonnen aan een nieuw algoritme. ipv van boven naar beneden de netlist af gaan we eerst dingen die op dezelfde as liggen verbinden.
  - begonnen aan random algoritme
  - begonnen aan inschatten probleemgrootte

todo:
  - namen van bestanden die ingelezen worden niet hardcoden maar wat dan wel? optie: variabele namen vergelijkbaar met de website van marte -> gedaan met nieuw menu
  - cost-function in Wire() zetten
  - 3D gaan

### Vrijdag

Stap 3 - breid het uit met 7 lagen om het efficiënter te maken

Vandaag
  - menu voor algoritme kiezen
  - Marte heeft weer werkende laptops :D
  - comments gemaakt
  - marte's zoektocht naar BFS bespreken
  - 3D matrix bespreken
    - de hele basis aanpassen naar 3D
    - xyz_move algoritme aanpassen naar 3D
  - plot ziet er nu 3d uit

Probleem met xyz_move: als een gate vanaf boven benaderd is en een volgende kabel wil dat ook doen dan loopt het vast. De tweede kabel hoeft niet meer in x en y te verschuiven en kan niet naar beneden dus gaat maar de hele tijd naar boven en het probleem heeft dan geen oplossing.

todo:
  - andere algoritmes aanpassen naar 3D
  - hele figuur 3D?? werkt dat nu al?
  - opslaan output waar? hoe? nu steeds dezelfde file
  - opslaan afbeelding die gemaakt wordt?
  - lezen over DFS

### Vrijdag van Marte
- Marte heeft weer Python

## Week 2

### Maandag

Vandaag
  - 3D gemaakt
  - Marte leest over DFS
  - error uit straight_first halen -> verkeerd geindente return
  - random laten loopen totdat hij een oplossing vindt
  - lezen over A*
  - algorithms van straight first en random netlist samengevoegd

### Dinsdag

Vandaag
  - A* implementeren -> [bron](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2)
  - we hebben de continue statement in python geleerd


todo:
  - bronvermelding A* algoritme in eigen code
  - verbeteren algoritme/uitvoer: gates met meeste connecties eerst, rechte lijnen eerst

vragen
  - waarom zou je def __eq__ (self, other) gebruiken om twee instances van een class te vergelijken op een bepaalde eigenschap, ipv gewoon die eigenschappen vergelijken met class_1.eigenschap == class_2.eigenschap?

### Later

Stap 4 - optimaliseer


### Links

https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/

[A* algorithm](https://gist.github.com/jamiees2/5531924)

https://matplotlib.org/
