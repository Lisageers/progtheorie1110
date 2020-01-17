"""
wiring.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Uses an algorithm to generate an output file with the solution for wiring.
"""

import csv

from code.algorithms.xyz_move import xyz_wire
from code.algorithms.straight_first import straight_wire 
from code.algorithms.random_netlist import random_wire 
from code.algorithms.new_astar import execute_astar
from code.algorithms.straight_random import straight_random_wire
from code.algorithms.iddfs import execute_dfs

class Wiring():
	""" This class outputs wires to connect gates as listed in netlist. """

	def __init__(self, netlist, chip, alg_req):
		self.chip = chip
		self.net_cor = netlist.net_cor
		algorithm = self.choose_alg(alg_req)
		self.wire = algorithm(self.net_cor, self.chip)

		if not self.wire == None:
			self.output(self.wire)


	def choose_alg(self, alg_req):
		""" Get the algorithm the user chose. """

		if alg_req == 'xyz_move':
			algorithm = xyz_wire
		elif alg_req == 'straight_first':
			algorithm = straight_wire
		elif alg_req == 'random_netlist':
			algorithm = random_wire
		elif alg_req == 'straight_random':
			algorithm = straight_random_wire
		elif alg_req == 'astar':
			algorithm = execute_astar
		elif alg_req == 'dfs':
			algorithm = execute_dfs

		return algorithm


	def cost(self, output_dict):
		""" Calculate the cost of wire used in the solution. """

		cost = 0

		for net in output_dict:
			if not output_dict[net] == ["emma", "marte"]:
				cost += (len(output_dict[net]) - 1)

		return cost


	def output(self, output_dict):
		""" Writes the nets and wires to a csv-file. """

		# write to csv
		with open('data/test/output.csv', mode='w') as csv_output:
			# write header
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			# write wires and nets
			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
