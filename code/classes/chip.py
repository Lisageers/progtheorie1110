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
		with open(f'data/chip_1/{filename}') as in_file:
			chip_reader = csv.reader(in_file)
			next(chip_reader)

			# write gates and coordinates to dictionary
			for gate, x, y in chip_reader:
				gates[(int(x.strip()), int(y.strip()))] = gate

		return gates

	def create_grid(self, gates):
		""" Create grid with gates. """

		n = self.get_x_dimension(gates)
		m = self.get_y_dimension(gates)

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

	def get_x_dimension(self, gates):

		x_cor = []

		# determine size of grid
		for gate in gates:
			x_cor.append(gate[0])

		n = int(max(x_cor)) + 2

		return n

	def get_y_dimension(self, gates):
		y_cor = []

		for gate in gates:
			y_cor.append(gate[1])

		m = int(max(y_cor)) + 2

		return m
