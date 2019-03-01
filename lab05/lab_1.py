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
# From table: result = <T=0.94, F=0.06>

print('Probability of John calling if a burglary happens without an earthquake')
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=False), burglary).show_approx())
'''
For this example, given that a burglary happens, John could call after an alarm goes off or, potentially,
he could get lucky and call despite the alarm going off.  Therefore, to solve this problem, we need
the probability distribution of the alarm going off in case of a burglary and no earthquake, and the 
probability distribution of John calling given the presence of an alarm or not.

The probability distribution of John calling in this situation can be found by
adding the probability that John calls given an alarm multiplied by the probability of an
alarm given a burglary and no earthquake to the probability that John calls given no alarm multiplied by 
the probability of no alarm given a burglary and no earthquake, multiplying the whole term by the probability
of a burglary and no earthquake, and then correcting.  The remainder of the distribution, the probability
that John will not call in the event of a burglary and no earthquake, can be found by subtracting
'''

print('Probablility of a burglary if the alarm goes off')
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
'''
Look for the cases where the alarm goes off as result of a burglary as a percentage of the total cases when 
the alarm goes off.

Find the probability of a burglary given an alarm by finding the probability of an alarm given each possible
combination of burglary and earthquake, multiplying the result by the probability of each combination, and 
then dividing the sum of the probability of all cases including an alarm and a burglary by the sum of the 
probability of all cases.

Term 1 = P(alarm | burglary && earthquake) * P(burglary) * P(earthquake)
Term 2 = P(alarm | burglary && ~earthquake) * P(burglary) * P(~earthquake)
Term 3 = P(alarm | ~burglary && earthquake) * P(~burglary) * P(earthquake)
Term 4 = P(alarm | ~burglary && ~earthquake) * P(~burglary) * P(~earthquake)

P(burglary | alarm) = (Term 1 + Term 2) / (sum of all terms)
P(~burglary | alarm) = (Term 3 + Term 4) / (sum of all terms) = 1 - P(burglary | alarm)
'''

print("Probability of a burglary if John and Mary call")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
'''
This requires two cases to be covered: first, the probability that the burglary causes an alarm, and that
John and Mary call in response to that alarm.  Second, the probability of a burglary happening but no alarm
going off, and then 

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

Outside result: <F=0.716,T=0.284>
'''