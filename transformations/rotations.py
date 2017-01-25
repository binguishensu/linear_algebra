"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
from numpy import matrix
import math

class rotation:

	def __init__(self,angle=0):
		self.angle = angle
		self.angle_radiand = (angle * math.pi) / 180.0
		self.matrix = matrix([math.cos(self.angle_radiand), -math.sin(self.angle_radiand)],[math.sin(self.angle_radiand),math.cos(self.angle_radiand)])

	@staticmethod
	def rotate(array):
		return array * self.matrix





