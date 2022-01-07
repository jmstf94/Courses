# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 00:10:46 2020

@author: jmstf94
"""
def function1(x):
    return x
def function2(x):
    return x**2
functions=[function1,function2]
print(functions) 

def get_sum_metrics(predictions, metrics):
    for i in range(3):
        metrics.append((lambda y: lambda x: x + y)(i))
    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)
    return sum_metrics
print(get_sum_metrics(3,functions))
print(functions) 
print(get_sum_metrics(3,functions))