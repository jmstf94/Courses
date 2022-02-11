# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:42:39 2019

@author: jmstf
"""
s='azcbobobegghakl'
count=0
for letter in s:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count+=1
print('Number of vowels: '+str(count))        
    
    