
def wire(net_cor, chip):
    """ Determine wire needed to connect the nets. """

    output_dict = {}

    # loop through netlist
    for net in net_cor:
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
                print("wire", wire)
                output_dict[net] = wire
                break

            # move towards end-gate
            else:
                # move +x if x of end is larger and +x is open
                if (end_cor[0] - current_cor[0]) > 0 and chip.check_empty(((current_cor[0] + 1), current_cor[1], current_cor[2]), chip.grid):
                    print("+X")
                    current_cor[0] += 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))

                # move -x if x of end is smaller and -x is open
                elif ((end_cor[0] - current_cor[0]) < 0) and chip.check_empty(((current_cor[0] - 1), current_cor[1], current_cor[2]), chip.grid):
                    print("-X")
                    current_cor[0] -= 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))

                # move +y if y of end is larger and +y is open
                elif ((end_cor[1] - current_cor[1]) > 0) and chip.check_empty((current_cor[0], (current_cor[1] + 1), current_cor[2]), chip.grid):
                    print("+Y")
                    current_cor[1] += 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))

                # move -y if y of end is smaller and -y is open
                elif ((end_cor[1] - current_cor[1]) < 0) and chip.check_empty((current_cor[0], (current_cor[1] - 1), current_cor[2]), chip.grid):
                    print("-Y")
                    current_cor[1] -= 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))

                # move -z if z of end is larger and -z is open
                elif ((end_cor[2] - current_cor[2]) < 0) and chip.check_empty((current_cor[0], current_cor[1], (current_cor[2] - 1)), chip.grid):
                    print("-Z")
                    current_cor[2] -= 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))
				
				# move +z if z of end is larger and +z is open
                else:
                    if current_cor[2] + 1 == 8:
                        return None
                    print("+Z")
                    current_cor[2] += 1
                    chip.grid[current_cor[0]][current_cor[1]][current_cor[2]] = True
                    wire.append(tuple(current_cor))
                

    return output_dict
