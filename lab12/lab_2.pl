house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

% a.
% Exercise 2.1
% 1. This pair unifies because they are the same atom.
% 2. This pair will not unify because Prolog is case-sensitive, and the capital B in 'Bread' makes it a different atom
%    than bread.
% 8. successful unification, X = bread
% 9. successful unificationm, Y = bread, X = sausage
% 14. unification fails, since X would need to take on two different values to unify the statements.

% Exercise 2.2
% 1. This query is satisfied.
% 2. This query is not satisfied, since Prolog does not know the atom harry.
% 3. This query is satisfied by line 6.
% 4. This query is satisfied by combination of lines 3 and 7, X instantiates as 'McGonagall'.
% 5. This query is not satisfied.  Prolog does not know the atom Hermoine.  Also, Hermoine is not a legal atom.

% b.
% Unification is used in propositional logic to simplify some expressions, e.g. {a = a}.

% c.
% Prolog uses resolution because it can do modus ponens, a special case of resolution (wikipedia).