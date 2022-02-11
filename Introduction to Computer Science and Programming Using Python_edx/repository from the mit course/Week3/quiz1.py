# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:32:35 2019

@author: jmstf
"""
aTup=('I', 'am', 'a', 'test', 'tuple')
def oddTuples(f):
    t=()
    for x in range(0,len(f)+1,2):
        t+=(f[x],)
    return t
oddTuples(aTup)

