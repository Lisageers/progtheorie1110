"""
grid.py

Minor programmeren - January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates a grid with gates to be connected.
"""

import csv


gates = {}
x_cor = []
y_cor = []

# hoe heet de file? moeten we die niet laten meegeven als input als de user het programma runt? (print_X.csv)
with open("file.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)

	for gate, x, y in csv_reader:
		gates[(x,y)] = gate
		x_cor.append(x)
		y_cor.append(y)

m = max(y_cor) + 1
n = max(x_cor) + 1

grid = {}

for y in range m:
	for x in range n:
		grid[(x,y)] = None

for gate in gates:
	if gate in grid:
		grid[gate] = gates[gate]