import copy
import random

from code.algorithms.astar import execute_astar


class HillClimber():
	def __init__(self, chip, output_dict):
		
		self.output_dict = copy.deepcopy(output_dict)
		self.run_hill = self.run(chip)
	

	def mutate_random_wire(self, chip):
		random_wire = random.choice(list(self.output_dict.keys()))
		for point in self.output_dict[random_wire]:
			chip.grid[point[0]][point[1]][point[2]] = False
		random_wire = [random_wire]
		new_wire = execute_astar(random_wire, chip, False)

		return new_wire


	def check_solution(self, chip, new_wire):
		old_cost = 0
		new_cost = 0

		net = next(iter(new_wire.keys()))

		old_cost = (len(self.output_dict[net]) - 1)

		new_cost = (len(new_wire[net]) - 1)

		if new_cost < old_cost and not new_cost == 0:
			self.output_dict.update(new_wire)
			print("Hij is verbetert")
		else:
			for point in self.output_dict[net]:
				chip.grid[point[0]][point[1]][point[2]] = True

	
	def run(self, chip):
		for wires in range(750):
			new_wire = self.mutate_random_wire(chip)
			self.check_solution(chip, new_wire)
		
		return self.output_dict