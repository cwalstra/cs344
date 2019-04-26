% If wood, then witch
% If floats, then made of wood
% If weighs same as duck, then floats

weighsSameAsDuck(woman).
floats(X) :- weighsSameAsDuck(X).
wood(X) :- floats(X).
witch(X) :- wood(X).