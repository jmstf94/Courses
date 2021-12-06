def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    x = 0
    flag = test(x)
    negflag = test(-x)
    while not (flag or negflag):
        x+=1
        try:
            flag = test(x)
            negflag = test(-x)
        except:
            flag = test(x)
        if flag or negflag:
            if flag:
                return x
            elif negflag:
                return -x
    return 0
