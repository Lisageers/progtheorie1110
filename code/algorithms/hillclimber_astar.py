from code.algorithms.astar import execute_astar
import copy
import random


class HillClimber():
	""" Tries to improve A*-output, by taking a random wire and laying it again differently. """

	def __init__(self, chip, output_dict):

		self.output_dict = copy.deepcopy(output_dict)
		self.run_hillclimber = self.run(chip)


	def mutate_random_wire(self, chip):
		""" Remove random wire and lay again by executing A*. """

		random_wire = random.choice(list(self.output_dict.keys()))

		for point in self.output_dict[random_wire]:
			chip.grid[point[0]][point[1]][point[2]] = False

		random_wire = [random_wire]
		new_wire = execute_astar(random_wire, chip, False)

		return new_wire

	def lay_unlaid_wires(self, chip):
		""" Try to lay unlaid wires in the new situation. """

		unlaid_netlist = []
		
		for net, wire in self.output_dict.items():
			if len(wire) == 1:
				unlaid_netlist.append(net)
		new_unlaid_wires = execute_astar(unlaid_netlist, chip, False)

		return new_unlaid_wires


	def check_solution(self, chip, new_wire):
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
					chip.grid[point[0]][point[1]][point[2]] = True


	def run(self, chip):
		""" Executes hillclimb algorithm. """

		for wires in range(750):
			new_unlaid_wires = self.lay_unlaid_wires(chip)
			self.check_solution(chip, new_unlaid_wires)
			new_wire = self.mutate_random_wire(chip)
			self.check_solution(chip, new_wire)

		return self.output_dict
