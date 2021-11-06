import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    x = random.randint(0,49)
    return 2*x

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    x = random.randint(5,10)
    return 2*x
