from code.classes import chip
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def visualise(gates, output_dict, x, y):

    # clear previous plot
    plt.clf()

    # create grid
    plt.xlim(0.0, x, 1.0)
    plt.ylim(0.0, y, 1.0)
    plt.grid(True)

    # create lines
    for wires in output_dict.values():
        line_x = []
        line_y = []
        for cor in wires:
            line_x.append(cor[0])
            line_y.append(cor[1])
        plt.plot(line_x, line_y)


    # create scatterplot
    cor_x = []
    cor_y = []

    for gate in gates:
        cor_x.append(gate[0])
        cor_y.append(gate[1])
    plt.scatter(cor_x, cor_y, marker='H', c='r', s=200, edgecolors='k')

    # show plot
    plt.savefig("test1.png")
    plt.show()
