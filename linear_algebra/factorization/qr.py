"""
    Created by Faggioni
    Python Script
    @author: Miguel Faggioni
"""

from numpy.linalg import qr as qr_factorization
from numpy.linalg import lu as lu_factorization

def factorizacion_qr(matrix):
    return qr_factorization(matrix)

def factorizacion lu(matrix):
    return lu_factorization(matrix)
