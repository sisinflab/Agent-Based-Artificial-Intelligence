from csp.problem import *
from csp.backtracking import *

problem = MapColors()
initial_state = {}

search = BackTracking(problem=problem,
                      var_criterion=random_variable,
                      value_criterion=random_assignment)

print(f'{search}, Random strategies')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=minimum_remaining_values,
                      value_criterion=least_constraining_value)

print(f'{search}, Minimum Remaining Values, Least Constraining Value')
print(search.run(initial_state))

search = BackTracking(problem=problem,
                      var_criterion=degree_heuristic,
                      value_criterion=least_constraining_value)

print(f'{search},Degree Heuristic, Least Constraining Value')
print(search.run(initial_state))

print(f'{search},Forward Checking, Degree Heuristic, Least Constraining Value')
print(search.run_with_forward_checking(initial_state, problem.domains))
