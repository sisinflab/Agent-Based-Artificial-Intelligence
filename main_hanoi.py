from search.Problems import HanoiTower
from search.strategies import *
from search.GraphSearch import GraphSearch

problem = HanoiTower(n=3)

strategies = [AStar(problem), DepthFirst()]

for strategy in strategies:
    search = GraphSearch(problem=problem, strategy=strategy)
    result, node = search.run()
    print(f'{strategy}, {search}')
    print(result)
    try:
        print(node.path())
        print(node.cost)
    except AttributeError:
        pass

print("---------")


