# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:36:45 2019

@author: jmstf
"""

balance=4773
annualInterestRate=0.2
monthlyPayment=0
bal=balance
while bal>=0:
    monthlyPayment=monthlyPayment+10
    bal=balance
    for x in range(12):
        bal=bal-monthlyPayment
        print(bal)
        bal=bal+(annualInterestRate/12.0)*bal
        print(bal)
    print(monthlyPayment)
print("Lowest Payment:",monthlyPayment)