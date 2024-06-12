% MEMBER OF A LIST: check if an element E is into a list L
% ?- member(1, [2,3,4,1,2]).
member(E,[E|_]).
member(E,[_|T]):-member(E,T).

% COPY OF A LIST ELEMENT BY ELEMENT: copy a list L1 into a list L2 
% element by element.
% ?- copy([2,3,4,1], L).
copy([], []). %-> we do not need cut since empty list does not unify with the head H of a list
copy([H|T1], [H|T2]):-copy(T1,T2).

% APPEND A LIST INTO ANOTHER LIST: create a list X by appending a list 
% L2 into an initial list L1
% ?- append([1,2,4], [5,6,2], X).
append([], L2, L2).
append([H|T1], L2, [H|TR]):- append(T1, L2, TR).

% ADD AN ELEMENT TO A LIST
% FIRST CASE: insert the element as the first element of the list
% ?-puta([1,2,3],4, X).
puta(L, E, [E|L]).
% SECOND CASE: insert the element as the last element of the list
% ?-putz([1,2,3],4, X).
putz([], E, [E]).
putz([H|T], E, [H|T2]):- putz(T, E, T2).

% REMOVE THE FIRST OCCURRENCE OF AN ELEMENT FROM A LIST
remove(E,[E|TS], TS):-!. % -> once we find the element we copy the tail of the source list
remove(E,[HS|TS],[HS|TD]):- remove(E, TS, TD). % -> copy the head of the source list until we find the element

% REMOVE ALL THE OCCURENCES OF AN ELEMENT FROM A LIST
remove_all(_, [], []):-!.
remove_all(E, [E|TS], L):- !, remove_all(E, TS, L).
remove_all(E, [HS|TS], [HS|TD]):- remove_all(E, TS, TD).

% SUCCESSORS: find an element within a list and return the next element
succ(E, [E|[H|_]], H). %->possible red cut in the case in which we have duplicated elements
succ(E, [_|T], X):- succ(E, T, X).

% SPLIT A LIST: find an element E within a list. Then create two lists:
% in the first one the last element will be E.
% in the second one the first element will be the successor of E.
split([E|T], E, [E], T). %->possible red cut in the case in which we have duplicated elements
split([H|T], E, [H|T1], L2):- split(T, E, T1, L2).

% SUM THE ELEMENTS OF A LIST
sum([], 0).
sum([H|T], S):-sum(T,S1), S is S1 + H.

% COUNT THE ELEMENTS OF A LIST -> length
count([], 0).
count([_|T], C):-count(T,C1), C is C1 + 1.

% ALL EQUALS: check if all the elements of a list are equal. If the
% check fails, the query fails.
% IDEA: compare the first element with all the remaining
all_equals([H|T]):- equals(H,T).
equals(_,[]):- !.
equals(E,[E|T]):-equals(E,T).

% ALL DIFFERENT: check if all the elements of a list are different.
% IDEA: check all the elements with the remaining
all_different([]). 
all_different([H|T]):- different(H,T), all_different(T). 
different(_,[]):- !.
different(E,[H|T]):- not(E = H), different(E,T).













