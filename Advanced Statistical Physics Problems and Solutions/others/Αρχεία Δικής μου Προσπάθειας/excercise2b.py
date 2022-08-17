import numpy as np
import matplotlib.pyplot as plt
import random


N = 100000
n = 1000

random.seed(14277)

R_squar = []
xF = []
yF = []

for rep in range(N):

    x = 0
    y = 0

    for i in range(n):
        xy = random.random()
        r  = random.random()
        if xy>=0.5:
            if r>=0.5:
                x += 1
            else:
                x -= 1
        else:
            if r>=0.5:
                y += 1
            else:
                y -= 1
    xF.append(x)
    yF.append(y)
    R_squar.append(x**2 + y**2)

R_ave = sum(R_squar) / N
print(R_ave)

h = plt.hist2d(xF,yF,bins=100)
plt.colorbar(h[3])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random 2D Walk - Distribution")
plt.text(40, -80, "$R^2$="+str(R_ave), color="white")
plt.savefig("histogram.png", dpi=100, bbox_inches='tight')
