# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:06:10 2019

@author: jmstf
"""
print('Please think of a number between 0 and 100')
x=50
i=50
while True:
    print('Is your secret number ',x,'?')
    test=input("Enter 'h' to indicate the guess is too high.Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.")
    if test=='h':
        x=x-int(i/2)
    elif test=='l':
        x=x+int(i/2)
    elif test=='c':
        print('Game over. Your secret number was: ',x)
        break
    else:
        print('Sorry, I did not understand your input.')
    if i%2==0:
        i=int(i/2)
    else:
        i=int((i-1)/2)
    if i<=1:
        i=2