# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:48:50 2019

@author: jmstf
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    cpL=L.copy()
    cpL.sort(reverse=True)
    max=cpL[1]
    oddflag=False
    for k in cpL:
        if k==max:
            oddflag=not(oddflag)
        else:
            if oddflag==True:
                break
            max=k
            oddflag=True
    if oddflag==True:
        return max
    else:
        return None

print(largest_odd_times([2,2,4,4]))
print(largest_odd_times([3,5,3,5,3]))