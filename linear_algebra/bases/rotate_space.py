"""
	Created by Faggioni
	Python Script
	@author: Miguel Faggioni
"""


import math
from numpy import matrix


def rotate_by_angle(angle):
	angle = (angle * math.pi) / 180
	return matrix([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
