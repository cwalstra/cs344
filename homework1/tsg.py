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
from timeit import default_timer as timer


class TSG(Problem):
    '''
    State: A list of the cities in visitation order
    Action: Swap two cities
    '''

    def __init__(self, initial, lengths):
        self.initial = initial
        self.lengths = lengths

    def actions(self, state):
        actions = []
        for i in range(len(state)-1):
            actions.append([state[i+1], state[i]])
        return actions

    # There is no goal_test for this problem.

    def result(self, state, action):
        newState = state[:]
        # find indices
        index1 = newState.index(action[1])
        index2 = newState.index(action[0])

        # remove old states
        newState.remove(action[1])
        newState.remove(action[0])

        # insert new states
        newState.insert(index1, action[0])
        newState.insert(index2, action[1])
        return newState

    def value(self, state):
        tripLength = 0
        for i in range(len(state)-1):
            letter1 = state[i]
            letter2 = state[i+1]

            if letter1 > letter2:
                key = letter2 + letter1
            else:
                key = letter1 + letter2

            tripLength += self.lengths[key]

        return -tripLength


# This creates an initial list of cities and the distances between them
lengths = {"AB":1, "AC":11, "AD":18, "AE":20, "AF":6, "AG":6, "AH":3, "AI":2, "AJ":15,
           "BC":1, "BD":9, "BE":7, "BF":20, "BG":1, "BH":17, "BI":13, "BJ":5,
           "CD":20, "CE":15, "CF":7, "CG":5, "CH":19, "CI":19, "CJ":1,
           "DE":3, "DF":14, "DG":20, "DH":13, "DI":7, "DJ":2,
           "EF":20, "EG":4, "EH":8, "EI":3, "EJ":5,
           "FG":18, "FH":8, "FI":12, "FJ":13,
           "GH":2, "GI":1, "GJ":1,
           "HI":14, "HJ":15,
           "IJ":18}
initial = ["A", "B", "C"]#, "D", "E"]#, "F", "G", "H", "I", "J"]
p = TSG(initial, lengths)  # Create an Abs variant problem, specifying the delta step value.
print('Initial                      x: ' + str(p.initial) + '\t\tvalue: ' + str(p.value(initial)))

startH = timer()
# Solve the problem using hill-climbing.
hill_solution = hill_climbing(p)
print('Hill-climbing solution       x: ' + str(hill_solution) + '\tvalue: ' + str(p.value(hill_solution)))
endH = timer()

startS = timer()
# Solve the problem using simulated annealing.
annealing_solution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
print('Simulated annealing solution x: ' + str(annealing_solution) + '\tvalue: ' + str(p.value(annealing_solution)))
endS = timer()

print(f"Hill Time: {endH - startH}")
print(f"Annealing Time: {endS - startS}")

'''
Introspection would not make a good model for AI to use to emulate human thought.  According to Wikipedia, introspection is “the examination of one’s conscious thoughts and feelings.”  Since computers do not possess conscious thought, they cannot use introspection to determine the validity of their thinking processes while the processes are running.  A better model would be close to the scientific method: seeing what processes generate useful results and then keeping those while tossing processes that generate bogus or useless results.  This would allow computers to evaluate a given process and continue to learn.  However, because computers cannot consciously think about a process while it is running, introspection is a poor choice to model human thought.
'''
