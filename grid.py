"""
grid.py

Minor programmeren - January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates a grid with gates to be connected.
"""

import csv

# moet dit niet gewoon een losse functie zijn, zonder een class te maken?
class Grid():
	""" This class creates a grid with gates. """

	def __init__(self, filename):
		self.grid = self.create_grid(filename)

	def create_grid(self, filename):
		gates = {}
		x_cor = []
		y_cor = []

		with open(filename) as csv_file:
			csv_reader = csv.reader(csv_file)
			next(csv_reader)

			for gate, x, y in csv_reader:
				gates[(int(x.strip()), int(y.strip()))] = gate
				x_cor.append(x)
				y_cor.append(y)

		m = int(max(y_cor)) + 2
		n = int(max(x_cor)) + 2

		grid = {}

		for y in range(m):
			for x in range(n):
				grid[(x,y)] = None

		for gate in gates:
			if gate in grid:
				grid[gate] = gates[gate]

		return grid

if __name__ == "__main__":

	filename = input("Enter the filename of your print.\n")

	grid = Grid(filename)

	netlist = input("Enter the filename of the netlist to use.\n")