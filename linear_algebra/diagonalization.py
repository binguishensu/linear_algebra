"""
    Created by Faggioni
    Python Script
    @author: Miguel Faggioni
"""

from numpy import linalg as l

def autovalores(matrix):
    return l.eig(matrix)[0]

def autovectores(matrix):
    return l.eig(matrix)[1]
