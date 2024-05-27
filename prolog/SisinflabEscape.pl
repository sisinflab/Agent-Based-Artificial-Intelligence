people([claudio,walter,felice,antonio]).
time(antonio,40).
time(claudio,80).
time(felice,100).
time(walter,20).

couple(antonio,felice).
couple(antonio,walter).
couple(antonio,claudio).

couple(felice,walter).
couple(claudio,felice).
couple(claudio,walter).

battery(240).

max(X,Y,Y):- X=<Y, !.
max(X,Y,X):- X>Y.
puta(List,E,NewList):- NewList=[E|List].

remove(E,[E|T1],T1):- !.
remove(E,[A|B],[A|D]):- remove(E,B,D).

member2(E,[E|_]):- !.
member2(X,[_|T]):- member2(X,T).

putz([],E,[E]):- !.
putz([H|T1],E,[H|T2]):-putz(T1,E,T2).

updatesolution(A,B,C):- puta(['forward'],A,D), puta(D,B,C).
updatesolution(A,B):- puta(['backward'],A,B).

% FORWARD: in the forward move we save people! Then, we find a couple of not saved people. We compute the maximum time they need to overcome the traps.
% We update the status of the battery checking wether the smartphone has enough battery. If the previous clauses success, we put the couple among the
% saved people. We update the temporary solution.

forward(RBattery, Notsaved, Saved, TempSolution,RBattery2,Saved3,Notsaved3,TempSolution2):- couple(X,Y),member2(X,Notsaved),member2(Y,Notsaved),time(X,Tx),time(Y,Ty),max(Tx,Ty,M),RBattery2 is RBattery - M, RBattery2 >= 0, puta(Saved,X,Saved2),puta(Saved2,Y,Saved3), remove(X,Notsaved,Notsaved2), remove(Y,Notsaved2,Notsaved3),updatesolution(X,Y,ListResult),putz(TempSolution,ListResult,TempSolution2).

% BACKWARD: in the backward move we put people in trouble! Then, we find a candidate person to go backward. We update the status of the battery checking
% wether the smartphone  has enough battery, If the previous clauses success, we put the candidate person among the not saved people by removing him/her
% from the saved people. We update the temporary solution.

backward(RBattery, Saved, Notsaved,TempSolution,RBattery2,Notsaved3,Saved3,TempSolution2):- time(X,Tx), member2(X,Saved), RBattery2 is RBattery - Tx, RBattery2 >=0, remove(X,Saved,Saved3), puta(Notsaved,X,Notsaved3), updatesolution(X,ListResult), putz(TempSolution,ListResult,TempSolution2).

% MOVE: we have two possible cases for a move:
% 1. after the forward step, we still have not saved people! We perform the backward step.
% 2. after the forward step, all people are saved. We have a solution!
move(RBattery, Notsaved, Saved, TempSolution, RBatterySol, Solution):- forward(RBattery, Notsaved, Saved, TempSolution, RBattery2, Saved2, Notsaved2, TempSolution2), not(Notsaved2 = []), backward(RBattery2,Saved2,Notsaved2,TempSolution2, RBattery3,Notsaved3,Saved3,TempSolution3), move(RBattery3,Notsaved3,Saved3,TempSolution3,RBatterySol,Solution).
move(RBattery, Notsaved, Saved, TempSolution, RBattery2, TempSolution2):- forward(RBattery,Notsaved,Saved, TempSolution, RBattery2, _, Notsaved2,TempSolution2), Notsaved2 = []. 

% The query will be ?-main(Time, Solution).
main(RBattery, Solution):- battery(Battery), people(People), !, move(Battery, People, [], _, RBattery, Solution). % initially, the list of saved people is empty.

% HOMEWORK: Complete the task without explicitly declaring couples. Why do the results seem to be "different"?