import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(14277)

N = 10000
n_steps = 1000

unique_array = []

for rep in range(N):
    x = []
    y = []
    j = 0
    k = 0
    x.append(j)
    y.append(k)

    for i in range(n_steps):
        r  = random.random()
        xy = random.random()
        if xy>=0.5:
            if r>=0.5:
                j += 1
            else:
                j -= 1
        else:
            if r>=0.5:
                k += 1
            else:
                k -= 1
        x.append(j)
        y.append(k)
    x = np.array(x)
    y = np.array(y)

    coord = np.empty([len(x), 2], dtype=np.int64)
    coord[:,0] = x
    coord[:,1] = y

    unique = []
    for i in range(10):
        unique.append(len(np.unique(coord[100*i:100*(i+1)], axis=0)))

    unique_array.append(unique)


unique_array = np.array(unique_array)
S = np.sum(unique_array, axis=0) // N


steps = [element for element in range(100,1100,100)]

plt.plot(steps, S, "--o")
plt.xlabel("Time (steps)")
plt.xlim(0,1100)
plt.xticks(steps)
plt.ylabel("<S>")
plt.title("<S> - Time plot")
#plt.text(800, 15.2, str(N)+" simulations")
plt.savefig("scatterplot2d_"+str(N)+".png", dpi=100, bbox_inches="tight")
