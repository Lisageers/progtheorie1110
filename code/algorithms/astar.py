import math
from math import sqrt

class Cor():
	"""A coordination class for A* Pathfinding"""

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		# cost 
		self.c = 0
		# heuristiek
		self.h = 0
		# sum
		self.f = 0


def astar(grid, start, end):
	"""Returns a list of tuples as a path from the start gate and end gate""" 

	# create start and end gate
	start_gate = Cor(None, start)
	start_gate.c = 0
	start_gate.h = start_gate.f = sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
	end_gate = Cor(None, end)
	end_gate.c = end_gate.h = end_gate.f = 0 
	
	# initialize lists and add start cor
	queue = []
	closed_list = []

	queue.append(start_gate)

	# loop while end_gate not found
	while len(queue) > 0:
		# sort by f and get cor with smallest f
		current_cor = queue[0]
		current_index = 0
		for index, item in enumerate(queue):
			if item.f < current_cor.f:
				current_cor = item
				current_index = index
						
		# remove current cor from queue
		queue.pop(current_index)
		closed_list.append(current_cor)

		# found end gate
		if current_cor.position == end_gate.position:
			path = []
			current = current_cor
			while current is not None:
				path.append(current.position)
				current = current.parent
			
			for cor in path:
				grid[cor[0]][cor[1]][cor[2]] = True
			return path[::-1]
		
		# generate children, adjacent cors
		children = []
		for new_position in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
			# get cor of new position
			cor_position = (current_cor.position[0] + new_position[0], current_cor.position[1] + new_position[1], current_cor.position[2] + new_position[2] )

			# make sure the cor is within range grid
			if cor_position[0] > (len(grid) -1) or cor_position[0] < 0 or cor_position[1] > (len(grid[len(grid)-1]) -1) or cor_position[1] < 0 or cor_position[2] > (len(grid[len(grid[len(grid)-1])-1]) -1) or cor_position[2] < 0:
				continue
			
			# make sure cor is not already occupied
			if grid[cor_position[0]][cor_position[1]][cor_position[2]] != False and cor_position != end_gate.position:
				continue
			
			new_cor = Cor(current_cor, cor_position)

			children.append(new_cor)

			for child in children:
				# check if child is on the closed_list
				if not child in closed_list:
				
					# set c, h, and f values
					child.c = current_cor.c + 1
					
					# use Pythagoras twice to calculate the heuristic (as the crow flies)
					child.h = sqrt(sqrt((end[0] - child.position[0]) ** 2 + (end[1] - child.position[1]) ** 2) ** 2 + (end[2] - child.position[2]) ** 2)
					child.f = child.c + child.h

					# check if child already in queue and 
					if not child in queue:
						queue.append(child)
					
					else:
						for cor in queue:
							if child == cor and child.f < cor.f:
								queue.append(child)
						

def execute_astar(net_cor, chip):
	"""Executes astar function for all nets""" 
	
	grid = chip.grid
	output_dict = {}

	for net in net_cor:
		start = net[0]
		end = net[1]
		path = astar(grid, start, end)
		output_dict[net] = path

	return output_dict