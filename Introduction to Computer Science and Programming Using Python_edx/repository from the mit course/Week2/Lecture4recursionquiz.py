# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:04:41 2019

@author: jmstf
"""

def iterPower(base, exp):
    if exp==1:
       return base
    else:
       return base*iterPower(base,exp-1)
print(iterPower(2,10))