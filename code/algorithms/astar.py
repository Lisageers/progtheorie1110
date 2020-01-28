import copy
from heapq import heappush, heappop
from math import sqrt
from random import shuffle
from collections import Counter


class Astar():
	""" Determine shortest path between two gates on a grid. """

	def __init__(self, netlist, chip, heuristic):

		self.netlist = netlist
		self.chip = chip
		self.grid = self.chip.grid
		self.gates = self.chip.gates
		self.heuristic = heuristic
		self.occurance_gate = self.occurance_gates()


	def astar(self, start, end, netlist):
		""" A* for connecting gates on a grid. """

		Q = []
		visited_points = {}

		heappush(Q, (0, [start]))

		while len(Q) > 0:
			top_tuple = heappop(Q)
			current_path = top_tuple[1]

			if not current_path[-1] in visited_points:
				visited_points[current_path[-1]] = top_tuple[0]
			elif top_tuple[0] < visited_points[current_path[-1]]:
				visited_points[current_path[-1]] = top_tuple[0]

			neighbours = self.make_neighbours(current_path[len(current_path) - 2], current_path[-1], end)

			# determine heuristic (h), cost, f for neighbours and place in heapq accordingly
			for neighbour in neighbours:

				if self.heuristic == 'manhattan_distance':
					h = self.manhattan_distance(neighbour, end)
				elif self.heuristic == 'distance_to_gate':
					h = self.distance_to_gate(neighbour, start, end, netlist)
				elif self.heuristic == 'loose_cables':
					h = self.loose_cables(current_path[-1], neighbour, end, start, netlist)

				new_path = current_path + [neighbour]

				# lay the wire if the end has been found
				if neighbour == end:
					for point in new_path:
						self.grid[point[0]][point[1]][point[2]] = True

					return new_path

				f = h + len(new_path) - 1

				# only add neighbours to the queue when they are new or have a lower f
				if not neighbour in visited_points.keys():
					heappush(Q, (f, new_path))
					visited_points[neighbour] = f
				else:
					if visited_points[neighbour] > f:
						heappush(Q, (f, new_path))
						visited_points[neighbour] = f

		return [(0, 0, 0)]


	def make_neighbours(self, parent, current, end):
		""" Fill list with available neighbouring points. """

		neighbours = []

		for change_position in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:

			next_position = (current[0] + change_position[0], current[1] + change_position[1], current[2] + change_position[2] )

			# make sure the next position is within the grid
			if next_position[0] > (len(self.grid) -1) or next_position[0] < 0 or next_position[1] > (len(self.grid[0]) -1) or next_position[1] < 0 or next_position[2] > (len(self.grid[0][0]) -1) or next_position[2] < 0:
				continue

			# make sure the next position is not already occupied
			if self.grid[next_position[0]][next_position[1]][next_position[2]] != False and next_position != end:
				continue

			# parent cannot also be neighbour
			if next_position == parent:
				continue

			neighbours.append(next_position)

		return neighbours


	def execute_astar(self, first_execution=True):
		""" Execute astar function for all nets. """

		output_dict = {}

		if first_execution:
			# does user want loose_layering?
			layering_input = input("Do you want equal distribution of wires over the layers? (y/n)\n").lower()
			if layering_input == 'y' or layering_input == 'yes':
				loose_layering = True
			else:
				loose_layering = False
		else:
			loose_layering = False

		# loose_layering forces the wires through a predetermined layer
		if loose_layering == True:
			netlist = self.layer_netlist()

			for index, layer in enumerate(netlist):
				for net in layer:
					start = net[0]
					end = net[1]

					# for nets that are not direct neighbours create a between in a predetermined layer for equal distribution of wires
					if self.manhattan_distance(start, end) > 1:
						between = (int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2), 7 - index)
						position_changes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

						# if the between point is occupied, try again with a random neighbour in x or y direction
						if not self.chip.check_empty(between, self.grid):
							for position in position_changes:
								new_between = (between[0] + position[0], between[1] + position[1], between[2])
								if self.chip.check_empty(new_between, self.grid):
									between = new_between
									break

						path_1 = self.astar(start, between, netlist)
						path_2 = self.astar(between, end, netlist)

						# if half of the wire was not laid, remove the other half as well
						if path_1 == [(0, 0, 0)] or path_2 == [(0, 0, 0)]:
							remove_path = path_1 + path_2
							for point in remove_path:
								self.grid[point[0]][point[1]][point[2]] = False
							output_dict[net] = [(0, 0, 0)]
						else:
							output_dict[net] = path_1 + path_2

					else:
						path = self.astar(start, end, netlist)
						output_dict[net] = path

		else:
			# run astar for each net
			for net in self.netlist:
				start = net[0]
				end = net[1]
				path = self.astar(start, end, self.netlist)
				output_dict[net] = path

		return output_dict


	def occurance_gates(self):
		""" Determine how many connections each gate should have. """

		gates_in_netlist = []
		for net in self.netlist:
			gates_in_netlist.append(net[0])
			gates_in_netlist.append(net[1])

		# count how often a gate occurs and collect the data in a dictionary
		occurance_gate = Counter(gates_in_netlist)

		return occurance_gate


	def layer_netlist(self):
		""" Create a divided netlist for equal distribution of wires per layer. """

		# determine how many wires per layer for equal distribution
		rest_nets = len(self.netlist) % 7
		normal_divisible = len(self.netlist) - rest_nets
		cables_per_layer = int(normal_divisible / 7)
		cables_per_layer += 1

		# create a list of lists corresponding to which nets should go via which layer
		layer_list = []

		for x in range(7):
			if len(self.netlist) < cables_per_layer:
				netlist_copy = copy.deepcopy(self.netlist)
				layer_list.append(netlist_copy)
				del self.netlist[:len(self.netlist)]
			elif len(self.netlist) != 0:
				layer = self.netlist[:cables_per_layer]
				layer_list.append(layer)
				del self.netlist[:cables_per_layer]

		return layer_list


	def manhattan_distance(self, current, end):
		""" Determine the manhattan distance between two points. """

		distance = abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2])

		return distance


	def distance_to_gate(self, current, start, end, netlist):
		""" Protect points around gates that need to be accessible for multiple wires, by increasing their heuristic. """

		heuristic = self.manhattan_distance(current, end)

		PROTECTION_INCREASE = 50

		for gate in self.gates:
			if self.manhattan_distance(current, gate) == 1 and gate != start and gate != end and (self.occurance_gate[gate] > 1 or gate in netlist[-5:]):
				heuristic = self.manhattan_distance(current, end) + PROTECTION_INCREASE

		return heuristic


	def loose_cables(self, parent, current, end, start, netlist):
		""" Make looser cables cheaper, to generate suboptimal solutions that can be optimised itteratively. """

		# how happy does going in positive z-direction make the heuristic
		if current[2] > parent[2]:
			looseness = 10 - current[2]
		elif current[2] > 0:
			looseness = 2
		else:
			looseness = 1

		heuristic = 2 * (self.distance_to_gate(current, start, end, netlist) / looseness)

		return heuristic
