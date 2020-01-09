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

	def __init__(self, chip_file):
		self.gates = self.create_gates(chip_file)
		self.grid = self.create_grid(self.gates)

	def create_gates(self, chip_file):
		""" Create a dictionary of gates with their coordinates. """

		gates = {}

		# get gate coordinates from csv file
		with open(chip_file, 'r') as in_file:
			gate_reader = csv.DictReader(in_file)

			# write gates and coordinates to dictionary
			for row in gate_reader:
				gates[(int(row['x']), int(row['y']))] = row['chip']

		return gates

	def create_grid(self, gates):
		""" Create grid with gates. """

		n = self.get_x_dimension(gates)
		m = self.get_y_dimension(gates)

		# create empty grid
		grid = [[False for y in range(m)] for x in range(n)]

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

		# determine size of x-axis of grid
		for gate in gates:
			x_cor.append(gate[0])

		n = int(max(x_cor)) + 2

		return n

	def get_y_dimension(self, gates):
		
		y_cor = []

		# determine size of y-axis of grid
		for gate in gates:
			y_cor.append(gate[1])

		m = int(max(y_cor)) + 2

		return m
