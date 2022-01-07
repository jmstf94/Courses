import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")

for K in [1,2,3,4]:
    costs = []
    for seed in range(5):
        mixture, post = common.init(X, K, seed= seed)
        mixture, post, cost = kmeans.run(X, mixture, post)
        costs.append(cost)
    print(np.min(costs))
