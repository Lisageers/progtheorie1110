# Code Sjips

## Classes

## chip.py
In chip.py wordt een grid met gates gemaakt, van een gekozen print uit de folder Data.

## netlist.py
In netlist.py wordt een gekozen netlist uit de folder Data ingelezen. Deze netlist kan op verschillende manieren geordend worden (sorted_netlist):
* Random: python kiest random een volgorde van nets (een net is een te maken verbinding tussen 2 gates). Hierdoor kan het resultaat elke keer anders zijn.
* Straight_first: Alle nets die op hetzelfde x- of y-coördinaat liggen worden vooraan de sorted_netlist geplaatst, waardoor deze als eerst met elkaar verbonden, daarna pas de rest (deze worden op volgorde, zoals ze in de netlist staan, gelegd). Zo is het zeker dat deze nets geen omweg hoeven te maken.
* Straight_random: Alle nets die op hetzelfde x- of y-coördinaat liggen worden vooraan de sorted_netlist geplaatst, waardoor deze als eerst met elkaar verbonden, daarna de rest op random volgorde.
* most_common: De gates die het vaakst voorkomen in de gekozen netlist komen vooraan de sorted_netlist te staan, zodat deze gates niet ingebouwd/afgesneden kunnen worden door andere nets.
* longest_first: De gates die het verst van elkaar afliggen en verbonden moeten worden met elkaar worden vooraan de sorted_netlist geplaatst. Deze kabels hebben de meeste ruimte nodig en hebben de meeste kans om vast te lopen/ ingesloten te worden wanneer ze later nog gelegd moeten worden. 


## wiring.py

In wiring.py wordt het gekozen algoritme, met gekozen heuristiek, aangeroepen. In wiring.py worden ook de kosten berekend. 


## Algoritmen

### xyz_move
Kabels verplaatsen zich eerst in de x-richting, dan in de y-richting en dan in de z-richting. Op weg naar zijn doel.

### astar
Het astar algoritme is een algoritme om in een graaf de korste weg te vinden tussen gates. De korste weg word bepaald door de laagste som. De som hangt af van de heuristiek (manhattan distance tot aan doel) en de gemaakte kosten om vanaf de start gate te komen (f = h + c).

### xyz_astar
Hier wordt in eerste instantie de xyz_move uitgevoerd. Maar bij het xyz_move algoritme kunnen niet alle wires gelegd worden, doordat er een aantal vastlopen. De overgebleven wires worden met het astar algoritme toch nog gelegd.

### hill climber
De hill climber wordt toegepast na het uitvoeren van een van deze algoritmen. Bij de hill climber worden de  wires strakker getrokken, zodat de totale kosten lager worden.


## Heuristieken

### loose_layering
Met loose layering worden kabels gedwongen om zich te verspreiden over de verschillende lagen. Hiermee wordt er een groter gedeelte van de ruimte benut, waardoor kabels minder snel vast lopen. De eerste kabels uit de sorted_netlist worden naar de bovenste laag gestuurd en zo steeds lager.

### manhattan_distance 
Deze heuristiek berekend de kortste weg tussen gates.

### distance_to_gate
Met deze heuristiek wordt ervoor gezorgd dat gates die meerdere verbindingen hebben niet afgesloten worden door andere wires. De heuristiek om toch een gate af te sluiten is veel hoger dan wanneer de kabel via een andere (langere weg) gaat.

### loose_cables
Deze heuristiek zorgt ervoor dat het "aantrekkelijker" (lagere heuristiek) is om naar een hogere laag te gaan (waarbij de heuristiek voor laag 1 het laagst is). Het ik ook "aantrekkelijker" om, eenmaal boven, op een hogere laag te blijven.