import math


class StreetProblem:

    def __init__(self, initial_state, goal_state, environment):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.environment = environment

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def actions(self, state):
        """
        Given a state returns the list of possible actions
        :param state: actual state
        :return: a list of actions
        """
        return self.environment.streets[state]

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        return action

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return state == self.goal_state

    def cost(self, state, action):
        """
        Given a state and an action returns the cost of the action
        :param state: a state
        :param action: an action
        :return: the cost of doing that action in that state
        """
        reached_state = self.result(state, action)
        return self.environment.distance(state, reached_state)

    def h(self, state):
        # goal_x, goal_y = self.environment.coordinates[self.goal_state]
        # x, y = self.environment.coordinates[state]
        # return math.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2)
        lat_a, long_a = self.environment.coordinates[state]
        lat_b, long_b = self.environment.coordinates[self.goal_state]
        lat_diff = abs(lat_a - lat_b) * 111  # <- *111 to just convert the latitude distance in KM.
        long_diff = abs(long_a - long_b) * 111  # <- *111 to just convert the longitude distance in KM.
        return math.sqrt(lat_diff ** 2 + long_diff ** 2)
