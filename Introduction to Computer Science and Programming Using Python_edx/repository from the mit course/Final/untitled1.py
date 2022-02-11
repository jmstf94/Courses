# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:39:41 2019

@author: jmstf
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    i=1
    while k>0:
        k-=i
        i+=1
    if k==0:
        return True
    else:
        return False
    
print(is_triangular(3))