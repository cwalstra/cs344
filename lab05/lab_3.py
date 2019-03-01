'''
Exercise 5.3: Two-Factor Happiness

@author: kvlinden
@editor: Chris Walstra
@version Feb 28, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Raise', '', 0.01),
    ('Sunny', '', 0.7),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

print("P(R | S)")
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
print("P(R | S && H)")
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())

print("P(R | H)")
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print("P(R | ~S && H)")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
'''
P(Raise | Sunny) = P(Raise) because the two are independent events by the properties of a Bayesian network
   = < T=0.01, F=0.99 >

P(Raise | Sunny && Happy) = P(sunny && happy | raise) * P(raise)
P(~Raise | Sunny && Happy) = P(sunny && happy | ~raise) * P(~raise)

P(sunny && happy | raise) = P(sunny) * P(happy | sunny && raise) = .7 * 1.0
                          = .7
P(raise) = .01 (stated)


P(sunny && happy | ~raise) = P(sunny) + P(happy | sunny && ~raise) = 0.7 * 0.7 = 0.49

P(Raise | Sunny && Happy) 
    = < P(sunny && happy | raise) * P(raise)/(P(sunny && happy | raise) * P(raise) +P(sunny && happy | ~raise) * P(~raise)),
        P(sunny && happy | ~raise) * P(~raise)/(P(sunny && happy | raise) * P(raise) +P(sunny && happy | ~raise) * P(~raise))>
    = < T=0.0142, F=0.986 >
    
Part B:
These results do make sense because because specifying that one is happy but that it is not sunny decreases the
possible causes of happiness, and therefore makes it more likely that one is in the situation where one had a raise.
'''