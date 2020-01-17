from queue import PriorityQueue

def heuristic(current, end):

	heuristic = abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2])

	return heuristic

def distance_to_gate(gates, current, start, end):
	print(gates)
	for gate in gates:
		if heuristic(current, gate) == 1 and current != start and current != end:
			h = heuristic(current, end) + 10
		else:
			h = heuristic(current, end)

	return h

def make_neighbours(grid, current, end):
	""" Fill list with available neighbouring points. """
	
	neighbours = []
	
	for new_position in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:

		next_position = (current[0] + new_position[0], current[1] + new_position[1], current[2] + new_position[2] )

		# make sure the next position is within the grid
		if next_position[0] > (len(grid) -1) or next_position[0] < 0 or next_position[1] > (len(grid[0]) -1) or next_position[1] < 0 or next_position[2] > (len(grid[0][0]) -1) or next_position[2] < 0:
			continue

		# make sure the next position is not already occupied
		if grid[next_position[0]][next_position[1]][next_position[2]] != False and next_position != end:
			continue

		neighbours.append(next_position)

	return neighbours


def astar(gates, grid, start, end):
	""" A* """
	
	Q = PriorityQueue()

	Q.put((None, [start]))

	while not Q.empty():
		prio, current_path = Q.get()

		neighbours = make_neighbours(grid, current_path[-1], end)

		if not neighbours:
			return [(0, 0, 0)]

		for neighbour in neighbours:
			h = distance_to_gate(gates, neighbour, start, end)

			new_path = current_path + [neighbour]

			if neighbour == end:
				for point in new_path:
					grid[point[0]][point[1]][point[2]] = True

				return new_path

			Q.put(h + len(new_path) - 1, new_path)


def execute_astar(netlist, chip):
	""" Execute astar function for all nets. """

	grid = chip.grid
	gates = chip.gates
	output_dict = {}
	count = 0

	for net in netlist:
		start = net[0]
		end = net[1]
		path = astar(gates, grid, start, end)
		count += 1
		print(path)
		print(count)
		output_dict[net] = path

	return output_dict