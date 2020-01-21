from code.algorithms.xyz_move import xyz_wire
from code.algorithms.astar import execute_astar
import random

def find_point_stuck(output_dict, unsolved_wire):
	""" Find the point where the wire gets stuck in the grid. """

	stuck_point = {}
	stuck_wires = {}

	for net, wire in output_dict.items():
		# check if no wire
		if len(wire) < 2:
			# initialise wire
			wire = []

			# look in unsolved wire
			for point in unsolved_wire[net]:

				# find the point where wire gets stuck
				if net[1][0] == point[0] and net[1][1] == point[1] and (unsolved_wire[net].count(point) == 1) or point == unsolved_wire[net][-1]:
					#put wire and point in dictionary
					stuck_wires[net] = wire
					stuck_point[net] = point
					break

				# add point to list if stuck-point is not found
				wire.append(point)

	return stuck_point, stuck_wires

def change_wires(stuck_points, stuck_wires, chip, output_dict):
	""" Lays the remaining points of the wires that got stuck with the use of A*. """

	new_output_dict = {}



	for net, point in stuck_points.items():
		# make new netlist
		new_netlist = [(point, net[1])]

		# execute astar
		new_wires = execute_astar(new_netlist, chip, 'nosort')

		# merge wires if new found
		if len(next(iter(new_wires.values()))) > 1:
			stuck_wires[net] += next(iter(new_wires.values()))
			new_output_dict[net] = stuck_wires[net]

	# update the output with new wires
	output_dict.update(new_output_dict)

	return output_dict
