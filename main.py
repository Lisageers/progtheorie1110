"""
main.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Connect gates on a grid.
"""

import sys
from code.classes import chip, netlist, wiring
from code.visualisation import matplot


if __name__ == '__main__':

	# let user choose a chip
	while True:
		req_chip = input("Which chip do you want to use? (1, 2, test)\n")
		if req_chip == '1':
			chip_path = 'data/chip_1/print_1.csv'
			req_chip = 'chip_1'
			break
		elif req_chip == '2':
			chip_path = 'data/chip_2/print_2.csv'
			req_chip = 'chip_2'
			break
		elif req_chip.lower() == 'test':
			chip_path = 'data/test/print.csv'
			req_chip = 'test'
			break
		else:
			print("That chip does not exist.")

	# create a Chip object for the chosen chip
	chip = chip.Chip(chip_path)

	# let user choose a netlist
	while True:
		req_netlist = input("Which netlist do you want to use? (1, 2, 3)\n")
		if req_netlist == '1' or req_netlist == '2' or req_netlist == '3':
			netlist_path = 'data/' + req_chip + f'/netlist_{req_netlist}.csv'
			break
		else:
			print("That is not an option.")

	# create a Netlist object for the chosen chip and netlist combination
	netlist = netlist.Netlist(netlist_path, chip.gates)

	# let user choose an algorithm
	while True:
		alg_req = input("Which algorithm would you like to use? (xyz_move, straight_first, random_netlist, straight_random)\n").lower()
		if alg_req == 'xyz_move' or alg_req == 'straight_first' or alg_req == 'random_netlist' or alg_req == 'straight_random':
			break
		else:
			print("This algorithm does not exist.")

	loopcount = 0
	while True:
		if loopcount > 100000:
			break
		loopcount += 1

		# generate a solution
		wires = wiring.Wiring(netlist, chip, alg_req)

		if wires.wire == None:
			print("This algorithm can not find a solution for this problem.")
			# sys.exit(1)
		else:
			# calculate cost of the solution
			cost = wires.cost(wires.wire)
			print(f"The cost of this solution is {cost}")
			# get the dimensions for the visual representation
			x_dim = chip.get_x_dimension(chip.gates)
			y_dim = chip.get_y_dimension(chip.gates)

			# create visual representation of the solved chip
			visualise = matplot.visualise(chip.gates, wires.wire, x_dim, y_dim)
			break

		print()
