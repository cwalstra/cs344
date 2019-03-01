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

P(Raise | Sunny && Happy) = P(sunny && happy | raise) * P(raise)
P(~Raise | Sunny && Happy) = P(sunny && happy | ~raise) * P(~raise)

P(sunny && happy | raise) = P(sun) * P(happy| sunny && raise) 
                          = .7
P(raise) = .01
P(sunny && happy) = P(sunny)*P(raise)*P(happy|sunny&&raise) + P(sunny)*P(~raise)*P(happy|sunny&&~raise)
                  = .4921



'''