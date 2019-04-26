a.
Exercise 1.4
1. killer(Butch) - This states that Butch has the property killer.
2. married(Mia, Marsellus) - This links Mia and Marsellus with the property married
3. dead(Zed) - Zed has the property dead
4. kills(Marsellus, X):- footMassageMia(X) - The second part assigns a name to X if the person with that name gives Mia
   a foot massage.  The operator indicates that the first part is the case if the second is.  The first part indicates
   that Marsellus will kill the person whose name is stored in X.
5. loves(Mia, X) :- goodDancer(X) - The second part assigns a name to X if the person with that name has the property
   goodDancer.  The operator indicates that the first part is the case if the second is.  The first part indicates
   that Mia loves the person with name X.
6. julesEats(X) :- tasty(X);nutritious(X) - The second part checks if something is tasty or nutritious.    The operator
   indicates that the first part is the case if something is tasty or nutritious.  The first part indicates that
   Jules will eat item X if the conditional laid out in the second half of the statement is true.

Exercise 1.5
1. yes - this comes from stated fact in the first line
2. no - no property witch known to prolog
3. no - hermoine is unknown to prolog
4. no - witch and hermoine are unknown to prolog,
5. yes - Prolog deduces this because harry hasWand (line 2) and is quidditchPlayer (line 3).  The latter means that he
   hasBroom (line 5), and because he hasWand and hasBroom, wizard(harry) must be true (line 4).
6. X = ron - prolog returns the first possible value it finds for X, in this case ron, since wizard is established as a
   property of ron in line 1.
7. no - since witch is not a known property to prolog, it cannot unify X to any value, and thus returns no