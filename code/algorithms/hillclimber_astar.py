from code.algorithms.astar import Astar
import copy
import random


class HillClimber():
	""" Tries to improve current solution, by taking a random wire and laying it again differently. """

	def __init__(self, chip, output_dict, heuristic):

		self.chip = chip
		self.heuristic = heuristic
		self.output_dict = copy.deepcopy(output_dict)


	def mutate_random_wire(self):
		""" Remove random wire and lay again by executing A*. """

		random_wire = random.choice(list(self.output_dict.keys()))

		for point in self.output_dict[random_wire]:
			self.chip.grid[point[0]][point[1]][point[2]] = False

		random_wire = [random_wire]
		astar_instance = Astar(random_wire, self.chip, self.heuristic)
		new_wire = astar_instance.execute_astar(False)

		return new_wire


	def lay_unlaid_wires(self):
		""" Try to lay unlaid wires in the new situation. """

		unlaid_netlist = []
		
		for net, wire in self.output_dict.items():
			if len(wire) == 1:
				unlaid_netlist.append(net)
		astar_instance = Astar(unlaid_netlist, self.chip, self.heuristic)
		new_unlaid_wires = astar_instance.execute_astar(False)

		return new_unlaid_wires


	def check_solution(self, new_wire):
		""" Check whether the new wire is shorter than previous versions. """

		old_cost = 0
		new_cost = 0

		if new_wire:
			net = next(iter(new_wire.keys()))

			old_cost = (len(self.output_dict[net]) - 1)

			new_cost = (len(new_wire[net]) - 1)

			if new_cost < old_cost and not new_cost == 0:
				self.output_dict.update(new_wire)
			else:
				for point in self.output_dict[net]:
					self.chip.grid[point[0]][point[1]][point[2]] = True


	def run(self):
		""" Executes hillclimb algorithm. """

		for wires in range(750):
			new_unlaid_wires = self.lay_unlaid_wires()
			self.check_solution(new_unlaid_wires)
			new_wire = self.mutate_random_wire()
			self.check_solution(new_wire)

		return self.output_dict
