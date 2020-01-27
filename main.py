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
			print("That chip does not exist.\n")

	# create a Chip object for the chosen chip
	chipinit = chip.Chip(chip_path)

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

	best_cost = 10000
	best_count = 0

	loopcount = 0
	while True:
		if loopcount > 749:
			break
		loopcount += 1

		# create a Netlist object for the chosen chip and netlist combination
		netlistloop = netlist.Netlist(netlist_path, chipinit.gates, req_sort)

		# generate a new chip for each loop
		chiploop = chip.Chip(chip_path)

		# generate a solution
		wires = wiring.Wiring(netlistloop.net_cor, chiploop, alg_req)

		# calculate cost of the solution
		cost = wires.cost(wires.wire)

		print(f"The cost of this solution is {cost}\n")
		count = 0
		for wire in wires.wire.values():
			if len(wire) != 1:
				count +=1
<<<<<<< HEAD

		if count > best_count or (cost < best_cost and count == best_count):
			best_cost = cost

			print(f"The algorithm laid {count} wires.\n")
			best_count = count
=======
		
		print(f"The algorithm laid {count} wires.\n")
		total_count += count
>>>>>>> 067b6cf56b3b91fddba1e8d16afabc201d01f1cf

		# get the dimensions for the visual representation
		x_dim = chiploop.get_x_dimension(chiploop.gates)
		y_dim = chiploop.get_y_dimension(chiploop.gates)

		# create visual representation of the solved chip
		# visualise = matplot.visualise(chiploop.gates, wires.wire, x_dim, y_dim)
		# break

	print(f"The total_cost is {best_cost}.\n")
	print(f"The total_count is {best_count}.\n")
