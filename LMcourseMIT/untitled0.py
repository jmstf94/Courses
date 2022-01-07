# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:05:19 2020

@author: jmstf
"""
import numpy as np
import sympy as sm
from itertools import permutations

def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):
    """
    Properly updates the classification parameter, theta and theta_0, on a
    single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    z=(np.dot(feature_vector,current_theta)+current_theta_0)*label
    if (z<0.00000001):
        return (current_theta+label*feature_vector,current_theta_0+label)
    else:
        return (current_theta,current_theta_0)

def perceptron_algorithm(feature_matrix, labels, T,order_list):
    """
    Runs the full perceptron algorithm on a given set of data. Runs T
    iterations through the data set, there is no need to worry about
    stopping early.

    NOTE: Please use the previously implemented functions when applicable.
    Do not copy paste code from previous parts.

    NOTE: Iterate the data matrix by the orders returned by get_order(feature_matrix.shape[0])

    Args:
        feature_matrix -  A numpy matrix describing the given data. Each row
            represents a single data point.
        labels - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        T - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.
        order_list - the list of numbers that specifies the permutation
            of training

    Returns: A tuple where the first element is a numpy array with the value of
    theta, the linear classification parameter, after T iterations through the
    feature matrix and the second element is a real number with the value of
    theta_0, the offset classification parameter, after T iterations through
    the feature matrix.Combined in another tuple part the mistake count list.
    """
    n_r, n_c = feature_matrix.shape
    theta=np.zeros(((n_c,)))
    theta_0=0
    mistake_count=[0]*n_r
    for t in range(T):
        for i in order_list:
            x,y=theta,theta_0
            theta,theta_0 = perceptron_single_step_update(feature_matrix[i],labels[i],theta,theta_0)
            if (x-theta).any() or (y!=theta_0):
                mistake_count[i]+=1
    return ((theta,theta_0),mistake_count)

labels = np.array([-1,-1,-1,-1,-1,+1,+1,+1,+1,+1])
data_points = np.array([[0,0],[2,0],[3,0],[0,2],[2,2],[5,1],[5,2],[2,4],[4,4],[5,5]])
num_of_mistakes = [1,9,10,5,9,11,0,3,1,1]

for g in list(permutations(range(9))):
    x,y=perceptron_algorithm(data_points, labels, 10, g)
    if y==num_of_mistakes:
        print(x)
    