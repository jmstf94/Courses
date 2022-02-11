# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:33:22 2019

@author: jmstf
"""
count=0
s='azcbobobobegghakl'
num=0
x=len(s)-2
for i in range(x):
    if s[i]+s[i+1]+s[i+2]=='bob':
        num+=1
print('Number of times bob occurs is: ',num)