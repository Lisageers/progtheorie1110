"""
wiring.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Uses an algorithm to generate an output file with the solution for wiring.
"""

import csv
from code.algoritmes import random_netlist as algorithm

class Wiring():
	""" This class outputs wires to connect gates as listed in netlist. """

	def __init__(self, netlist, chip):
		self.chip = chip
		self.net_cor = netlist.net_cor
		self.wire = algorithm.wire(self.net_cor, self.chip)
		self.output(self.wire)


	def output(self, output_dict):
		""" Write the output dictionary to a csv file. """
		
		with open('data/test/output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
