"""
chip.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates an empty grid and adds gates.
"""

import csv


class Chip(object):
	""" This class creates a grid with gates. """

	def __init__(self, filename):
		self.gates = self.create_gates(filename)
		self.grid = self.create_grid(self.gates)

	def create_gates(self, filename):
		""" Create a dictionary of gates with their coordinates. """

		gates = {}

		# get gate coordinates from csv file
		with open(filename, 'r') as in_file:
			gate_reader = csv.DictReader(in_file)

			# write gates and coordinates to dictionary
			for row in gate_reader:
				gates[(int(row['x']), int(row['y']))] = row['chip']

		return gates

	def create_grid(self, gates):
		""" Create grid with gates. """

		y_cor = []
		x_cor = []

		# determine size of grid
		for gate in gates:
			x_cor.append(gate[0])
			y_cor.append(gate[1])

		m = int(max(y_cor)) + 2
		n = int(max(x_cor)) + 2

		# create empty grid
		grid = [[False for x in range(n)] for y in range(m)]

		# add gates to grid
		for gate in gates:
			grid[gate[0]][gate[1]] = gates[gate]

		return grid

	def check_empty(self, cor, grid):
		if grid[cor[0]][cor[1]] == False:
			return True

		return False

