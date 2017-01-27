"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
import matplotlib.pyplot as plt


def plot_shapes(shape):
	fig, ax = plt.subplots()
	ax.plot(shape.verts_x, shape.verts_y)
	plt.grid()
	plt.axis([-20, 20, -20, 20])
	plt.show()
