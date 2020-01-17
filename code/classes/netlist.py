"""
netlist.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Reads a netlist from csv input and write a coordinate list from it.
"""

import csv
from collections import Counter

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
			netlist_gates = []

			# remove spaces
			for start, end in netlist_reader:
				netlist.append((start.strip(), end.strip()))
				netlist_gates.append(start.strip())
				netlist_gates.append(end.strip())

		return netlist


	def sort_list_straight(self, netlist):
		""" Sort the netlist by straight lines."""
		pass


	def sort_gates(self, netlist, netlist_gates):
		""" Sort the netlist by connections."""
		
		count_dict = Counter(netlist_gates)

		sorted_netlist = []

		for gate in count_dict.most_common():
			for net in netlist:
				if gate[0] in net and not net in sorted_netlist:
					if gate[0] != net[0]:
						switch = (net[1], net[0])
						sorted_netlist.append(switch)
						netlist.remove(net)
					else:
						sorted_netlist.append(net)


		print("newnetlist", sorted_netlist)
		return sorted_netlist


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
