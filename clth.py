# -*- coding: utf-8 -*-
"""
This is an example
confirming the Central Limit Theorem
computationaly.
"""

#Firstly we create some arbitrary pdf's.
import numpy as np
import matplotlib.pyplot as plt
#degrees of freedom of chi pdf
df=20
#usual parameter lambda of the exp
l=50
#mean, standard deviation and sample size of the normal dist
m=150
s=20
#bins and binwidth of the plots
bwdth=200
bins = np.linspace(0,400,bwdth)
#the size of the samples
n=10000



"""plots"""
chi = np.random.chisquare(df,n)
plt.hist(chi,bins, alpha=0.5, label='chi')
exp=np.random.exponential(l,n)
plt.hist(exp,bins,alpha=0.5, label='exp')
norm = np.random.normal(m,s,n)
plt.hist(norm ,bins, alpha=0.5, label='norm')
plt.legend(loc='upper right')
plt.savefig('the different distributions')


"""
We combine anyway we want these three distributions. We lack mathematical
rigor here but that doesn't mess with our goal.
For simplicity I create a distribution by taking the sum of the three.
"""
pdf=[x+y+z for x,y,z in zip(chi,exp,norm)]
#the plot and find the mean value of the whatever pdf:
plt.hist(pdf,bins)
plt.savefig('with the new distribution')
mean=sum(pdf)/n


#let us choose n random samples of our new whatever pdf of size m each one
n=10000
m=100

#we create the mean values list of the m groups
f=[]
for i in range(0,n):
    k=np.random.choice(pdf,m)
    p=sum(k)/m
    f.append(p)
    
#plotting the mean list must give a normal distribution
bwdth=200
bins = np.linspace(150,300,bwdth)
plt.hist(f,bins)
plt.savefig('with the normal distribution')
plt.show()