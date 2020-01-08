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
		grid = [[False for x in range(n)] for y in range(m)]

		# add gates to grid
		for gate in gates:
			grid[gate[0]][gate[1]] = gates[gate]

		return grid

	def check_empty(self, cor, grid):
		if grid[cor[0]][cor[1]] == False:
			return True

		return False


class Netlist():
	""" This class creates a usable netlist. """

	def __init__(self, filename, gates):
		self.netlist = self.netlist(filename)
		self.net_cor = self.net_cor(self.netlist, gates)

	def netlist(self, filename):
		""" Create list type netlist from csv file. """

		with open(filename) as csv_netlist:
			csv_netlist = csv.reader(csv_netlist)
			next(csv_netlist)

			netlist = []

			for start, end in csv_netlist:
				netlist.append((start.strip(), end.strip()))

		return netlist

	def net_cor(self, netlist, gates):
		""" Create altered netlist with coordinates instead of names. """

		net_cor = []

		for net in netlist:
			for gate in gates:
				if gates[gate] == net[0]:
					cor_start = gate
				elif gates[gate] == net[1]:
					cor_end = gate

			net_cor.append((cor_start, cor_end))

		return net_cor


class Wiring():
	""" This class creates wires to connect gates as listed in netlist. """

	def __init__(self, netlist, grid):
		self.print = grid
		self.net_cor = netlist.net_cor
		self.output(self.wire())

	def wire(self):
		""" Determine wire needed to connect the nets. """

		output_dict = {}

		for net in self.net_cor:
			wire = []
			wire.append(net[0])

			current_cor = list(net[0])
			end_cor = net[1]

			while True:
				# check whether current point and end point are adjacent (manhattan distance)
				if (abs(current_cor[0] - end_cor[0]) == 1 and current_cor[1] - end_cor[1] == 0) or (abs(current_cor[1] - end_cor[1]) == 1 and current_cor[0] - end_cor[0] == 0):
					wire.append(net[1])
					output_dict[net] = wire
					break

				# move towards the end-gate
				else:
					print("wire: ", wire)
					if (end_cor[0] - current_cor[0]) > 0 and self.print.check_empty(((current_cor[0] + 1), current_cor[1]), self.print.grid):
						current_cor[0] += 1
						self.print.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[0] - current_cor[0]) < 0) and self.print.check_empty(((current_cor[0] - 1), current_cor[1]), self.print.grid):
						current_cor[0] -= 1
						self.print.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[1] - current_cor[1]) > 0) and self.print.check_empty((current_cor[0], (current_cor[1] + 1)), self.print.grid):
						current_cor[1] += 1
						self.print.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[1] - current_cor[1]) < 0) and self.print.check_empty((current_cor[0], (current_cor[1] - 1)), self.print.grid):
						current_cor[1] -= 1
						self.print.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))


		print("dict:", output_dict)
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

	grid = Print(filename)

	netlist_name = input("Enter the filename of the netlist to use.\n")

	netlist = Netlist(netlist_name, grid.gates)

	wiring = Wiring(netlist, grid)
