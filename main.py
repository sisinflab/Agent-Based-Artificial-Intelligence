from search.Problems import StreetProblem
from search.strategies import *
from search.TreeSearch import TreeSearch
from search.GraphSearch import GraphSearch
import math

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

# cities coordinates
streets_coords = {
    'Andria': (41.2316, 16.2917),
    'Corato': (41.1465, 16.4147),
    'Altamura': (40.8302, 16.5545),
    'Ruvo': (41.1146, 16.4886),
    'Terlizzi': (41.1321, 16.5461),
    'Bisceglie': (41.243, 16.5052),
    'Trani': (41.2737, 16.4162),
    'Molfetta': (41.2012, 16.5983),
    'Giovinazzo': (41.1874, 16.6682),
    'Bitonto': (41.1118, 16.6902),
    'Modugno': (41.0984, 16.7788),
    'Bari': (41.1187, 16.852)
}


class Roads:
    def __init__(self, streets, coordinates):
        self.streets = streets
        self.coordinates = coordinates

    def distance(self, start, end):
        lat_a, long_a = self.coordinates[start]
        lat_b, long_b = self.coordinates[end]
        lat_diff = abs(lat_a - lat_b)*111  # <- *111 to just convert the latitude distance in KM.
        long_diff = abs(long_a - long_b)*111 # <- *111 to just convert the longitude distance in KM.
        return math.sqrt(lat_diff**2 + long_diff**2)


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

