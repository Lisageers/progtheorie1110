
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

* Gates in een grid verbinden. Welke gates verbonden moeten worden staat vast in een netlist. Je wil het liefst de snelste weg vinden van gate A naar gate B, zodat je de kosten zo laag mogelijk houdt.
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