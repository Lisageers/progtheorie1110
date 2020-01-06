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

Stap 2 - datastructuur voor wiring en cost function
  - We definiëren wiring als de groep coördinaten waar je kabel langs legt om twee gates met elkaar te verbinden.
  - is dat dan gewoon een lijst? (zoals in example_output?) daarin moeten ook de coördinaten van begin- en eindpunt
  - cost function: aantal punten in lijst - 1

  todo:
    - netlist (csv-file) inlezen
    - maak het hele algoritme dat het probleem oplost

Stap 3 - breid het uit met 7 lagen om het efficiënter te maken

Stap 4 - optimaliseer