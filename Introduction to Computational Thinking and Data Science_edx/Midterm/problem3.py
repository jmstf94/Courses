"""
You are given a list of unique positive integers L sorted in
descending order and a positive integer sum s.
The list has n elements. Consider writing a program that finds
values for multipliers m0,m1,.... such that the following equation holds:
s = L[0]*m0+L[1]*m1+...+L[n-1]*m_(n-1)
"""
"""
Assume a greedy approach to this problem.
You calculate the integer multipliers m_0, m_1, ..., m_(n-1)
 by finding the largest multiplier possible for the
 largest value in the list, then for the second largest,
 and so on. Write a function that returns the sum of the
 multipliers using this greedy approach. If the greedy approach
 does not yield a set of multipliers such that the equation above
 sums to s, return the string "no solution". Write the function
 implementing this greedy algorithm with the specification below:
"""
def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
        L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
        not yield a set of multipliers such that the equation sums to 's'
    """
    m = []
    for x in L:
        if x<=s:
            division = s//x
            m.append(division)
            s = s - x*(division)
    if s==0 and len(m)!=0:
        return sum(m)
    else:
        return "no solution"

print(greedySum([10,7,6,3],19))
