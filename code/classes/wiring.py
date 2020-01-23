"""
wiring.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Uses an algorithm to generate an output file with the solution for wiring.
"""

import csv
from code.algorithms.xyz_move import xyz_wire
from code.algorithms.astar import execute_astar
from code.algorithms.hillclimber_astar import HillClimber

class Wiring():
	""" This class outputs wires to connect gates as listed in netlist. """

	def __init__(self, netlist, chip, alg_req):
		self.chip = chip
		self.netlist = netlist

		algorithm, optimisation = self.choose_alg(alg_req)

		self.wire = algorithm(self.netlist, self.chip)

		if optimisation == 'y' or optimisation == 'yes':
			output_dict = HillClimber(chip, self.wire)
			self.wire = output_dict.run_hill

		self.output(self.wire)


	def choose_alg(self, alg_req):
		""" Get the algorithm the user chose. """

		if alg_req == 'xyz_move':
			algorithm = xyz_wire
		elif alg_req == 'astar':
			optimisation_input = input("Do you want to optimise the result with hillclimber? (y/n)\n").lower()
			algorithm = execute_astar

		return algorithm, optimisation_input


	def cost(self, output_dict):
		""" Calculate the cost of wire used in the solution. """

		cost = 0

		for net in output_dict:
			# penalty for missing wire: assume an 8th layer was needed, so add 16 for going up and down plus manhattan distance
			if output_dict[net] == [(0, 0, 0)]:
				manhattan_distance = abs(net[0][0] - net[1][0]) + abs(net[0][1] - net[1][1]) + abs(net[0][2] - net[1][2])
				cost += (manhattan_distance + 16)
			else:
				cost += (len(output_dict[net]) - 1)

		return cost


	def output(self, output_dict):
		""" Writes the nets and wires to a csv-file. """

		with open('data/test/output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
