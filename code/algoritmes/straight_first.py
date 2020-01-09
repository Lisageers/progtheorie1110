def wire(net_cor, chip):
    """ Determine wire needed to connect the nets. """

    output_dict = {}
    cor_list = []

    for net in net_cor:
        start_cor = list(net[0])
        end_cor = net[1]

        if (end_cor[0] == start_cor[0]) or (end_cor[1] == start_cor[1]):
            cor_list.insert(0, net)
        else:
            cor_list.insert(len(cor_list), net)

    for net in cor_list:
        wire = []
        wire.append(net[0])

        current_cor = list(net[0])
        end_cor = net[1]

        while True:
            # check whether current point and end point are adjacent (manhattan distance)
            if (abs(current_cor[0] - end_cor[0]) == 1 and current_cor[1] - end_cor[1] == 0) or (abs(current_cor[1] - end_cor[1]) == 1 and current_cor[0] - end_cor[0] == 0):
                wire.append(net[1])
                output_dict[net] = wire
                break

            # move towards the end-gate
            else:
                if (end_cor[0] - current_cor[0]) > 0 and chip.check_empty(((current_cor[0] + 1), current_cor[1]), chip.grid):
                    current_cor[0] += 1
                    chip.grid[current_cor[0]][current_cor[1]] = True
                    wire.append(tuple(current_cor))
                elif ((end_cor[0] - current_cor[0]) < 0) and chip.check_empty(((current_cor[0] - 1), current_cor[1]), chip.grid):
                    current_cor[0] -= 1
                    chip.grid[current_cor[0]][current_cor[1]] = True
                    wire.append(tuple(current_cor))
                elif ((end_cor[1] - current_cor[1]) > 0) and chip.check_empty((current_cor[0], (current_cor[1] + 1)), chip.grid):
                    current_cor[1] += 1
                    chip.grid[current_cor[0]][current_cor[1]] = True
                    wire.append(tuple(current_cor))
                elif ((end_cor[1] - current_cor[1]) < 0) and chip.check_empty((current_cor[0], (current_cor[1] - 1)), chip.grid):
                    current_cor[1] -= 1
                    chip.grid[current_cor[0]][current_cor[1]] = True
                    wire.append(tuple(current_cor))


    return output_dict
