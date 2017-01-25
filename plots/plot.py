"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
import matplotlib.pyplot as plt

def plot_shapes(shape):
	fig, ax = plt.subplots()
	x, y = zip(*shape.path.vertices)
	line, = ax.plot(x,y)
	plt.grid()
	plt.axis([-20,20,-20,20])
	plt.show()

