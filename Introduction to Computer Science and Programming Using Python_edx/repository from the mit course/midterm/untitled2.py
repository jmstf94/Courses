# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:19:58 2019

@author: jmstf
"""
def uniqueValues(aDict):
    a=list(aDict.values())
    b=list(aDict.keys())
    c=[]
    for x in range(len(aDict)):
        count=0
        for i in range(len(a)):
            if a[i]==a[x]:
                count+=1
            if count==2:
                break
        if count==1:
           c.append(b[x])
    return sorted(c)
p={2: 1, 6: 2, 1: 3,3:1}
print(uniqueValues(p))