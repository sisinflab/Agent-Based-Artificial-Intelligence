from src.Node import Node


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
                return 'Ok', node.path()

            # expand the node
            new_states = self.problem.successors(node.state)
            new_nodes = [node.expand(state=s,
                                     action=a,
                                     cost=1) for s, a in new_states]

            # a solution was not found, update the fringe and pick the next node coherently with the search strategy
            self.fringe, node = self.strategy.select(self.fringe, new_nodes)

            # Check if the search fails (empty fringe)
            if len(self.fringe) == 0:
                return 'Fail', []
