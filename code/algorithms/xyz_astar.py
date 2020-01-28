from code.algorithms.astar import execute_astar
import random


def find_point_stuck(output_dict, unsolved_wire):
	""" Find the point where an attempted wire gets stuck in the grid. """

	stuck_point = {}
	stuck_wires = {}

	LAID_WIRE_LENGTH = 2

	for net, wire in output_dict.items():

		if len(wire) < LAID_WIRE_LENGTH:
			
			wire = []

			for point in unsolved_wire[net]:

				# break if stuck-point is found
				if net[1][0] == point[0] and net[1][1] == point[1] and (unsolved_wire[net].count(point) == 1) or point == unsolved_wire[net][-1]:
					stuck_wires[net] = wire
					stuck_point[net] = point
					break

				# otherwhise add point to wire
				wire.append(point)

	return stuck_point, stuck_wires


def change_wires(stuck_points, stuck_wires, chip, output_dict, heuristic):
	""" Lays the remaining points of the wires that got stuck, with the use of A*. """

	new_output_dict = {}

	for net, point in stuck_points.items():

		new_netlist = [(point, net[1])]

		new_wires = execute_astar(new_netlist, chip, heuristic, False)

		# merge old part of wire with new part of wire if A* was succesfull
		if len(next(iter(new_wires.values()))) > 1:
			stuck_wires[net] += next(iter(new_wires.values()))
			new_output_dict[net] = stuck_wires[net]

	output_dict.update(new_output_dict)

	return output_dict
