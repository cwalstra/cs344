'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@editor: Chris Walstra
@version Feb 28, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
])


print("Probability of the alarm going off if a burglary but no earthquake occurs")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=False), burglary).show_approx())
# Can be found by reading from the table

print('Probability of John calling if a burglary happens without an earthquake')
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=False), burglary).show_approx())
'''
Can be found by adding the probability that John calls given an alarm multiplied by the probability of an
alarm given a burglary and no earthquake to the probability that John calls given no alarm multiplied by 
the probability of no alarm given a burglary and no earthquake, multiplying the whole term by the probability
of a burglary and no earthquake, and then correcting

<add method explanation>
'''

print('Probablility of a burglary if the alarm goes off')
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
'''
Term 1 = P(alarm | burglary && earthquake) * P(burglary) * P(earthquake)
Term 2 = P(alarm | burglary && ~earthquake) * P(burglary) * P(~earthquake)
Term 3 = P(alarm | ~burglary && earthquake) * P(~burglary) * P(earthquake)
Term 4 = P(alarm | ~burglary && ~earthquake) * P(~burglary) * P(~earthquake)

P(burglary | alarm) = Term 1 + Term 2
P(~burglary | alarm) = Term 3 + Term 4 = 1 - P(burglary | alarm)
'''

print("Probability of a burglary if John and Mary call")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
'''
P(burglary | johnCalls && maryCalls) = 
    P(burglary|alarm) * P(alarm | johnCalls && maryCalls) + P(burglary | ~alarm) * P(~alarm | johnCalls && maryCalls)
P(~burglary | johnCalls && maryCalls) = 1 - P(burglary | johnCalls && maryCalls)

Find P(burglary | alarm) as shown above
Find P(burglary | ~alarm) by replacing P(alarm | some condition) in the formula with P(~alarm | same condition)
    and then adding the same terms
    
P(alarm | johnCalls && maryCalls) = P(johnCalls && maryCalls | alarm) * P(alarm)/P(johnCalls && maryCalls)
    = (.9 * .7) * P(a) / ((.9*P(a) + .05(1 - P9a))*(.7*P(a) + .01(1-P(a)))
    Find P(alarm) = P(a) using probability of earthquakes and burglaries and an alarm going off given these things
P(~alarm | johnCalls && maryCalls) = 1 - P(alarm | johnCalls && maryCalls)
'''