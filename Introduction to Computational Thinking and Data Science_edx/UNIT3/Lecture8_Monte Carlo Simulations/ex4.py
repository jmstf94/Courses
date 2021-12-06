import random

def random_pop(list):
    """
    pops a random element from a list and returns the renewd list
    and the poped element as a tuple
    """
    r = random.randint(0,len(list)-1)
    x = list.pop(r)
    return (x,list)

def single_trial(bucket):
    '''
    a single trial of 3 choices from a bucket, return the chosen balls
    '''
    chosen = []
    for i in range(3):
        x, bucket = random_pop(bucket)
        chosen.append(x)
    return chosen

def identical_elements(list):
    '''
    returns True if all elements in the given list are identical
    False otherwise
    '''
    flag = True
    checklist = []
    for x in list:
        checklist.append(x)
    for x in range(len(list)-1):
        if list[x]!=checklist[x+1]:
            flag = False
    return flag

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    times = 0
    for i in range(numTrials):
        bucket = ['Red','Green','Red','Green','Red','Green']
        chosen = single_trial(bucket)
        if identical_elements(chosen):
            times+=1
    return times/numTrials

#print(noReplacementSimulation(10))
