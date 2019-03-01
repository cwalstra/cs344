'''
Exercise 5.2: Cancer Testing

@author: kvlinden
@editor: Chris Walstra
@version Feb 28, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

testing = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

print("P(C | T1 && T2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), testing).show_approx())
print("P(C | T1 && ~T2)")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), testing).show_approx())


'''
P(cancer | test1 && test2)
    = P(test1 && test2 | cancer) * P(cancer) / (P(test1 && test2 | cancer) * P(cancer) + P(test1 && test2 | ~cancer) * P(~cancer))
    = (.9 * .9) * .01 / (0.9*0.9*0.01 + 0.2*0.2*0.99)
    = 0.17
P(~cancer | test1 && test2) 
    = P(test1 && test2 | ~cancer) * P(~cancer) / (P(test1 && test2 | cancer) * P(cancer) + P(test1 && test2 | ~cancer) * P(~cancer))
    = (.2 * .2) * .99 / (0.9*0.9*0.01 + 0.2*0.2*0.99)
    = 0.83

P(C | T1 ^ T2) = <P(cancer | test1 && test2), P(~cancer | test1 && test2)> = <0.17, 0.83>

P(cancer | test1 && ~test2) 
    = P(test1 && ~test2 | cancer) * P(cancer) / (P(test1 && ~test2 | cancer) * P(cancer) + P(test1 && ~test2 | ~cancer) * P(~cancer))
    = (.9 * .1) * .01 / (0.9*0.1*0.01 + 0.2*0.8*0.99)
    = 0.00565
P(~cancer | test1 && test2) = P(test1 && test2 | ~cancer) * P(~cancer) / P(test1 && ~test2)
    = (.2 * .8) * .99 / (0.9*0.1*0.01 + 0.2*0.8*0.99)
    = 0.994
    
P(C | T1 ^ ~T2) = <P(cancer | test1 && ~test2), P(~cancer | test1 && ~test2)> = <0.00565, 0.994>


These results do make sense because the probability of having cancer is very low and the probability
of a false positive is quite large, leaving open possibility of more false positives than true positives.

Although it is not likely that one has cancer even if both tests indicate the presence of cancer,
having one test show the presence of no cancer reduces the odds of cancer by a factor of 34, reducing
the odds from 17% to about 0.5%.
'''