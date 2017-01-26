"""
Created by Faggioni
Python Script
@author: Miguel Faggioni
"""
from bases.rotate_space import rotate_by_angle
from bases.scale_space import scale_by_factor
from bases.mirror_space import mirror_by_x, mirror_by_y
from numpy import matmul,matrix


class Shape(object):


	def __init__(self, verts_x, verts_y):
		self.verts_x = verts_x
		self.verts_y = verts_y
		self.verts = []
		for item in zip(verts_x, verts_y):
			self.verts.append([[item[0]],[item[1]]])
	

	def rotate(self, angle=0):
		matrix_base = rotate_by_angle(angle)
		self.set_vertex(matrix_base)
		

	def scale(self,factor=1):
		matrix_base = scale_by_factor(factor)
		self.set_vertex(matrix_base)

	def mirror(self,type='x'):
		if type == 'x':
			matrix_base = mirror_by_x()
			self.set_vertex(matrix_base)
		elif type == 'y':
			matrix_base = mirror_by_y()
			self.set_vertex(matrix_base)

	def translate(self, x=0, y=0):
		aux_verts = []
		for vert in self.verts:
			aux_verts.append([vert[0][0] + x, vert[1][0] + y])
		self.verts = aux_verts
		self.verts_x, self.verts_y = zip(*self.verts)


	def set_vertex(self, matrix):
		aux_verts = []
		for vert in self.verts:
			aux_verts.append(matmul(matrix,vert).tolist())
		self.verts = aux_verts
		self.verts_x, self.verts_y = zip(*self.verts)


	
	
	