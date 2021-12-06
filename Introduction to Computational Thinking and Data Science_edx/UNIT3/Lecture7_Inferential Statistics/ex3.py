# import os
# os.environ["OPENBLAS_NUM_THREADS"] = "1"
# import numpy as np

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L)==0:
        return float("nan")
    L = np.array(L)
    lenghts = []
    for x in L:
        lenghts.append(len(x))
    lengths = np.array(lenghts)
    return np.std(lenghts)

#print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
