"""
main.py

Minor programmeren, programmeertheorie
January 2020
Marte van der Wijk, Lisa Geers, Emma Caarls

Connect gates on a grid.
"""

from code.classes import , netlist, wiring


if __name__ = '__main__':
    
	filename = input("Enter the filename of your print.\n")

	chip = chip.Chip(filename)

	netlist_name = input("Enter the filename of the netlist to use.\n")

	netlist = netlist.Netlist(netlist_name, chip.gates)

	wiring = wiring.Wiring(netlist, chip)