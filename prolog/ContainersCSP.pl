items([t1, t2, t3, t4, t5, f1, f2, f3, e1, e2, fz1, fz2, fz3, fs1]).
trash([t1, t2, t3, t4, t5]).
food([f1, f2, f3]).
explosive([e1, e2]).
frozen([fz1, fz2, fz3]).
fresh([fs1]).

count([],0):- !. 
count([_|T],X):- count(T,X2), X is X2+1.

remove(E,[E|T1],T1):- !.
remove(E,[A|B],[A|D]):- remove(E,B,D).

member2(E,[E|_]):- !.
member2(X,[_|T]):- member2(X,T).

add_item(Item, Container, [Item | Container]).

count_common_elements([], _, 0):-!. % Base case: an empty list has 0 common elements.
count_common_elements([H|T], List2, Count) :-
    member(H, List2),           % Check if the head of List1 is a member of List2.
    !,
    count_common_elements(T, List2, RestCount), % Recursion with the tail of List1.
    Count is RestCount + 1.     % Increment the count if H is in List2.
count_common_elements([H|T], List2, Count) :-
    not(member(H, List2)),        % Check if the head of List1 is not a member of List2.
    !,
    count_common_elements(T, List2, Count). % Recursion with the tail of List1, Count remains the same.

check_not_common(L1, L2, Container):-
    count_common_elements(L1, Container, 0),
    count_common_elements(L2, Container, _),
    !.
check_not_common(L1, L2, Container):-
    count_common_elements(L1, Container, _),
    count_common_elements(L2, Container, 0).


all_within(L, Container, _):-
    count_common_elements(L, Container, 0).
all_within(L, _, Items):-
    count_common_elements(L, Items, CLI),
    CLI > 0,
    !.
all_within(L, Container, Items):-
    count_common_elements(L, Items, 0),
    count(L, LL),
    count_common_elements(L, Container, LL).


constraints(NewContainer, Items):-
    explosive(Explosives),
    count_common_elements(Explosives, NewContainer, CExpl),
    CExpl < 2,
    frozen(Frozen),
    all_within(Frozen, NewContainer, Items),
    trash(Trash),
    food(Food),
    check_not_common(Trash, Food, NewContainer),
    fresh(Fresh),
    check_not_common(Fresh, Frozen, NewContainer).


% Initialize containers with empty lists
init_containers(0, []) :- !.
init_containers(N, [[]|Rest]) :-
    N1 is N - 1,
    init_containers(N1, Rest).

% Distribute items into containers
distribute_items([], Containers, _, Containers).
distribute_items([Item | RestItems], Containers, MaxCapacity, FinalContainers) :-
    place_item(Item, RestItems, Containers, MaxCapacity, NewContainers),
    distribute_items(RestItems, NewContainers, MaxCapacity, FinalContainers).

% Place an item into a container while respecting the constraints
place_item(Item, RestItems, [Container | RestContainers], MaxCapacity, [NewContainer | RestContainers]) :-
    add_item(Item, Container, NewContainer),
    count(NewContainer, Length),
    Length =< MaxCapacity,
    constraints(NewContainer, RestItems).
place_item(Item, RestItems, [Container | RestContainers], MaxCapacity, [Container | NewRestContainers]) :-
    place_item(Item, RestItems, RestContainers, MaxCapacity, NewRestContainers).

main(NumberContainers, MaxCapacity, Solution):- init_containers(NumberContainers, EmptyContainers), 
                                        items(Items), !,
                                        distribute_items(Items, EmptyContainers, MaxCapacity, Solution).

