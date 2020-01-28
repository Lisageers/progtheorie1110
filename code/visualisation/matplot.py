from code.classes import chip
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def visualise(gates, output_dict, x, y):
	""" Create a visual representation of the solved chip. """

	# make 3D-figure
	fig = plt.figure()
	plot = fig.gca(projection='3d')
	
	# create grid
	plot.set_xlabel("X")
	plot.set_xlim(0.0, x, 1.0)
	plot.set_ylabel("Y")
	plot.set_ylim(0.0, y, 1.0)
	plot.set_zlabel("Z")
	plot.set_zlim(0.0, 7.0, 1.0)

	# create scatterplot
	cor_x = []
	cor_y = []

	for gate in gates:
		cor_x.append(gate[0])
		cor_y.append(gate[1])
	plt.scatter(cor_x, cor_y, marker='H', c='r', s=200, edgecolors='k')

	# create lines between gates
	for wires in output_dict.values():
		line_x = []
		line_y = []
		line_z = []
		for cor in wires:
			line_x.append(cor[0])
			line_y.append(cor[1])
			line_z.append(cor[2])
			plt.plot(line_x, line_y, line_z)
	
	plt.savefig(f"results/output.png")
	
	# show plot
	plt.show()
