"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""

from shapes.shape import Shape


class Arrow(Shape):

	def __init__(self):
		self.path = [[0, 0], [5, 0], [5, 1], [7, 0], [5, -1], [5, 0]]
		verts_x, verts_y = zip(*self.path)
		super(Arrow, self).__init__(list(verts_x), list(verts_y))
