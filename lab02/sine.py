'''
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
'''
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class AbsVariant(Problem):
    '''
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    '''

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    # There is no goal_test for this problem.

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x*math.sin(x))


# This creates a 2D hill function with a single maximum value and runs both local search algorithms.
maximum = 30
initial = randrange(0, maximum)  # Pick a random starting value for x.
bestHillClimbX = 0
bestSimAnnX = 0
hillList = []
annealList = []
for i in range(100):
    initial = randrange(0, maximum)  # Pick a random starting value for x.
    p = AbsVariant(initial, maximum, delta=1.0)  # Create an Abs variant problem, specifying the delta step value.

    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    hillList.append(p.value(hill_solution))
    if p.value(hill_solution) > p.value(bestHillClimbX):
        bestHillClimbX = hill_solution

    # Solve the problem using simulated annealing.
    annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
    annealList.append(p.value(annealing_solution))
    if p.value(annealing_solution) > p.value(bestSimAnnX):
        bestSimAnnX = annealing_solution


hillAvg = sum(hillList)/float(len(hillList))
annealAvg = sum(annealList)/float(len(annealList))

print('Initial                      x: ' + str(p.initial) + '\t\tvalue: ' + str(p.value(initial)))
print('Hill-climbing solution       x: ' + str(bestHillClimbX) + '\tvalue: ' + str(p.value(bestHillClimbX)))
print('Simulated annealing solution x: ' + str(bestSimAnnX) + '\tvalue: ' + str(p.value(bestSimAnnX)))
print(f'Hill average: {hillAvg}')
print(f"Annealing average {annealAvg}")