# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:42:28 2019

@author: jmstf
"""

import numpy as np

def apply_stochastic_matrix(p, M):
    """Apply the matrix M to the vector p, but only if
    p is a stochastic vector and M is a left stochastic
    matrix. Otherwise raise a ValueError.
    """
    k=np.array([p[0]*M[0,0]+p[0]*M[0,1],p[1]*M[1,0]+p[1]*M[1,1]])
    if abs(np.linalg.norm(k,ord=1)-1)<0.1:
        return k

M=np.array([[1,0],[0,0]])
p=np.array([0.2,0.8])
apply_stochastic_matrix(p,M)