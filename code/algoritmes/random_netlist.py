from random import shuffle

def wire(net_cor, chip):
    """ Determine wire needed to connect the nets. """

    output_dict = {}

    print("not: ", net_cor)

    shuffle(net_cor)

    print('shuffeled:', net_cor)

    for net in net_cor:
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
