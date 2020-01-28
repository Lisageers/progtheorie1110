import copy
from heapq import heappush, heappop
from math import sqrt
from random import shuffle
from collections import Counter


def layer_netlist(netlist):
	""" Create a divided netlist for equal distribution of wires per layer. """

	# determine how many wires per layer for equal distribution
	rest_nets = len(netlist) % 7
	normal_divisible = len(netlist) - rest_nets
	cables_per_layer = int(normal_divisible / 7)
	cables_per_layer += 1

	# create a list of lists corresponding to which nets should go via which layer
	layer_list = []

	for x in range(7):
		if len(netlist) < cables_per_layer:
			netlist_copy = copy.deepcopy(netlist)
			layer_list.append(netlist_copy)
			del netlist[:len(netlist)]
		elif len(netlist) != 0:
			layer = netlist[:cables_per_layer]
			layer_list.append(layer)
			del netlist[:cables_per_layer]

	return layer_list


def manhattan_distance(current, end):
	""" Determine the manhattan distance between two points. """

	distance = abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2])

	return distance


def distance_to_gate(gates, current, start, end, occurance_gate, sorted_netlist):
	""" Protect points around gates that need to be accessible for multiple wires, by increasing their heuristic. """

	heuristic = manhattan_distance(current, end)

	PROTECTION_INCREASE = 50

	for gate in gates:
		if manhattan_distance(current, gate) == 1 and gate != start and gate != end and (occurance_gate[gate] > 1 or gate in sorted_netlist[-5:]):
			heuristic = manhattan_distance(current, end) + PROTECTION_INCREASE

	return heuristic


def loose_cables(parent, current, end, gates, start, occurance_gate, netlist):
	""" Make looser cables cheaper, to generate suboptimal solutions that can be optimised itteratively. """

	# how happy does going in positive z-direction make the heuristic
	if current[2] > parent[2]:
		looseness = 10 - current[2]
	elif current[2] > 0:
		looseness = 2
	else:
		looseness = 1

	heuristic = 2 * (distance_to_gate(gates, current, start, end, occurance_gate, netlist) / looseness)

	return heuristic


def make_neighbours(grid, parent, current, end):
	""" Fill list with available neighbouring points. """

	neighbours = []

	for change_position in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:

		next_position = (current[0] + change_position[0], current[1] + change_position[1], current[2] + change_position[2] )

		# make sure the next position is within the grid
		if next_position[0] > (len(grid) -1) or next_position[0] < 0 or next_position[1] > (len(grid[0]) -1) or next_position[1] < 0 or next_position[2] > (len(grid[0][0]) -1) or next_position[2] < 0:
			continue

		# make sure the next position is not already occupied
		if grid[next_position[0]][next_position[1]][next_position[2]] != False and next_position != end:
			continue

		# parent cannot also be neighbour
		if next_position == parent:
			continue

		neighbours.append(next_position)

	return neighbours


def astar(gates, grid, start, end, occurance_gate, netlist, heuristic):
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

		neighbours = make_neighbours(grid, current_path[len(current_path) - 2], current_path[-1], end)

		# determine heuristic (h), cost, f for neighbours and place in heapq accordingly
		for neighbour in neighbours:

			if heuristic == 'manhattan_distance':
				h = manhattan_distance(neighbour, end)
			elif heuristic == 'distance_to_gate':
				h = distance_to_gate(gates, neighbour, start, end, occurance_gate, netlist)
			elif heuristic == 'loose_cables':
				h = loose_cables(current_path[-1], neighbour, end, gates, start, occurance_gate, netlist)

			new_path = current_path + [neighbour]

			# lay the wire if the end has been found
			if neighbour == end:
				for point in new_path:
					grid[point[0]][point[1]][point[2]] = True

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


def execute_astar(netlist, chip, heuristic, first_execution=True):
	""" Execute astar function for all nets. """

	grid = chip.grid
	gates = chip.gates
	output_dict = {}

	# determine how many connections each gate should have
	gates_in_netlist = []
	for net in netlist:
		gates_in_netlist.append(net[0])
		gates_in_netlist.append(net[1])

	occurance_gate = Counter(gates_in_netlist)

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
		netlist = layer_netlist(netlist)

		for index, layer in enumerate(netlist):
			for net in layer:
				start = net[0]
				end = net[1]

				# for nets that are not direct neighbours create a between in a predetermined layer for equal distribution of wires
				if manhattan_distance(start, end) > 1:
					between = (int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2), 7 - index)
					position_changes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]

					# if the between point is occupied, try again with a random neighbour in x or y direction
					if not chip.check_empty(between, grid):
						for position in position_changes:
							new_between = (between[0] + position[0], between[1] + position[1], between[2])
							if chip.check_empty(new_between, grid):
								between = new_between
								break

					path_1 = astar(gates, grid, start, between, occurance_gate, netlist, heuristic)
					path_2 = astar(gates, grid, between, end, occurance_gate, netlist, heuristic)

					# if half of the wire was not laid, remove the other half as well
					if path_1 == [(0, 0, 0)] or path_2 == [(0, 0, 0)]:
						remove_path = path_1 + path_2
						for point in remove_path:
							grid[point[0]][point[1]][point[2]] = False
						output_dict[net] = [(0, 0, 0)]
					else:
						output_dict[net] = path_1 + path_2

				else:
					path = astar(gates, grid, start, end, occurance_gate, netlist, heuristic)
					output_dict[net] = path

	else:
		# run astar for each net
		for net in netlist:
			start = net[0]
			end = net[1]
			path = astar(gates, grid, start, end, occurance_gate, netlist, heuristic)
			output_dict[net] = path

	return output_dict
