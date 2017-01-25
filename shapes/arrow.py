"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from shapes.shape import Shape

class Arrow(Shape):

	def __init__(self,origin_x = 0,origin_y = 0):
		Path = mpath.Path
		path_data = [
		    (Path.MOVETO, (0 + origin_x,0 + origin_y)),
		    (Path.LINETO, (5 + origin_x,0 + origin_y)),
		    (Path.LINETO, (5 + origin_x,1 + origin_y)),
		    (Path.LINETO, (7 + origin_x,0 + origin_y)),
		    (Path.LINETO, (5 + origin_x, -1 + origin_y)),
		    (Path.CLOSEPOLY, (5 + origin_x, 0 + origin_y))
		    ]
		codes, verts = zip(*path_data)
		self.path = mpath.Path(verts, codes)
		self.x_vertex, self.y_vertex = zip(*self.path.vertices)
		self.vertex = self.path.vertices

