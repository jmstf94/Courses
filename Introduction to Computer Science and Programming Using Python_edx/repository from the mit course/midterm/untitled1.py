# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:14:39 2019

@author: jmstf
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    s=0
    for x in range(len(listA)):
        s=s+listA[x]*listB[x]
    return s