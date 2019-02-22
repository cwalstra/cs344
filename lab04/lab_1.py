'''
Find the probability of a cavity given a catch

By hand:
P(Cavity|Catch=T) = P(Cavity && Catch) / P(Catch) = (.108+.072)/(.108+.016+.072+.144) = .529
'''

'''
Copied from joint.py

This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())



P = JointProbDist(['Coin2', 'Coin1'])
T, F = True, False
P[T, T] = .25
P[T, F] = .25
P[F, T] = .25
P[F, F] = .25

coinProb = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print(coinProb.show_approx())