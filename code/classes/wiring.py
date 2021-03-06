import csv
from code.algorithms.xyz_move import XYZ_algorithm
from code.algorithms.astar import Astar
from code.algorithms.hillclimber_astar import HillClimber


class Wiring():
	""" This class retutrns output in three parts: dictionary of laid wires, cost of the wires, csv-file of laid wires. """

	def __init__(self, netlist, chip, alg_req):
		
		self.chip = chip
		self.netlist = netlist

		algorithm, optimisation = self.choose_alg(alg_req)

		if algorithm == Astar:
			heuristic = self.choose_heuristic()
			astar_instance = algorithm(self.netlist, self.chip, heuristic)
			self.wire = astar_instance.execute_astar()
		else:
			xyz_instance = algorithm(self.netlist, self.chip)
			self.wire = xyz_instance.output_dict

		if optimisation == 'y' or optimisation == 'yes':
						
			output_dict = HillClimber(self.chip, self.wire, heuristic)
			self.wire = output_dict.run()

		self.output(self.wire)


	def choose_alg(self, alg_req):
		""" Get the algorithm the user chose. """

		if alg_req == 'xyz_move':
			algorithm = XYZ_algorithm
			optimisation_input = None
		elif alg_req == 'astar':
			algorithm = Astar
			optimisation_input = input("Do you want to optimise the result with hillclimber? (y/n)\n").lower()

		return algorithm, optimisation_input


	def choose_heuristic(self):
		""" Make user choose an heuristic. """

		while True:
			heuristic = input("Which heuristic do you want to use? (manhattan_distance, distance_to_gate, loose_cables)\n").lower()
			if heuristic == 'manhattan_distance' or heuristic == 'distance_to_gate' or heuristic == 'loose_cables':
				break
			else:
				print("This is not an option.\n")

		return heuristic


	def cost(self, output_dict):
		""" Calculate the cost of wires used in the solution plus a penalty for unlaid wire. """

		cost = 0

		for net in output_dict:
			# penalty for missing wire: assume an 8th layer was needed, so add 16 for going up and down plus manhattan distance
			if output_dict[net] == [(0, 0, 0)]:
				manhattan_distance = abs(net[0][0] - net[1][0]) + abs(net[0][1] - net[1][1]) + abs(net[0][2] - net[1][2])
				cost += (manhattan_distance + 16)
			else:
				cost += (len(output_dict[net]) - 1)

		return cost


	def output(self, output_dict):
		""" Write the nets and wires to a csv-file. """

		with open('results/output.csv', mode='w') as csv_output:
			fieldnames = ['net', 'wires']
			writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
			writer.writeheader()

			for net, wire in output_dict.items():
				writer.writerow({'net' : net, 'wires' : wire})
