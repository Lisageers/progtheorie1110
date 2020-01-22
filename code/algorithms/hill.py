import copy
import random

class HillClimber():
	def __init__(self, grid, netlist):
		if not grid.is_solution():
			raise Exception("HillClimber requires a complete solution.")

		self.grid = copy.deepcopy(grid)
		

		self.netlist = netlist
	