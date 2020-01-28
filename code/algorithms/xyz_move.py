from code.algorithms.xyz_astar import *
from code.algorithms.hillclimber_astar import HillClimber


class XYZ_algorithm():
	""" Lay wires by moving in the direction of the endgate in the order x-direction, y-direction, z-direction."""

	def __init__(self, netlist, chip):

		self.netlist = netlist
		self.chip = chip

		self.output_dict, self.unsolved_wire, optimisation = self.run_xyz()
		
		if optimisation == 'y' or optimisation == 'yes':
			self.output_dict = self.optimise_xyz(self.output_dict, self.unsolved_wire)


	def move_xyz(self, net):
		""" Determine wire needed to connect the nets. """
		
		wire = []
		wire.append(net[0])
		current = list(net[0])
		end = net[1]

		while True:
			# check whether current point and end point are adjacent, else move towards the end gate
			if abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2]) == 1:
				wire.append(net[1])
				return True, wire

			else:
				# move +x if x of end is larger and +x is open
				if (end[0] - current[0]) > 0 and self.chip.check_empty(((current[0] + 1), current[1], current[2]), self.chip.grid):
					current[0] += 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -x if x of end is smaller and -x is open
				elif ((end[0] - current[0]) < 0) and self.chip.check_empty(((current[0] - 1), current[1], current[2]), self.chip.grid):
					current[0] -= 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move +y if y of end is larger and +y is open
				elif ((end[1] - current[1]) > 0) and self.chip.check_empty((current[0], (current[1] + 1), current[2]), self.chip.grid):
					current[1] += 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -y if y of end is smaller and -y is open
				elif ((end[1] - current[1]) < 0) and self.chip.check_empty((current[0], (current[1] - 1), current[2]), self.chip.grid):
					current[1] -= 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -z if z of end is larger and -z is open
				elif ((end[2] - current[2]) < 0) and self.chip.check_empty((current[0], current[1], (current[2] - 1)), self.chip.grid):
					current[2] -= 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move +z if z of end is larger and +z is open, or quit if the top has been reached
				else:
					if current[2] + 1 == 8:
						return False, wire

					current[2] += 1
					self.chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))


	def run_xyz(self):
		""" Execute move_xyz for an entire netlist. """

		output_dict = {}
		unsolved_wire = {}

		for net in self.netlist:
			solved, solution = self.move_xyz(net)
			
			if solved == True:
				output_dict[net] = solution
			else:
				output_dict[net] = [(0, 0, 0)]
				unsolved_wire[net] = solution

		optimisation = input("Do you want to optimise the xyz_move result with A*? (y/n) \n").lower()

		return output_dict, unsolved_wire, optimisation


	def optimise_xyz(self, output_dict, unsolved_wire):
		""" Run optimisation on move_xyz result. """

		while True:
			heuristic = input("Which heuristic do you want to use? (manhattan_distance, distance_to_gate, loose_cables)\n").lower()
			if heuristic == 'manhattan_distance' or heuristic == 'distance_to_gate' or heuristic == 'loose_cables':
				break
			else:
				print("This is not an option.\n")

		# optimise result by redoing unlaid wires with A*
		xyz_optimisation = XYZ_astar(output_dict, unsolved_wire)
		new_wires = xyz_optimisation.change_wires(self.chip, output_dict, heuristic)

		optimisation = input("Do you want to optimise the result with hillclimber? (y/n)\n").lower()

		if optimisation == 'y' or optimisation == 'yes':
						
			output_dict = HillClimber(self.chip, new_wires, heuristic)
			new_wires = output_dict.run()

		return new_wires
