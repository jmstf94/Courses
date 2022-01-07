import random
# helper function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return (mean, std)

def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess

    Runs a Monte Carlo simulation, 'num_trials' times. In each trial
    you guess what each food is, the ith food has 'prob[i]' probability
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars.

    Returns: a tuple of the mean and standard deviation over
    'num_trials' trials of the net money earned
    when making len(probs) guesses
    """
    data_points = []
    for i in range(num_trials):
        earnings = 0
        for k in range(len(probs)):
            prob_of_correct_guess = probs[k]
            randomlist = ['1']*int(prob_of_correct_guess*10) + ['0']*int((1-prob_of_correct_guess)*10)
            r = int(random.choice(randomlist))
            if r==1:
                earnings+=get
        final_gain = earnings-cost*len(probs)
        data_points.append(final_gain)
    return getMeanAndStd(data_points)

#print(guessfood_sim(3000, [0.1, 0.1, 0.7], 0.5, 0.8))
