from heapq import heappush, heappop
from math import sqrt

def manhattan_distance(current, end):

	heuristic = abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2])

	return heuristic

def distance_to_gate(gates, current, start, end):

	heuristic = manhattan_distance(current, end)

	for gate in gates:
		if manhattan_distance(current, gate) == 1 and gate != start and gate != end:
			heuristic = manhattan_distance(current, end) + 50

	return heuristic


# def pythagoras(current, end):
# 	""" Determine the distance as the bird flies between two coordinates. """

# 	distance  = sqrt((end[0] - current[0]) ** 2 + (end[1] - current[1]) ** 2 + (end[2] - current[2]) ** 2)

# 	return distance



def loose_cables(parent, current, end):
	""" Make looser cables cheaper, to generate suboptimal solutions that can be optimised itteratively. """

	# how happy does going in positive z-direction make the heuristic
	if current[2] > parent[2]:
		looseness = 10 - current[2]
	elif current[2] > 0:
		looseness = 2
	else:
		looseness = 1

	heuristic = manhattan_distance(current, end) / looseness - (2 * current[2] + looseness)

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

		if next_position == parent:
			continue

		neighbours.append(next_position)

	return neighbours


def astar(gates, grid, start, end, index=None):
	""" A* """

	Q = []

	heappush(Q, (None, [start]))

	while len(Q) > 0:
		current_path = heappop(Q)[1]

		neighbours = make_neighbours(grid, current_path[len(current_path) - 2], current_path[-1], end)

		if not neighbours:
			return [(0, 0, 0)]

		for neighbour in neighbours:
			# h = manhattan_distance(neighbour, end) 
			h = distance_to_gate(gates, neighbour, start, end)
			# loose_cables(current_path[-1], neighbour, end)

			new_path = current_path + [neighbour]

			if neighbour == end:
				for point in new_path:
					grid[point[0]][point[1]][point[2]] = True

				return new_path

			f = h + len(new_path) - 1
			heappush(Q, (f, new_path))


def execute_astar(netlist, chip, req_sort):
	""" Execute astar function for all nets. """
	
	grid = chip.grid
	gates = chip.gates
	output_dict = {}
	count = 0

	if req_sort == 'loose_layering':
		for index, layer in enumerate(netlist):
			for net in layer:
				start = net[0]
				end = net[1]
				# between = (end[0], end[1], 7 - index)
				between = (int((start[0] + end[0]) / 2), int((start[1] + end[1]) / 2), 7 - index)
				# print("START", start)
				print("BETWEEN", between)
				# print("END", end)
				path_1 = astar(gates, grid, start, between, index)
				print("PATH_1", path_1)
				path_2 = astar(gates, grid, between, end, index)
				print("PATH_2", path_2)
				output_dict[net] = path_1 + path_2

	else:
		for net in netlist:
			start = net[0]
			end = net[1]
			path = astar(gates, grid, start, end)
			count += 1
			print(path)
			print(count)
			output_dict[net] = path

	return output_dict
