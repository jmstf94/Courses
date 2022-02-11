# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:58:27 2019

@author: jmstf
"""
balance=42
annualInterestRate=0.2
monthlyPaymentRate=0.04
for x in range(12):
    balance=balance-monthlyPaymentRate*balance
    balance=balance+(annualInterestRate/12)*balance
print('Remaining balance:', round(balance,2))