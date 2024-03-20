from search.Node import Node


class TreeSearch:
    """
    A class able to find a solution with a given search strategy
    """

    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []

    def __repr__(self):
        return 'Tree Search'

    def run(self):
        """
        Run the search
        :return: a path or a failure
        """

        node = Node(state=self.problem.initial_state,
                    parent=None,
                    action=None,
                    cost=0,
                    depth=0)

        # search loop
        while True:
            # check if the node passes the goal test
            if self.problem.goal_test(node.state):
                return 'Ok', node

            # expand the node
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=self.problem.cost(node.state, a)) for s, a in new_states]

            # update the fringe
            self.fringe = self.fringe + new_nodes

            # check if the search fails: empty fringe, unless the last node from the fringe contains the goal state
            # if the fringe is not empty, we pop the next node from the fringe according to the strategy
            if len(self.fringe) != 0:
                self.fringe, node = self.strategy.select(self.fringe)
                # check to manage if the fringe becomes empty within the strategy class (e.g., because of DepthLimited)
                if node is None:
                    return 'Fail', []
            else:
                if self.problem.goal_test(node.state):
                    return 'Ok', node
                else:
                    return 'Fail', []

