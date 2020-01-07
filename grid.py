"""
grid.py

Minor programmeren - January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates a grid with gates to be connected.
"""

import csv


class Grid():
	""" This class creates a grid with gates. """

	def __init__(self, filename):
		self.grid = self.create_grid(filename)

	def create_grid(self, filename):
		gates = {}
		x_cor = []
		y_cor = []

		with open(filename) as csv_print:
			csv_print = csv.reader(csv_print)
			next(csv_print)

			for gate, x, y in csv_print:
				gates[(int(x.strip()),int(y.strip()))] = gate
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

class Wiring():
	""" This class creates wires from netlists. """

	def __init__(self, filename, grid):
		self.grid = grid
		print(grid)
		self.netlist = self.netlist(filename)
		self.output(self.wire())

	def netlist(self, filename):
		with open(filename) as csv_netlist:
			csv_netlist = csv.reader(csv_netlist)
			next(csv_netlist)

			netlist = []

			for start, end in csv_netlist:
				netlist.append((start, end))

		return netlist

	def wire(self):
		self.output_dict = {}
		# coordinaten ophalen uit dict
		for net in self.netlist:
			wire = [cor for cor in self.grid if self.grid[cor] == net[0] or self.grid[cor] == net[1]]
			current_cor = wire[0]
			end_cor = wire[1]

			while True:

				# check of ze naast elkaar liggen manhattan distance
				if abs((current_cor[0] + current_cor[1]) - (end_cor[0] + end_cor[1])) == 1:
					output_dict[net] = wire
					break

				else:
					if (end_cor[0] - current_cor[0]) > 0:
						current_cor[0] += 1
						wire.append(current_cor)
					elif (end_cor[0] - current_cor[0]) < 0:
						current_cor[0] -= 1
						wire.append(current_cor)
					elif (end_cor[1] - current_cor[1]) > 0:
						current_cor[1] += 1
						wire.append(current_cor)
					else:
						current_cor[1] -= 1
						wire.append(current_cor)

		return output_dict


	def output(self, output_dict):

		# antwoord schrijven naar csv
		with open('output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			# write dictionary to dictionary?
			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wire' : wire})


if __name__ == "__main__":

	filename = input("Enter the filename of your print.\n")

	grid = Grid(filename)

	netlist_name = input("Enter the filename of the netlist to use.\n")

	netlist = Wiring(netlist_name, grid)
