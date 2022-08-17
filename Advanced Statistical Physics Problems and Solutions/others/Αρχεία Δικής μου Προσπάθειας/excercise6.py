import random
import matplotlib.pyplot as plt

import numpy as np

random.seed(14277)

A = np.zeros([500,500])
B = np.zeros([500,500])

for i in range(2500):
    x = random.choice(range(500)) # the traps
    y = random.choice(range(500))
    A[x,y] = 1

for i in range(250):
    x = random.choice(range(500)) # the traps
    y = random.choice(range(500))
    B[x,y] = 1

N = 100000




S1 = []
S2 = []
steps1 = []
steps2 = []

for i in range(N):

    flag = False
    while flag==False:
        x01 = random.choice(range(500)) # the initial position
        y01 = random.choice(range(500))
        if A[x01,y01]==0:
            flag = True
    flag = False
    while flag==False:
        x02 = random.choice(range(500)) # the initial position
        y02 = random.choice(range(500))
        if B[x02,y02]==0:
            flag = True


    flag = False
    x1 = []
    y1 = []
    x1.append(x01)
    y1.append(y01)
    j = x01
    k = y01
    n1 = 0

    while flag==False:
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

        if j==-1:
            j = 499
        if k==-1:
            k = 499
        if j==500:
            j = 0
        if k==500:
            k = 0
        x1.append(j)
        y1.append(k)
        n1 +=1

        if A[j,k]==1:
            flag = True

    x1 = np.array(x1)
    y1 = np.array(y1)

    steps1.append(n1)

    coord1 = np.empty([len(x1), 2], dtype=np.int64)
    coord1[:,0] = x1
    coord1[:,1] = y1

    S1.append(len(np.unique(coord1[::], axis=0)))


    flag = False
    x2 = []
    y2 = []
    x2.append(x02)
    y2.append(y02)
    j = x02
    k = y02
    n2 = 0

    while flag==False:
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

        if j==-1:
            j = 499
        if k==-1:
            k = 499
        if j==500:
            j = 0
        if k==500:
            k = 0
        x2.append(j)
        y2.append(k)
        n2 +=1

        if B[j,k]==1:
            flag = True

    x2 = np.array(x2)
    y2 = np.array(y2)

    steps2.append(n2)

    coord2 = np.empty([len(x2), 2], dtype=np.int64)
    coord2[:,0] = x2
    coord2[:,1] = y2

    S2.append(len(np.unique(coord2[::], axis=0)))



#plt.hist(steps2, label='C=$10^{-3}%$')
#plt.hist(steps1, label='C=$10^{-2}%$')
#plt.xlabel("Time (steps)")
#plt.ylabel("Frequency")
#plt.title("Particle Life Time Plot")
#plt.legend(loc="upper right")
#plt.text(800, 15.2, str(N)+" simulations")
#plt.savefig("hist_steps.png", dpi=100, bbox_inches="tight")

plt.plot(steps2, S2, "--ro", label= 'C=$10^{-3}$')
plt.plot(steps1, S1, "--o", label= 'C=$10^{-2}%$')
plt.xlabel("Time (steps)")
plt.ylabel("S")
plt.title("S - Time plot")
plt.legend(loc="upper left")
#plt.text(800, 15.2, str(N)+" simulations")
plt.savefig("S_steps.png", dpi=100, bbox_inches="tight")
