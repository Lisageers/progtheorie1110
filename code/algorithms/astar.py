from math import sqrt
from heapq import heappush, heappop

class Node():
	"""A coordination class for A* Pathfinding"""

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		# cost 
		self.cost = 0
		# heuristiek
		self.heur = 0
		# sum
		self.sum = 0

	def __lt__(self, other):
		return self.sum < other.sum

	def __eq__(self, other):
		return self.sum == other.sum

def astar(grid, start, end):
	"""Returns a list of tuples as a path from the start gate and end gate""" 

	# create start and end gate
	start_gate = Node(None, start)
	start_gate.cost = 0
	start_gate.heur = start_gate.sum = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
	end_gate = Node(None, end)
	end_gate.cost = end_gate.heur = end_gate.sum = 0 
	
	# make priority queue of nodes to expand
	queue = []
	expanded = set()

	heappush(queue, (start_gate.sum, start_gate))

	# loop while end_gate not found
	while len(queue) > 0:
		current_node = heappop(queue)[1]
		expanded.add(current_node.position)

		# check if end gate has been reached
		if current_node.position == end_gate.position:
			path = []
			current = current_node
			while current is not None:
				path.append(current.position)
				current = current.parent
			
			for node in path:
				grid[node[0]][node[1]][node[2]] = True

			return path[::-1]
		
		# generate children, adjacent nodes
		children = []
		for new_position in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:

			next_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2] )

			# make sure the next position is within the grid
			if next_position[0] > (len(grid) -1) or next_position[0] < 0 or next_position[1] > (len(grid[len(grid)-1]) -1) or next_position[1] < 0 or next_position[2] > (len(grid[len(grid[len(grid)-1])-1]) -1) or next_position[2] < 0:
				continue
			
			# make sure the next position is not already occupied
			if grid[next_position[0]][next_position[1]][next_position[2]] != False and next_position != end_gate.position:
				continue
			
			next_node = Node(current_node, next_position)

			children.append(next_node)

		for child in children:
			# check if child-position had already been expanded
			if not child.position in expanded:
			
				child.cost = current_node.cost + 1
				
				# use Pythagoras to calculate the heuristic (as the crow flies)
				child.heur = sqrt((end[0] - child.position[0]) ** 2 + (end[1] - child.position[1]) ** 2 + (end[2] - child.position[2]) ** 2)
				child.sum = child.cost + child.heur

				heappush(queue, (child.sum, child))
						

def execute_astar(net_cor, chip):
	"""Executes astar function for all nets""" 
	
	grid = chip.grid
	output_dict = {}

	for net in net_cor:
		start = net[0]
		end = net[1]
		path = astar(grid, start, end)
		print(path)
		output_dict[net] = path

	return output_dict