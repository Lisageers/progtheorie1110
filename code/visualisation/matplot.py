from code.classes import chip
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def visualise(gates, output_dict, x, y):
    plt.clf()
    plt.xlim(0.0, x, 1.0)
    plt.ylim(0.0, y, 1.0)
    plt.grid(True)

    cor_x = []
    cor_y = []

    for gate in gates:
        cor_x.append(gate[0])
        cor_y.append(gate[1])

    plt.scatter(cor_x, cor_y)

    line_x = []
    line_y = []

    for wires in output_dict.values():
        print("wires:", wires)
        for cor in wires:
            line_x.append(cor[0])
            line_y.append(cor[1])
            plt.plot(line_x, line_y)

    print(line_x)
    print(line_y)



    plt.savefig("test1.png")

    plt.show()
