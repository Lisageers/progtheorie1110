import csv
from random import shuffle
from collections import Counter


class Netlist():
	""" This class creates a netlist with a usable datastructure from csv. """

	def __init__(self, list_file, gates, req_sort):
		self.netlist = self.netlist(list_file, req_sort)
		self.net_coords = self.net_coords(self.netlist, gates, req_sort)


	def netlist(self, list_file, req_sort):
		""" Create list type netlist from csv file. """

		# get netlist from csv-file
		with open(list_file) as in_file:
			netlist_reader = csv.reader(in_file)
			next(netlist_reader)

			netlist = []
			netlist_gates = []

			# remove white-space
			for start, end in netlist_reader:
				netlist.append((start.strip(), end.strip()))
				netlist_gates.append(start.strip())
				netlist_gates.append(end.strip())

		# sort netlist as per user request
		if req_sort == 'random':
			sorted_netlist = self.sort_random(netlist)
		elif req_sort == 'most_common':
			sorted_netlist = self.sort_most_common(netlist, netlist_gates)
		else:
			sorted_netlist = netlist

		return sorted_netlist


	def net_coords(self, netlist, gates, req_sort):
		""" Create altered netlist with coordinates instead of names. """

		net_coords = []
		
		for net in netlist:
			for gate in gates:
				if gates[gate] == net[0]:
					start_coord = gate
				elif gates[gate] == net[1]:
					end_coord = gate

			net_coords.append((start_coord, end_coord))

		# sort netlist as per user request
		if req_sort == 'straight_first':
			sorted_net_coords = self.sort_straight_first(net_coords)
		elif req_sort == 'straight_random':
			sorted_net_coords = self.sort_straight_random(net_coords)
		elif req_sort == 'longest_first':
			sorted_net_coords = self.sort_longest_first(net_coords)
		else:
			sorted_net_coords = net_coords

		return sorted_net_coords


	def sort_random(self, netlist):
		""" Sort the netlist randomly. """

		shuffle(netlist)

		return netlist


	def sort_straight_first(self, netlist):
		""" Sort the netlist by straight lines first, the rest as in csv. """

		sorted_list = []

		for net in netlist:
			start = net[0]
			end = net[1]

			# set net at front of list when x's or y's of start and end are the same
			if (end[0] == start[0]) or (end[1] == start[1]):
				sorted_list.insert(0, net)

			else:
				sorted_list.append(net)

		return sorted_list


	def sort_straight_random(self, netlist):
		""" Sort the netlist by straight lines first, the rest random. """

		straight_list = []
		random_list = []

		for net in netlist:
			start = net[0]
			end = net[1]

			# set net at front of list when x's or y's of start and end are the same
			if (end[0] == start[0]) or (end[1] == start[1]):
				straight_list.insert(0, net)

			# otherwise add to list to be randomised
			else:
				random_list.append(net)

		shuffle(random_list)

		sorted_list = straight_list + random_list

		return sorted_list


	def sort_most_common(self, netlist, netlist_gates):
		""" Sort the netlist by amount of connections a gate has. """

		# count appearance of gates in the netlist
		count_dict = Counter(netlist_gates)

		sorted_netlist = []

		# itterate over list ordered by most common appearance
		for gate in count_dict.most_common():
			for net in netlist:
				if gate[0] in net and not net in sorted_netlist:
					if gate[0] != net[0]:
						switch = (net[1], net[0])
						sorted_netlist.append(switch)
						netlist.remove(net)
					else:
						sorted_netlist.append(net)

		return sorted_netlist


	def sort_longest_first(self, netlist):
		""" Sort the netlist by manhatten distance between start and end. """

		distance_list = []

		# determine manhattan distance between start and end
		for net in netlist:
			start = net[0]
			end = net[1]
			distance = abs(start[0] - end[0]) + abs(start[1] - end[1]) + abs(start[2] - end[2])
			distance_list.append((distance, net))

		# sort nets by manhattan distance (largest first)
		sorted_distance = sorted(distance_list, reverse=True)

		# create a list of nets without distance
		sorted_netlist = []

		for distance_net in sorted_distance:
			sorted_netlist.append(distance_net[1])

		return sorted_netlist
