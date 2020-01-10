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
