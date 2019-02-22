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
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())




'''
Answers to 4.2 part a and b
a. 
i.   With rain included, the joint probability distribution contains 16 entries.
ii.  The probabilities should still sum to one as long as the variables cover all possible scenarios
iii. It is possible to use more than just true and false for a probability distribution.  For example,
     if choosing a random location on the American flag, the possible states are red, white, and blue,
     each with a certain probability of being chosen randomly.  As long as every possible state is 
     covered, and the probabilities add to one, states beyond true and false are possible.
iv.  The probabilities that I chose indicate that the value of Rain is independent of the original values
     because the conditional probabilities, e.g. P(Cavity|Catch), are the same for both rain and not rain.
     
b. 
P(Toothache | rain) = P(Toothache && rain)/P(rain) = 
    (.054 + .008 + .032 + .006)/(.054 + .008 + .032 + .006 + .036 + .072 + .288 + .004) =
    = 0.2
    
AIMA result = .2
'''
