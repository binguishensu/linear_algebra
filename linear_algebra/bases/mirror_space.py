
"""
	Created by Faggioni
	Python Script
	@author: Miguel Faggioni
"""


from numpy import matrix


def mirror_by_x():
	return matrix('-1,0;0,1')


def mirror_by_y():
	return matrix('1,0;0,-1')
