from collections import defaultdict 

def get_neighbours(grid, node, end):
	""" Get neighbour nodes of current node """

	neighbours = defaultdict(list)

	# determine position of neighbour nodes
	for n in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
		neighbour = (node[0] + n[0], node[1] + n[1], node[2] + n[2])
		
		# make sure the next position is within the grid
		if neighbour[0] > (len(grid) -1) or neighbour[0] < 0 or neighbour[1] > (len(grid[0]) -1) or neighbour[1] < 0 or neighbour[2] > (len(grid[0][0]) -1) or neighbour[2] < 0:
			continue
		
		# make sure the next position is not already occupied
		if grid[neighbour[0]][neighbour[1]][neighbour[2]] != False and neighbour != end:
			continue

		neighbours[node].append(neighbour)

	return neighbours


def dfs(neighbours, start, end, visited, grid):
	""" Perform depth first search recursively until end node is reached """

	if start not in visited:
		visited.append(start)

		for node in neighbours[start]:
			if node == end:
				return visited
			dfs(get_neighbours(grid, node, end), node, end, visited, grid)
	return visited


def execute_dfs(net_cor, chip):
	""" Execute dfs function for all nets """

	grid = chip.grid
	output_dict = {}

	for net in net_cor:
		start = net[0]
		end = net[1]

		neighbours = get_neighbours(grid, start, end)
		path = dfs(neighbours, start, end, [], grid)
		
		for node in path:
			grid[node[0]][node[1]][node[2]] = True

		output_dict[net] = path
	print("output", output_dict)
	return output_dict


def iddfs(grid, node, end):
	for depth in range(grid):
		found = dls(node, end, depth, grid)
		if found is not None:
			return found

def dls(node, end, depth, grid):
	if depth == 0:
		if node == end:
			return node
		# not found, but may have children
		else:
			return None
	
	elif depth > 0:
		# any remaining = False

		neighbours = get_neighbours(grid, node, end)
		for node in neighbours:
			found = dls(node, end, depth-1, grid)
			if found is not None:
				return found