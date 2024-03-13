import random


class Random:
    def __repr__(self):
        return 'Random strategy'

    @staticmethod
    def select(fringe, new_nodes):
        fringe = fringe + new_nodes
        random.shuffle(fringe)
        node = fringe.pop(0)
        return fringe, node


class BreadthFirst:
    def __repr__(self):
        return 'Breadth First strategy'

    @staticmethod
    def select(fringe, new_nodes):
        fringe = fringe + new_nodes
        node = fringe.pop(0)
        return fringe, node


class DepthFirst:
    def __repr__(self):
        return 'Depth First strategy'

    @staticmethod
    def select(fringe, new_nodes):
        fringe = fringe + new_nodes
        node = fringe.pop()
        return fringe, node


class UniformCost:
    def __repr__(self):
        return 'Uniform Cost strategy'

    @staticmethod
    def select(fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = sorted(fringe, key=lambda x: x.cost)
        node = fringe.pop(0)
        return fringe, node


class DepthLimitedSearch:
    def __init__(self, limit):
        self.limit = limit

    def __repr__(self):
        return 'Depth First Limited strategy'

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.depth <= self.limit]
        node = fringe.pop()
        return fringe, node

