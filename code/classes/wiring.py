"""
wiring.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Creates the wiring to connect gates on a grid.
"""

import csv

class Wiring():
	""" This class creates wires to connect gates as listed in netlist. """

	def __init__(self, netlist, chip):
		self.chip = chip
		self.net_cor = netlist.net_cor
		self.wire = self.wire()
		self.output(self.wire)

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
					if (end_cor[0] - current_cor[0]) > 0 and self.chip.check_empty(((current_cor[0] + 1), current_cor[1]), self.chip.grid):
						current_cor[0] += 1
						self.chip.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[0] - current_cor[0]) < 0) and self.chip.check_empty(((current_cor[0] - 1), current_cor[1]), self.chip.grid):
						current_cor[0] -= 1
						self.chip.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[1] - current_cor[1]) > 0) and self.chip.check_empty((current_cor[0], (current_cor[1] + 1)), self.chip.grid):
						current_cor[1] += 1
						self.chip.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))
					elif ((end_cor[1] - current_cor[1]) < 0) and self.chip.check_empty((current_cor[0], (current_cor[1] - 1)), self.chip.grid):
						current_cor[1] -= 1
						self.chip.grid[current_cor[0]][current_cor[1]] = True
						wire.append(tuple(current_cor))

		return output_dict


	def output(self, output_dict):

		# antwoord schrijven naar csv
		with open('data/test/output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			# write dictionary to dictionary?
			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
