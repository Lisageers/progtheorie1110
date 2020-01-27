import csv


class Chip(object):
	""" This class creates a 3D grid with gates on z=0, from a chosen csv-file. """

	def __init__(self, chip_file):
		self.gates = self.create_gates(chip_file)
		self.grid = self.create_grid(self.gates)


	def create_gates(self, chip_file):
		""" Create a dictionary of gates with their coordinates. """

		gates = {}

		# gates are at the lowest layer
		z = 0

		# get gate coordinates from csv file
		with open(chip_file, 'r') as in_file:
			gate_reader = csv.DictReader(in_file)

			# write gates and coordinates to dictionary
			for row in gate_reader:
				gates[(int(row['x']), int(row['y']), z)] = row['chip']

		return gates


	def create_grid(self, gates):
		""" Create 3D grid with gates. """

		# get x and y dimensions and set z dimension to 8, as specified in assignment.
		n = self.get_x_dimension(gates)
		m = self.get_y_dimension(gates)
		o = 8

		# create empty grid
		grid = [[[False for z in range(o)] for y in range(m)] for x in range(n)]

		# add gates to grid
		for gate in gates:
			grid[gate[0]][gate[1]][gate[2]] = gates[gate]

		return grid


	def check_empty(self, cor, grid):
		""" Check whether a specified point in the grid is empty. """

		if grid[cor[0]][cor[1]][cor[2]] == False:
			return True

		return False


	def get_x_dimension(self, gates):
		""" Determine the max value for x for the grid, based on gate with highest x-value. """

		x_cor = []

		# determine size of x-axis of grid
		for gate in gates:
			x_cor.append(gate[0])

		n = int(max(x_cor)) + 2

		return n


	def get_y_dimension(self, gates):
		""" Determine the max value for y for the grid, based on hate with highest y-value. """

		y_cor = []

		# determine size of y-axis of grid
		for gate in gates:
			y_cor.append(gate[1])

		m = int(max(y_cor)) + 2

		return m
