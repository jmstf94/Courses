# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:24:26 2019

@author: jmstf
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    kleidia=[]
    times=[]
    for i in aDict.keys():
        kleidia.append(i)
    for i in aDict.values():
        times.append(i)
    listofkeys=[]
    for i in range(len(times)):
        count=0
        for k in range(len(times)):
            if times[i]==times[k]:
                count+=1
            if count>=2:
                break
        if count==1:
            listofkeys.append(kleidia[i])
    if len(listofkeys)==0:
        return listofkeys
    else:
        if listofkeys.sort()==None:
            return listofkeys
        else:
            return listofkeys.sort()

P = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
O = {1: 1, 2: 1, 3: 1}
print(uniqueValues(P))