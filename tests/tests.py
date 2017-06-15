"""
    Created by Faggioni
    Python Script
    @author: Miguel Faggioni
"""


import sys
sys.path.append('/home/faggioni/Documents/Github/linear_algebra/')

import linear_algebra.diagonalization as d

def diagonalization(matrix):
    return d.diagonalizacion(matrix)

def eigenvalues(matrix):
    return d.autovalores(matrix)

def eigenvectors(matrix):
    return d.autovectores(matrix)
