
"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
from shapes.arrow import Arrow
from plots.plot import plot_shapes as ps


arrow = Arrow()
arrow.rotate(235)
arrow.scale(2)
arrow.mirror('x')
ps(arrow)
