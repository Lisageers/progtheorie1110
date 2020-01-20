from code.algorithms.xyz_move import xyz_wire

def find_point_stuck(output_dict, unsolved_wire):
	""" Find the point where the wire gets stuck in the grid. """

	stuck_dict = {}
	for net, wire in output_dict.items():
		# check if no wire
		if len(wire) < 2:

			# look in wire
			for point in unsolved_wire[net]:
				# find the point where wire gets stuck
				if net[1][0] == point[0] and net[1][1] == point[1] and (unsolved_wire[net].count(point) == 1):
					stuck_dict[net] = point
					break

	return stuck_dict


def find_blocking_wire(output_dict, stuck_dict):
	""" Find the wires that block other wires. """

	block_dict = {}
	for point in stuck_dict.values():
		for net, wire in output_dict.items():

			# check if wire is below point
			if (point[0], point[1], (point[2] - 1)) in wire:
				block_dict[net] = wire

	return block_dict

def change_wires(stuck_dict, block_dict, chip, output_dict):
	""" Changes the wires that block other wires. """

	block_netlist = []
	stuck_netlist = []

	# remove blocked wires
	for net, wire in block_dict.items():
		block_netlist.append(net)
		for point in wire:
			chip.grid[point[0]][point[1]][point[2]] = False

	# lay stuck wires
	for net, point in stuck_dict.items():
		stuck_netlist.append(net)

		for z in range(int(point[2]) + 1):
			chip.grid[point[0]][point[1]][point[2] - z] = True


	block_wires = xyz_wire(block_netlist, chip)

	# make sure stuck wires can be laid
	for net, point in stuck_dict.items():
		stuck_netlist.append(net)
		for z in range(int(point[2]) + 1):
			chip.grid[point[0]][point[1]][point[2] - z] = False

	stuck_wires = xyz_wire(stuck_netlist, chip)

	print("output_dict", output_dict)
	print("stuck_wires", dict(stuck_wires))
	print("block_wires", dict(block_wires))
	output_dict.update(block_wires)
	output_dict.update(stuck_wires)


	return output_dict
