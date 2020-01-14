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

	def __init__(self, list_file, gates):
		self.netlist = self.netlist(list_file)
		self.net_cor = self.net_cor(self.netlist, gates)


	def netlist(self, list_file):
		""" Create list type netlist from csv file. """

		# get netlist from csv-file
		with open(list_file) as in_file:
			netlist_reader = csv.reader(in_file)
			next(netlist_reader)

			netlist = []

			# remove spaces
			for start, end in netlist_reader:
				netlist.append((start.strip(), end.strip()))

		return netlist


	def sort_list(self, netlist)
		""" Sort the netlist as required."""
		pass 


	def net_cor(self, netlist, gates):
		""" Create altered netlist with coordinates instead of names. """

		net_cor = []

		for net in netlist:
			for gate in gates:
				# get start cor of net
				if gates[gate] == net[0]:
					cor_start = gate

				# get end cor of net
				elif gates[gate] == net[1]:
					cor_end = gate

			# put cors in list
			net_cor.append((cor_start, cor_end))

		return net_cor
