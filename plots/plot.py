"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
import matplotlib.pyplot as plt

def plot(title = 'Plot', x, y):
	plt.plot(x,y)
	plt.xlabel('X - Coodinate')
	plt.ylabel('Y - Coordinate')
	plt.show()

def plot_shape(figure,title='Figure Plot'):
	plt.plot(figure)
