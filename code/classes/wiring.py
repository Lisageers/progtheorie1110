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
from code.algorithms.iddfs import execute_dfs
from code.algorithms.hillclimb import *

class Wiring():
	""" This class outputs wires to connect gates as listed in netlist. """

	def __init__(self, netlist, chip, alg_req, loose_layering):
		self.chip = chip
		self.netlist = netlist
		
		algorithm = self.choose_alg(alg_req)
		
		if alg_req == 'xyz_move':
			self.wire, self.unsolved = algorithm(self.netlist, self.chip)
			self.stuck, self.stuck_wires = find_point_stuck(self.wire, self.unsolved)
			self.new_wires = change_wires(self.stuck, self.stuck_wires, self.chip, self.wire)
		else:
			self.wire = algorithm(self.netlist, self.chip, loose_layering)

		self.output(self.wire)


	def choose_alg(self, alg_req):
		""" Get the algorithm the user chose. """

		if alg_req == 'xyz_move':
			algorithm = xyz_wire
		elif alg_req == 'astar':
			algorithm = execute_astar
		elif alg_req == 'dfs':
			algorithm = execute_dfs

		return algorithm


	def cost(self, output_dict):
		""" Calculate the cost of wire used in the solution. """

		cost = 0

		for net in output_dict:
			cost += (len(output_dict[net]) - 1)

		return cost


	def output(self, output_dict):
		""" Writes the nets and wires to a csv-file. """

		with open('data/test/output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			# write wires and nets from dictionary
			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
