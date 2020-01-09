"""
netlist.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Reads a netlist from csv input and write a coordinate list from it.
"""

import csv

class Netlist():
	""" This class creates a usable netlist. """

	def __init__(self, filename, gates):
		self.netlist = self.netlist(filename)
		self.net_cor = self.net_cor(self.netlist, gates)

	def netlist(self, filename):
		""" Create list type netlist from csv file. """

		with open(f'data/test/{filename}') as in_file:
			netlist_reader = csv.reader(in_file)
			next(netlist_reader)

			netlist = []

			for start, end in netlist_reader:
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
