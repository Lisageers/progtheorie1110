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

Visualisatie
  - matplotlib
  - assenstelsel met stippen voor gates en dikkere lijnen voor wires

Stap 3 - breid het uit met 7 lagen om het efficiënter te maken

Stap 4 - optimaliseer



Links:
https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/ 
