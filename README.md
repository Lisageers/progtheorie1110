
# Sjips
## Chips & Circuits

## Auteurs
* Emma Caarls
* Lisa Geers
* Marte van der Wijk

# Wat moet er in de read me
README
Voor de README kijken we o.a. naar:

De case waar de studenten mee bezig geweest zijn is duidelijk geïntroduceerd in de README.
De aanpak van de verschillende algoritmen is duidelijk beschreven in de README.
Het is na lezen van de README duidelijk hoe de resultaten te reproduceren zijn, via een interface (command line), argumenten die meegegeven kunnen worden voor de verschillende functionaliteiten/algoritmen, of bijvoorbeeld een duidelijke uitleg welke file te runnen om welk resultaat te krijgen.
#

### Case uitleg:

* Gates in een grid verbinden. Welke gates verbonden moeten worden staat vast in een netlist. Je wil het liefst de snelste weg vinden van gate A naar gate B, zodat je de kosten zo laag mogelijk houdt. Elke stap heeft een kosten van 1. Wanneer een wire niet gelegd kan worden, worden daar extra kosten voor in rekening gebracht.
* Wires mogen elkaar niet kruisen/ over dezelfde lijntje heen gaan/ door gates heen gaan.

<img src="doc/grid_uitleg.PNG" alt="grid_uitleg" width="400px">

*Voorbeeld grid. Deze gates moeten met elkaar verbonden worden.*


<img src="doc/test.png" alt="test plaatje" width="400px">

*Foto van test netlist, waarbij de gates met elkaar verbonden zijn met de kleinste kosten (20)*

* Deze gates kunnen door middel van x en y bewegingen met elkaar verbonden worden. De wire beweegt dan steeds dichter naar zijn target gate toe. Maar LET OP! Probleem

<img src="doc/probleem_plaatje.png" alt="probleem plaatje" width="400px">

*Visualisatie van het probleem wanneer je alleen in de x- en y-richting mag bewegen.*

* In de bovenstaande afbeelding is te zien dat de 2 lege gates niet met elkaar verbonden kunnen worden door alleen in de x- en y-richting te bewegen (manhattan distacnce).
* Om dit op te lossen maken we gebruik van extra lagen, zodat wires ook in de z-richting kunnen bewegen.

<img src="doc/oplossing_probleem.png" alt="oplossing voor het probleem" width="400px">

*Wires kunnen ook in de z-richting bewegen, waardoor ze andere wires niet hoeven te kruisen.*


* Dit ziet er allemaal nog eenvoudig uit, maar er zijn grotere grids, met meer gates die allemaal met elkaar verbonden moeten worden.

<img src="doc/60procent.png" alt="60procent" width="400px">

*In deze afbeelding zijn maar 60 procent van de gates met elkaar verbonden. De overige 40 procent van de te verbinden gates lopen ergens vast waardoor verbinden niet meer lukt.*

### Hoe kunnen we onze code verbeteren?

* Een andere ordening: most_common vooraan, zodat die niet ingebouwd kan worden. Gates kunnen met maximaal 5 andere gates verbonden worden. Om ervoor te zorgen dat de gates die zoveel verbindingen moeten leggen afgesneden worden plaatsten we deze vooraan de netlist, waardoor deze verbindingen alseerst gelegd worden.
* Er kan ook gesorteerd worden op "longest_first". Hierbij worden de gates die het verst van elkaar afliggen en met elkaar verbonden moeten worden als eerst in de netlist geplaatst. Deze hebben de meeste ruimte nodig en hebben de meeste kans om vast te lopen/ ingesloten te worden wanneer ze later nog gelegd moeten worden.


### Algortimen

* xyz_move: Wires verplaatsten zich eerst in de x-richting, dan in de y-richting en dan in de z-richting. Op weg naar zijn doel.
* astar: Het astar algoritme is een algoritme om in een graaf de korste weg te vinden tussen gates. De korste weg word bepaald door de laagste som. De som hangt af van de heuristiek (manhattan distance tot aan doel) en de gemaakt kosten om vanaf de start gate te komen (f = h + c).
* xyz_astar: Hier wordt in eerste instantie de xyz_move uitgevoerd. Maar bij het xyz_move algoritme kunnen niet alle wires gelegd worden, doordat er een aantal vastlopen. De overgebleven wires worden met het astar algoritme toch nog gelegd.
* hill climber: De hill climber wordt toegepast na het uitvoeren van een van deze algoritmen. Bij de hill climber worden de  wires strakker getrokken, zodat de totale kosten lager worden.


### Heuristieken

* Loose_layering: Met loose layering worden wires geforced om zich te verspreiden over de verschillende lagen. Hiermee wordt er een groter gedeelte van de ruimte benut, waardoor wires minder snel vast lopen. De eerste wires uit te list worden naar de bovenste laag gestuurd en zo steeds lager.
* Manhattan distance: Deze heuristiek berekend de kortste weg tussen gates.
* Distance_to_gate: Met deze heuristiek wordt ervoor gezorgd dat gates die meerdere verbindingen hebben niet afgesloten worden door andere wires. De heuristiek om toch een gate af te sluiten is veel hoger dan op via een andere (langere weg) te gaan.
* Loose_cables: Deze heuristiek zorgt ervoor dat het "aantrekkelijker" is om naar een hogere laag te gaan (waarbij de heuristiek voor laag 1 het laagst is). Het ik ook "aantrekkelijker" om, eenmaal boven, op een hogere laag te blijven.


### Menu
### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

### Gebruik
Het programma kan rerund worden door het aanroepen van:

```
python main.py
```

Bij het runnen van het programma krijgt de gebruiker verschillende opties:
- Maak een keuze welke chip je wil gebruiken.
- Maak een keuze welke netlist je wil gebruiken.
- Maak een keuze hoe je de netlist gesorteerd wil hebben.
- Maak een keuze welk algoritme je wil kiezen.
- Maak een keuze of je nadat het algoritme is uitgevoerd gebruik wil maken van de hill climber.
- Maak een keuze of je bij het leggen van de wires gebruik wil maken van loose_layering.

Wanneer je al deze keuzes gemaakt hebt krijg je een output:
- Een matplotlib met hoe de wires gelegd zijn.
- Hoeveel wires er gelegd zijn.
- De totale kosten.
