"""
main.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Connect gates on a grid.
"""

from code.classes import chip, netlist, wiring
from code.visualisation import matplot


if __name__ == '__main__':

	# let user choose a chip
	while True:
		req_chip = input("Which chip do you want to use? (1, 2)\n")
		if req_chip == '1':
			chip_path = 'data/chip_1/print_1.csv'
			req_chip = 'chip_1'
			break
		elif req_chip == '2':
			chip_path = 'data/chip_2/print_2.csv'
			req_chip = 'chip_2'
			break
		else:
			print("That chip does not exist.\n")

	# create a Chip object for the chosen chip
	chip = chip.Chip(chip_path)

	# let user choose a netlist
	while True:
		req_netlist = input("Which netlist do you want to use? (1, 2, 3)\n")
		if req_netlist == '1' or req_netlist == '2' or req_netlist == '3':
			netlist_path = 'data/' + req_chip + f'/netlist_{req_netlist}.csv'
			break
		else:
			print("That is not an option.\n")

	# let user choose a method for sorting the netlist
	while True:
		req_sort = input("How do you want to sort the netlist? (random, straight_first, straight_random, most_common, longest_first)\n")
		if req_sort == 'random' or req_sort == 'straight_first' or req_sort == 'straight_random' or req_sort == 'most_common' or req_sort == 'longest_first':
			break
		else:
			print("That is not an option.\n")

	# let user choose an algorithm
	while True:
		alg_req = input("Which algorithm would you like to use? (xyz_move, astar)\n").lower()
		if alg_req == 'xyz_move' or alg_req == 'astar':
			break
		else:
			print("This algorithm does not exist.\n")

	# create a Netlist object for the chosen chip and netlist combination
	netlist = netlist.Netlist(netlist_path, chip.gates, req_sort)

	# generate a dictionary containing the solution (wire) for each net
	wires = wiring.Wiring(netlist.net_coords, chip, alg_req)

	# calculate cost of the solution
	cost = wires.cost(wires.wire)
	print(f"The cost of this solution is {cost}\n")

	count = 0
	for wire in wires.wire.values():
		if len(wire) != 1:
			count +=1

	print(f"The algorithm laid {count} wires out of {len(netlist.netlist)}.\n")

	# get the dimensions of the grid for the visual representation
	x_dim = chip.get_x_dimension(chip.gates)
	y_dim = chip.get_y_dimension(chip.gates)

	# # create visual representation of the solved chip
	# visualise = matplot.visualise(chip.gates, wires.wire, x_dim, y_dim)
