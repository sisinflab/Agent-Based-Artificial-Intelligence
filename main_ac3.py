from csp.problem import *
from csp.backtracking import *
from csp.ac3 import AC3

problem = MapColors()
initial_state = {}
# Example 1
print('Example 1')
problem = CSP(variables=problem.variables,
              domains=problem.domains,
              constraints=problem.constraints)
state = problem.initial_state
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)

# Example 2
print('Example 2')
problem = CSP(variables=problem.variables,
              domains=problem.domains,
              constraints=problem.constraints)
act_state = {'WA': 'red', 'Q': 'green'}
problem.domains['WA'] = ['red']
problem.domains['Q'] = ['green']
optimizer = AC3(csp=problem)
optimizer.run(state)
print(problem.domains)
