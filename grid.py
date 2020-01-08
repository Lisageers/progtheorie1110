"""
grid.py

Minor programmeren - January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates a grid with gates to be connected.
"""

import csv

class Print(object):
	""" This class creates a grid with gates. """

	def __init__(self, filename):
		self.gates = self.create_gates(filename)
		self.grid = self.create_grid(self.gates)

	def create_gates(self, filename):
		""" Create a dictionary of gates with their coordinates. """
		
		gates = {}

		# get gate coordinates from csv file
		with open(filename) as csv_print:
			csv_print = csv.reader(csv_print)
			next(csv_print)

			# write gates and coordinates to dictionary
			for gate, x, y in csv_print:
				gates[(int(x.strip()), int(y.strip()))] = gate

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
		grid = [[None for x in range(n)] for y in range(m)]

		# add gates to grid
		for gate in gates:


		return grid


class Netlist():
	""" This class creates a usable netlist. """

	def __init__(self, filename):
		self.netlist = self.netlist(filename)

	def netlist(self, filename):
		""" Create list type netlist from csv file. """

		with open(filename) as csv_netlist:
			csv_netlist = csv.reader(csv_netlist)
			next(csv_netlist)

			netlist = []

			for start, end in csv_netlist:
				netlist.append((start.strip(), end.strip()))

		return netlist	

class Wiring():
	""" This class creates wires to connect gates as listed in netlist. """

	def __init__(self, filename, grid):
		self.grid = grid.grid
		self.netlist = self.netlist(filename)
		self.output(self.wire())


	def wire(self):
		""" Determine wire needed to connect the nets. """
		
		output_dict = {}

		# dit moet ergens anders: grid of netlist
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

	netlist_name = input("Enter the filename of the netlist to use.\n")

	netlist = Wiring(netlist_name, grid)
