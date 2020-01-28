from code.algorithms.astar import Astar
import random


class XYZ_astar():
	""" Redo unlaid wires from xyz_move result with A*. """

	def __init__(self, output_dict, unsolved_wire):
		
		self.output_dict = output_dict
		self.unsolved_wire = unsolved_wire

		self.stuck_point, self.stuck_wires = self.find_stuck_point()


	def find_stuck_point(self):
		""" Find the point where an attempted wire gets stuck in the grid. """

		stuck_point = {}
		stuck_wires = {}

		# wires of length 1 (-> [(0, 0, 0)]) were not laid
		LAID_WIRE_LENGTH = 2

		for net, wire in self.output_dict.items():
			if len(wire) < LAID_WIRE_LENGTH:

				wire = []

				for point in self.unsolved_wire[net]:
					# break if stuck-point is found, otherwhise add point to wire
					if net[1][0] == point[0] and net[1][1] == point[1] and (self.unsolved_wire[net].count(point) == 1) or point == self.unsolved_wire[net][-1]:
						stuck_wires[net] = wire
						stuck_point[net] = point
						break
 
					wire.append(point)

		return stuck_point, stuck_wires


	def change_wires(self, chip, output_dict, heuristic):
		""" Lays the remaining points of the wires that got stuck, with the use of A*. """

		new_output_dict = {}

		for net, point in self.stuck_point.items():

			new_netlist = [(point, net[1])]

			astar_instance = Astar(new_netlist, chip, heuristic)
			new_wires = astar_instance.execute_astar(False)

			# merge old part of wire with new part of wire if A* was succesfull
			if len(next(iter(new_wires.values()))) > 1:
				self.stuck_wires[net] += next(iter(new_wires.values()))
				new_output_dict[net] = self.stuck_wires[net]

		output_dict.update(new_output_dict)

		return output_dict
