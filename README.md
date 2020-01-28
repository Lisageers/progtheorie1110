
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

### Uitleg van de case:

Bij chips & circuits is het de bedoeling gates op een chip te verbinden met zo kort mogelijke kabels, die elkaar en de gates niet kruisen.  Welke gates verbonden moeten worden staat vast in een netlist. De chip wordt weergegeven als grid met de x- en y-dimensies zo dat er één extra rand om de buitenste gates om ligt. Er kan in de z-richting zeven lagen worden uitgebreid, om meer kabels te kunnen leggen. Kabels mogen alleen via de gridlijnen bewegen. Elke stap tussen coördinaten kost 1. Wanneer een kabel niet gelegd kan worden, worden daar extra kosten voor in rekening gebracht.


<img src="doc/grid_uitleg.PNG" alt="grid_uitleg" width="400px">

*Figuur 1) Voorbeeldchip. Deze gates moeten met elkaar verbonden worden.*

<img src="doc/test.png" alt="test plaatje" width="400px">

*Figuur 2) Voorbeeldnetlist, waarbij de gates met elkaar verbonden zijn met de laagste kosten (20)*


Het voorbeeld in Figuur 2 is makkelijk op te lossen met 2D-bewegingen. Het korste pad op een othogonaal grid heet de manhattan distance. In Figuur 1 is te zien dat dit snel verkeerd kan gaan; kabels zouden moeten kruisen bij enkel 2D-bewegingen naar hun doel. Dit probleem is in Figuur 3 weergegeven.


<img src="doc/probleem_plaatje.png" alt="probleem plaatje" width="400px">

*Figuur 3) Visualisatie van het probleem wanneer alleen in de x- en y-richting bew0gen mag worden.*


Om meer gates met elkaar te kunnen verbinden kunnen extra lagen in de z-richting worden toegevoegd, maximaal zeven. Figuur 4 laat zien hoe in de z-richting bewogen kan worden, waardoor kruising voorkomen wordt.


<img src="doc/oplossing_probleem.png" alt="oplossing voor het probleem" width="400px">

*Figuur 4) Kabels kunnen ook in de z-richting bewegen, waardoor ze andere kabels niet hoeven te kruisen.*

Figuur 4 is relatief eenvoudig opgelost met deze maatregel, maar de aanpak van een chip zoals Figuur 1 vereist meer maatregelen. In Figuur 5 is diezelfde chip te zien waarbij gebruik wordt gemaakt van meerdere lagen. Toch is hier pas zestig procent van de te leggen kabels gelegd. 


<img src="doc/60procent.png" alt="60procent" width="400px">

*Figuur 5) In deze afbeelding is slechts zestig procent van de te leggen kabels gelegd. De overige veertig procent van de kabels loopt ergens vast, waardoor verbinden niet meer lukt.*

### Ordening netlist

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


### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol uit te voeren. Deze zijn te installeren via pip met het volgende commando:

```
pip install -r requirements.txt
```

### Gebruik
Het programma kan gerund worden door het aanroepen van:

```
python main.py
```

Bij het runnen van het programma krijgt de gebruiker verschillende opties. Bij elke keuze die een gebruiker kan maken staat duidelijk waaruit de gebruiker kan kiezen::
- Maak een keuze welke chip je wil gebruiken.
- Maak een keuze welke netlist je wil gebruiken.
- Maak een keuze hoe je de netlist gesorteerd wil hebben.
- Maak een keuze welk algoritme je wil kiezen.
- Maak een keuze of je nadat het algoritme is uitgevoerd gebruik wil maken van de hill climber.
- Maak een keuze of je bij het leggen van de wires gebruik wil maken van loose_layering.

Wanneer je al deze keuzes gemaakt hebt krijg je een output:
- Een matplotlib met hoe de wires gelegd zijn met verschillende kleuren voor verschillende wires.
- Hoeveel wires er gelegd zijn.
- De totale kosten.


### Process
Tijdens het vak Programmeertheorie hebben wij een process bijgehouden. Deze vind je terug in de 'sjips' map. Hierin staat wat we gedaan hebben, hoe we door het project heen gelopen zijn, problemen waar we tegenaan gelopen zijn en keuzes die we gemaakt hebben.


### Problemen met github
* De laptop van Marte is de eerste dag van het vak (maandag 6 januari 2020) kapot gegaan. Hierdoor heeft Marte de eerste week weinig kunnen pushen en pullen via github. Deze dagen heeft ze wel veel meegewerkt.
* Lisa pushte eerst met een andere naam (de naam van haar laptop: Vince). Hier kwamen we pas eind van de eerste week achter, waardoor het lijkt alsog ook Lisa niet gupusht en gepulled had. Dit was wel zo.
