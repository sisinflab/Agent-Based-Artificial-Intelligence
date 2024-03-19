class Node:
    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    def __repr__(self):
        """
        A representation of the class. Useful with functions like print.
        :return: a string
        """
        return f'({self.state})'

    def expand(self, state, action, cost=1):
        """
        Given a new state returns a child tree node containing that state
        :param new_state: state that will be contained by the node
        :param action: action that led to the state
        :param cost: cost of the path of the previous node
        :return: a child node
        """
        return Node(state=state,
                    parent=self,
                    action=action,
                    cost=self.cost+cost,
                    depth=self.depth+1)

    def path(self):
        """
         Returns the path from the root node to the actual node
        :return: a list of actions
        """
        path = []
        node = self
        while node.parent:
            path.append(node.action)
            node = node.parent
        path = list(reversed(path))
        return path
