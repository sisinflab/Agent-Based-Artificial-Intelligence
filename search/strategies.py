import random


class Random:
    def __repr__(self):
        return 'Random strategy'

    @staticmethod
    def select(fringe):
        random.shuffle(fringe)
        node = fringe.pop(0)
        return fringe, node


class BreadthFirst:
    def __repr__(self):
        return 'Breadth First strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop(0)
        return fringe, node


class DepthFirst:
    def __repr__(self):
        return 'Depth First strategy'

    @staticmethod
    def select(fringe):
        node = fringe.pop()
        return fringe, node


class UniformCost:
    def __repr__(self):
        return 'Uniform Cost strategy'

    @staticmethod
    def select(fringe):
        fringe = sorted(fringe, key=lambda x: x.cost)
        node = fringe.pop(0)
        return fringe, node


class DepthLimitedSearch:
    def __init__(self, limit):
        self.limit = limit

    def __repr__(self):
        return 'Depth First Limited strategy'

    def select(self, fringe):
        fringe = [n for n in fringe if n.depth <= self.limit]
        try:
            node = fringe.pop()
        except IndexError:
            return [], None
        return fringe, node


class Greedy:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'Greedy strategy'

    def select(self, fringe):
        # sort fringe following the evaluation function
        fringe = sorted(fringe, key=lambda x: self.problem.h(x.state))
        node = fringe.pop(0)
        return fringe, node


class AStar:
    def __init__(self, problem):
        self.problem = problem

    def __repr__(self):
        return 'AStar strategy'

    def select(self, fringe):
        # sort fringe following the evaluation function
        fringe = sorted(fringe, key=lambda x: (self.problem.h(x.state)+x.cost))
        node = fringe.pop(0)
        return fringe, node
