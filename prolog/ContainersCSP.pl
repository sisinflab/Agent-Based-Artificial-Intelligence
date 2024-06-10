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

% Count common elements of two lists
count_common_elements([], _, 0):-!. % Base case: an empty list has 0 common elements.
count_common_elements([H|T], List2, Count) :-
    member2(H, List2),           % Check if the head of List1 is a member of List2.
    !,
    count_common_elements(T, List2, RestCount), % Recursion with the tail of List1.
    Count is RestCount + 1.     % Increment the count if H is in List2.
count_common_elements([H|T], List2, Count) :-
    not(member2(H, List2)),        % Check if the head of List1 is not a member of List2.
    !,
    count_common_elements(T, List2, Count). % Recursion with the tail of List1, Count remains the same.

% Check if a list does not contain elements belonging to two different lists simultaneously.
% Then, we count the common elements between L1 and Container and the common elements between L2 and Container.
% At least one of these counts must be 0.
check_not_common(L1, L2, Container):-
    count_common_elements(L1, Container, 0),
    count_common_elements(L2, Container, _),
    !.
check_not_common(L1, L2, Container):-
    count_common_elements(L1, Container, _),
    count_common_elements(L2, Container, 0).

% Check if all the elements of a list are contained into another list. We should be very careful with this constraint.

% Firstly, the fact that the second list does not contain none of the elements of the first list is not a violation
% of the constraint.
all_within(L, Container, _):-
    count_common_elements(L, Container, 0).
% Second, during the search phase, not all the items belonging to the first list could already be placed into a container.
% This is not a violation of the constraint. Then, we count the common elements between the first list and the list
% of items still to be placed. If such number is greater than 0, then we move on without raising the violation of the
% constraint.
all_within(L, _, Items):-
    count_common_elements(L, Items, CLI),
    CLI > 0,
    !.
% Third, if all the items belonging to the first list are already placed into a container, the number of common elements
% between the first list and the list of items still to be placed is zero. Then we should check the satisfaction of the
% constraint. The constraint is satisfied if the number of common elements between the first list and the second list (the
% container) is equal to the length of the first list.
all_within(L, Container, Items):-
    count_common_elements(L, Items, 0),
    count(L, LL),
    count_common_elements(L, Container, LL).


constraints(NewContainer, Items):-
    % all the explosive items must be put in different containers. The idea is to count the number of common elements
    % between the explosive list and the container in examination. If the count is greater than 1, this means that
    % more than one explosive are contained into the same container, thus violating the constraint.
    explosive(Explosives),
    count_common_elements(Explosives, NewContainer, CExpl),
    CExpl < 2,
    % frozen items must be all within the same container. We exploit the count_common_elements procedure.
    frozen(Frozen),
    all_within(Frozen, NewContainer, Items),
    % trash items cannot be in the same container with a food item. We exploit the count_common_elements procedure.
    trash(Trash),
    food(Food),
    check_not_common(Trash, Food, NewContainer),
    % fresh and frozen items cannot be in the same container. We exploit the count_common_elements procedure.
    fresh(Fresh),
    check_not_common(Fresh, Frozen, NewContainer).


% Initialize containers with empty lists

% We set the head of the list of lists as an empty list. We recursively operate on the tail of the list of lists (i.e.,
% the remaining lists) until we reach the boundary condition.
% The boundary condition is reached when the counter of the number of containers is 0.
init_containers(0, []) :- !.
init_containers(N, [[]|Rest]) :-
    N1 is N - 1,
    init_containers(N1, Rest).

% Distribute items into containers --> find a candidate item to be distributed.
% The idea is to select a candidate item to be placed in any container. We pick a candidate items from the head
% of the items list. Then, we try to place it into a container through the place_item procedure. When an item is
% successfully distributed, we repeat the same operations on the remaining ones.
% In the end, the arguments of this procedure are:
% - list: Items
% - list of lists: Containers that contain the lists corresponding to each container
% - integer: MaxCapacity of container (useful to check the constraint)
% - list of lists: FinalContainers that will host the final solution
% We do not need to distribute items when all the items have been distributed. Then, the boundary condition is
% encountered when the list of Items is empty. At this point, the solution corresponds to the current containers.
distribute_items([], Containers, _, Containers).
distribute_items([Item | RestItems], Containers, MaxCapacity, FinalContainers) :-
    place_item(Item, RestItems, Containers, MaxCapacity, NewContainers),
    distribute_items(RestItems, NewContainers, MaxCapacity, FinalContainers).

% Place an item into a container --> find a candidate container to host the selected items.
% Here, we place the item to be distributed into a candidate container while respecting the constraints.
% The idea is to select a candidate container to host the selected item. We pick a candidate container from the head
% of the list of lists containing all the containers. Then, we add the item to the container.
% Then, we check if placing the items into the candidate container does not violate any constraints. If so,
% the placement is valid, and the new container is set as the head of the current list of containers.
% If a constraint is violated, the first rule within this procedure returns false. Then, we will select another
% candidate container among the remaining containers and we repeat the same procedure.
place_item(Item, RestItems, [Container | RestContainers], MaxCapacity, [NewContainer | RestContainers]) :-
    add_item(Item, Container, NewContainer),
    count(NewContainer, Length), % first constraint: check the maximum capacity of the container after adding
                                 % the item into it.
    Length =< MaxCapacity,
    constraints(NewContainer, RestItems).
place_item(Item, RestItems, [Container | RestContainers], MaxCapacity, [Container | NewRestContainers]) :-
    place_item(Item, RestItems, RestContainers, MaxCapacity, NewRestContainers).

% The query will be ?-main(4, 6, Solution).
% Within the main, we init the containers. We create a list of lists containing NumberContainers empty list.
% Then, we find the Items to be distributed within the containers.
% Finally, we start distributing the items.
main(NumberContainers, MaxCapacity, Solution):- init_containers(NumberContainers, EmptyContainers), 
                                        items(Items),
                                        distribute_items(Items, EmptyContainers, MaxCapacity, Solution).

