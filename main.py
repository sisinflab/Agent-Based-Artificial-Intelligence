from src.Problems import StreetProblem
from src.strategies import *
from src.TreeSearch import TreeSearch
from src.GraphSearch import GraphSearch

# model and load the environment
streets = {
    'Andria': ['Corato', 'Trani'],
    'Corato': ['Ruvo', 'Trani', 'Andria', 'Altamura'],
    'Altamura': ['Corato', 'Ruvo', 'Modugno'],
    'Ruvo': ['Corato', 'Bisceglie', 'Terlizzi', 'Altamura'],
    'Terlizzi': ['Ruvo', 'Molfetta', 'Bitonto'],
    'Bisceglie': ['Trani', 'Ruvo', 'Molfetta'],
    'Trani': ['Andria', 'Corato', 'Bisceglie'],
    'Molfetta': ['Bisceglie', 'Giovinazzo', 'Terlizzi'],
    'Giovinazzo': ['Molfetta', 'Modugno', 'Bari', 'Bitonto'],
    'Bitonto': [ 'Modugno', 'Giovinazzo', 'Terlizzi'],
    'Modugno': ['Bitonto', 'Giovinazzo', 'Bari', 'Altamura'],
    'Bari': ['Modugno', 'Giovinazzo']
}

# formulate the problem
initial_state = 'Ruvo'
goal_state = 'Bari'
map_problem = StreetProblem(environment=streets,
                      initial_state=initial_state,
                      goal_state=goal_state)

# search strategy (for the search tree, we do not include DepthFirst because it will cause infinite loop.
# You can try by yourself)
strategies = [Random(), BreadthFirst(), DepthLimitedSearch(limit=3), UniformCost()]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=map_problem, strategy=strategy)
    result, path = search.run()
    print(f'{strategy}, {search}')
    print(result)
    print(path)

print("---------")

strategies = [Random(), BreadthFirst(), DepthFirst(), DepthLimitedSearch(limit=3), UniformCost()]
for strategy in strategies:
    search = GraphSearch(problem=map_problem, strategy=strategy)
    result, path = search.run()
    print(f'{strategy}, {search}')
    print(result)
    print(path)

