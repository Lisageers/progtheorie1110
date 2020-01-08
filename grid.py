"""
grid.py

Minor programmeren - January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates a grid with gates to be connected.
"""

import csv

# moet dit niet gewoon een losse functie zijn, zonder een class te maken?
class Grid(object):
	""" This class creates a grid with gates. """

	def __init__(self, filename):
		self.grid = self.create_grid(filename)

	def create_grid(self, filename):
		""" Gate coordinates from a csv file are used to build a grid and the gates are added. """

		gates = {}
		x_cor = []
		y_cor = []

		# get gate coordinates from csv file, write to dictionary
		with open(filename) as csv_print:
			csv_print = csv.reader(csv_print)
			next(csv_print)

			for gate, x, y in csv_print:
				gates[(int(x.strip()), int(y.strip()))] = gate
				x_cor.append(x)
				y_cor.append(y)

		# determine size of grid
		m = int(max(y_cor)) + 2
		n = int(max(x_cor)) + 2

		grid = {}

		# create empty grid
		for y in range(m):
			for x in range(n):
				grid[(x,y)] = None

		# add gates to grid
		for gate in gates:
			if gate in grid:
				grid[gate] = gates[gate]

		return grid


class Wiring():
	""" This class creates wires to connect gates as listed in netlist. """

	def __init__(self, filename, grid):
		self.grid = grid
		self.netlist = self.netlist(filename)
		self.output(self.wire())

	def netlist(self, filename):
		""" Create list type netlist from csv file. """

		with open(filename) as csv_netlist:
			csv_netlist = csv.reader(csv_netlist)
			next(csv_netlist)

			netlist = []

			for start, end in csv_netlist:
				netlist.append((start.strip(), end.strip()))

		return netlist

	def wire(self):
		""" Determine wire needed to connect the nets. """
		
		output_dict = {}

		# get coordinates of gates to couple from grid
		for net in self.netlist:
			wire = []
			for cor in self.grid:
				if self.grid[cor] == net[0]:
					wire.insert(0, cor)
				elif self.grid[cor] == net[1]:
					wire.append(cor)

			print(wire)
			current_cor = list(wire[0])
			end_cor = wire[1]

			while True:
				# check whether current point and end point are adjacent (manhattan distance)
				if abs((current_cor[0] + current_cor[1]) - (end_cor[0] + end_cor[1])) == 1:
					print(current_cor)
					print("hij is klaar")
					output_dict[net] = wire
					break

				# move towards the end-gate
				else:
					if (end_cor[0] - current_cor[0]) > 0:
						print(current_cor)
						print("naar rechts")
						current_cor[0] += 1
						wire.append(tuple(current_cor))
					elif (end_cor[0] - current_cor[0]) < 0:
						current_cor[0] -= 1
						wire.append(tuple(current_cor))
					elif (end_cor[1] - current_cor[1]) > 0:
						current_cor[1] += 1
						wire.append(tuple(current_cor))
					else:
						current_cor[1] -= 1
						wire.append(tuple(current_cor))

		return output_dict


	def output(self, output_dict):

		# antwoord schrijven naar csv
		with open('output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			# write dictionary to dictionary?
			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})


if __name__ == "__main__":

	filename = input("Enter the filename of your print.\n")

	grid = Grid(filename)
	grid = grid.create_grid(filename)

	netlist_name = input("Enter the filename of the netlist to use.\n")

	netlist = Wiring(netlist_name, grid)
