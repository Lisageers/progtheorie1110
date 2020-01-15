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
			netlist_connections = []

			# remove spaces
			for start, end in netlist_reader:
				netlist.append((start.strip(), end.strip()))
				netlist_connections.append(start)
				netlist_connections.append(end)

		netlist = self.sort_list_connections(netlist, netlist_connections)

		return netlist


	def sort_list_straight(self, netlist):
		""" Sort the netlist by straight lines."""


	def sort_list_connections(self, netlist, netlist_connections):
		""" Sort the netlist by connections."""

		print("netlist", netlist)

		print("netlistsort ", netlist_connections)
		print("netlist", netlist)
		count_dict = Counter(netlist_connections)
		print("count_dict", count_dict)

		sorted_netlist = []
		print("mostcommon", next(iter(count_dict)))
		for net in netlist:
			if '4' in net:
				sorted_netlist.insert(0, net)
				print("hij gaat hierin")
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
