
from code.algorithms.xyz_astar import *

def xyz_wire(netlist, chip):
	""" Determine wire needed to connect the nets. """

	output_dict = {}
	unsolved_wire = {}
	unsolved_count = 0

	for net in netlist:
		wire = []
		wire.append(net[0])

		current = list(net[0])
		end = net[1]

		while True:
			# check whether current point and end point are adjacent
			if abs(current[0] - end[0]) + abs(current[1] - end[1]) + abs(current[2] - end[2]) == 1:
				wire.append(net[1])
				output_dict[net] = wire
				break

			# move towards the end-gate
			else:
				# move +x if x of end is larger and +x is open
				if (end[0] - current[0]) > 0 and chip.check_empty(((current[0] + 1), current[1], current[2]), chip.grid):
					current[0] += 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -x if x of end is smaller and -x is open
				elif ((end[0] - current[0]) < 0) and chip.check_empty(((current[0] - 1), current[1], current[2]), chip.grid):
					current[0] -= 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move +y if y of end is larger and +y is open
				elif ((end[1] - current[1]) > 0) and chip.check_empty((current[0], (current[1] + 1), current[2]), chip.grid):
					current[1] += 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -y if y of end is smaller and -y is open
				elif ((end[1] - current[1]) < 0) and chip.check_empty((current[0], (current[1] - 1), current[2]), chip.grid):
					current[1] -= 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move -z if z of end is larger and -z is open
				elif ((end[2] - current[2]) < 0) and chip.check_empty((current[0], current[1], (current[2] - 1)), chip.grid):
					current[2] -= 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

				# move +z if z of end is larger and +z is open
				else:
					if current[2] + 1 == 8:
						unsolved_count += 1
						output_dict[net] = [(0, 0, 0)]
						unsolved_wire[net] = wire
						break
					current[2] += 1
					chip.grid[current[0]][current[1]][current[2]] = True
					wire.append(tuple(current))

	optimisation_input = input("Do you want to optimise the xyz_move result with A*? (y/n) \n").lower()

	if optimisation_input == 'y' or optimisation_input == 'yes':
		stuck, stuck_wires = find_point_stuck(output_dict, unsolved_wire)
		new_wires = change_wires(stuck, stuck_wires, chip, output_dict)
		return new_wires

	return output_dict
