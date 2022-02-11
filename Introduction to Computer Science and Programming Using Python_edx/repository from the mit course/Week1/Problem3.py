# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 04:17:46 2019

@author: jmstf
"""
#s='bobobegghakl'
maxim=0
p='abcdefghijklmnopqrstuvwxyz'
i=-1
x=0
counter=0
maximwr=''
while x<=len(s)-1:
    for l in range(0,26):
        if s[x]==p[l] and l>=i:
            i=l
            counter+=1
            maximwr=maximwr+s[x]
            break
    if counter>maxim:
        maxim=counter
        maximword=maximwr
    if l>=25:
        if i>=25:
            x=x+1
        i=-1
        counter=0
        maximwr=''
    else:
        x=x+1
print(maximword)
print(maxim)