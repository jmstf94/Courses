# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#1
#x=np.array([[-1,-1],[1,0],[-1,1.5]])
#y=np.array([1,-1,1])
#2
#x=np.array([[1,0],[-1,1.5],[-1,-1]])
#y=np.array([-1,1,1])
#x=np.array([[-1,-1],[1,0],[-1,10]])
#y=np.array([1,-1,1])
#x=np.array([[1,0],[-1,10],[-1,-1]])
#y=np.array([-1,1,1])
x=np.array([[-4,2],[-2,1],[-1,-1],[2,2],[1,-2]])
y=np.array([1,1,-1,-1,-1])
T=30
theta=np.array([0,0])
theta_0=0
for t in range(0,T):
    for i in range(len(y)):
        if(y[i]*(np.dot(x[i],theta)+theta_0)<=0):
            theta=theta+y[i]*x[i]
            theta_0=theta_0+y[i]
        print("round",t,"    ",i,"th---->",theta,"-------->",theta_0)