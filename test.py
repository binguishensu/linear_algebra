"""
Demo of a PathPatch object.
"""
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from shapes.arrow import Arrow
from plots.plot import plot_shapes as ps


arrow = Arrow(2,2)
ps(arrow)
