% 1.
%    Exercise 3.2
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).

% The first three lines establish which dolls are directly inside another.
% The fourth line establishes that doll x being directly inside doll y means that doll x is in doll y.
% The fifth line establishes that a doll x is inside another doll y if x is directly in a third doll z and doll z is
% in doll y.

%    Exercise 4.5

% listtran([], []).
% listtran([X|G], [Y|E]) :- listtran(G, E), trans(X, Y).

% The first line establishes that the translation of an empty list is an empty list.
% The second line establishes that, if the head of the German list is a translation of the head of the English list, and
% listtran(German, English) succeeds for all the remaining elements in the lists, the query succeeds.

% To complete this query, prolog pulls an element from a list and checks the remaining list.  This repeats until it hits
% the base case, a pair of empty lists.  It then builds a new list, adding the translation of the last element removed
% until the list matches, causing the query to succeed.

% 2.

% Prolog does implement a general version of modus ponens, using the form shown below.
% consequence(X, Y) :- statement(X, Y).