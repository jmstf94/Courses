import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    list_of_all_combs = []
    n = len(choices)
    ####all combinations as string
    for i in range(2**n):
        stringy = bin(i).replace('0b', '')
        for j in range(len(choices)-len(stringy)):
            stringy = '0'+stringy
        list_of_all_combs.append(stringy)
    ##### calculate sum for each comb
    for i in range(len(list_of_all_combs)):
        string = list_of_all_combs[i]
        sum = 0
        for k in range(len(string)):
            if string[k]=='1':
                sum+= choices[k]
        if sum == total:
            to_return = []
            for j in string:
                to_return.append(int(j))
            return np.array(to_return)



# print(find_combination([3, 10, 2, 1, 5], 12)) #[0, 1, 1, 0, 0]
# print(find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)) #[1, 1, 1, 1, 1, 1, 1]
# print(find_combination([21, 15, 100, 19, 12], 12)) #[0, 0, 0, 0, 1]
# print(find_combination([10, 10, 11, 11, 11], 20) #[1, 1, 0, 0, 0]
# print(find_combination([4, 6, 3, 5, 2], 10) #[1, 1, 0, 0, 0]
# print(find_combination([1, 3, 4, 2, 5], 16) #[1, 1, 1, 1, 1]
# print(find_combination([1, 81, 3, 102, 450, 10], 9) #[1, 0, 1, 0, 0, 0]
# print(find_combination([105, 10, 9, 6, 4], 120) #[1, 0, 1, 1, 0]
# print(find_combination([1], 10) #[1]
