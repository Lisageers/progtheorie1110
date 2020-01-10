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
			print("That chip does not exist.")

	# create a Chip object for the chosen chip
	chip = chip.Chip(chip_path)

	# let user choose a netlist
	while True:
		req_netlist = input("Which netlist do you want to use? (1, 2, 3)\n")
		if req_netlist == '1':
			netlist_path = 'data/' + req_chip + '/netlist_1.csv'
			break
		elif req_netlist == '2':
			netlist_path = 'data/' + req_chip + '/netlist_2.csv'
			break
		elif req_netlist == '3':
			netlist_path = 'data/' + req_chip + '/netlist_3.csv'
			break
		else:
			print("That is not an option.")

	# create a Netlist object for the chosen chip and netlist combination
	netlist = netlist.Netlist(netlist_path, chip.gates)

	# generate a solution
	wiring = wiring.Wiring(netlist, chip)

	# get the dimensions for the visual representation
	x_dim = chip.get_x_dimension(chip.gates)
	y_dim = chip.get_y_dimension(chip.gates)

	# create visual representation of the solved chip
	visualise = matplot.visualise(chip.gates, wiring.wire, x_dim, y_dim)
