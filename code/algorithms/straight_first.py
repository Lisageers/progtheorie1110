def straight_wire(net_cor, chip):
	""" Determine wire needed to connect the nets. """

	output_dict = {}
	cor_list = []

	# loop through cor and get end and start cors
	for net in net_cor:
		start_cor = list(net[0])
		end_cor = net[1]

		# set cor at start of list when x's or y's are the same
		if (end_cor[0] == start_cor[0]) or (end_cor[1] == start_cor[1]):
			cor_list.insert(0, net)

		# set cor at end of list
		else:
			cor_list.append(net)


	count = 0
	# loop through netlist
	for net in cor_list:
		# initialise wire
		wire = []
		wire.append(net[0])

		# get start and end
		current_cor = list(net[0])
		end_cor = net[1]

		# move while not at end
		while True:
			# check whether current point and end point are adjacent
			if abs(current_cor[0] - end_cor[0]) + abs(current_cor[1] - end_cor[1]) + abs(current_cor[2] - end_cor[2]) == 1:
				wire.append(net[1])
				count += 1
				print(count)
				output_dict[net] = wire
				break

			# move towards the end-gate
			else:
				# move +x if x of end is larger and +x is open
				if (end_cor[0] - current_cor[0]) > 0 and chip.check_empty(((current_cor[0] + 1), current_cor[1], current_cor[2]), chip.grid):
					current_cor[0] += 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

				# move -x if x of end is smaller and -x is open
				elif ((end_cor[0] - current_cor[0]) < 0) and chip.check_empty(((current_cor[0] - 1), current_cor[1], current_cor[2]), chip.grid):
					current_cor[0] -= 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

				# move +y if y of end is larger and +y is open
				elif ((end_cor[1] - current_cor[1]) > 0) and chip.check_empty((current_cor[0], (current_cor[1] + 1), current_cor[2]), chip.grid):
					current_cor[1] += 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

				# move -y if y of end is smaller and -y is open
				elif ((end_cor[1] - current_cor[1]) < 0) and chip.check_empty((current_cor[0], (current_cor[1] - 1), current_cor[2]), chip.grid):
					current_cor[1] -= 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

				# move -z if z of end is larger and -z is open
				elif ((end_cor[2] - current_cor[2]) < 0) and chip.check_empty((current_cor[0], current_cor[1], (current_cor[2] - 1)), chip.grid):
					current_cor[2] -= 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

				# move +z if z of end is larger and +z is open
				else:
					if current_cor[2] + 1 == 8:
						return None
					current_cor[2] += 1
					chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
					wire.append(tuple(current_cor))

	return output_dict
