from search.Problems import StreetProblem
from search.strategies import *
from search.TreeSearch import TreeSearch
from search.GraphSearch import GraphSearch
from search.Environments import *
import math

# model and load the environment

map = Roads(streets, streets_coords)
# formulate the problem
initial_state = 'Ruvo'
goal_state = 'Bari'
map_problem = StreetProblem(environment=map,
                      initial_state=initial_state,
                      goal_state=goal_state)

# search strategy (for the search tree, we do not include DepthFirst because it will cause infinite loop.
# You can try by yourself)
strategies = [AStar(map_problem), Greedy(map_problem), Random(), BreadthFirst(), DepthLimitedSearch(limit=3), UniformCost()]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=map_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    print(node.path())
    print(node.cost)

print("---------")

strategies = [AStar(map_problem), Greedy(map_problem), Random(), BreadthFirst(), DepthFirst(), DepthLimitedSearch(limit=6), UniformCost()]
for strategy in strategies:
    search = GraphSearch(problem=map_problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    print(node.path())
    print(node.cost)

