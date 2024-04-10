import math
import random


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
        lat_a, long_a = self.environment.coordinates[state]
        lat_b, long_b = self.environment.coordinates[self.goal_state]
        lat_diff = abs(lat_a - lat_b) * 111  # <- *111 to just convert the latitude distance in KM.
        long_diff = abs(long_a - long_b) * 111  # <- *111 to just convert the longitude distance in KM.
        return math.sqrt(lat_diff ** 2 + long_diff ** 2)


class MazeProblem:

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
        actionList = ['up', 'down', 'left', 'right']

        # managing maze borders
        if state[0] == 0:
            actionList.remove("up")

        if state[0] == self.environment.height - 1:
            actionList.remove("down")

        if state[1] == 0:
            actionList.remove("left")

        if state[1] == self.environment.width - 1:
            actionList.remove("right")

        for i in range(self.environment.n_walls):
            if (state[0] - 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("up")
            if (state[0] + 1, state[1]) == self.environment.p_walls[i]:
                actionList.remove("down")
            if (state[0], state[1] - 1) == self.environment.p_walls[i]:
                actionList.remove("left")
            if (state[0], state[1] + 1) == self.environment.p_walls[i]:
                actionList.remove("right")

        return actionList

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        if action == 'up':
            reached_state = (state[0] - 1, state[1])
        if action == 'down':
            reached_state = (state[0] + 1, state[1])
        if action == 'left':
            reached_state = (state[0], state[1] - 1)
        if action == 'right':
            reached_state = (state[0], state[1] + 1)
        return reached_state

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
        return 1

    def h(self, state):
        return abs(self.goal_state[0] - state[0]) + abs(self.goal_state[1] - state[1])


class EightQueensProblem:

    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = self.random()
        self.initial_state = initial_state
        self.max_conflicts = sum([i for i in range(1, 8)])

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
        actions = []
        for col, queen in enumerate(state):
            squares = list(range(0, 8))
            squares.remove(queen)
            # new_actions = list(zip(squares, [col]*len(squares)))
            new_actions = list(zip([col] * len(squares), squares))
            actions.extend(new_actions)
        return actions

    def result(self, state=None, action=None):
        """
        Given a state and an action returns the reached state
        :param state: actual state
        :param action: chosen action
        :return: reached state
        """
        new_state = list(state)
        col, new_row = action
        new_state[col] = new_row
        return tuple(new_state)

    def conflicts(self, state):
        """
        Given a state return the number of conflicts
        :param state: a state
        :return: number of conflicting queens
        """
        conflicts = 0
        for col in range(8):
            queen = state[col]
            for col1 in range(col+1, 8):
                queen1 = state[col1]
                if queen == queen1:
                    conflicts += 1
                if queen - col == queen1 - col1 or queen + col == queen1 + col1:
                    conflicts += 1
        return conflicts

    def goal_test(self, state):
        """
        Checks if the goal condition has been reached
        :param state: actual state
        :return: True if the goal condition is matched, False otherwise
        """
        return self.conflicts(state) == 0

    def cost(self, state, action):
        """
        Returns the cost of an action. In this problem the cost is always unitary.
        :param state: a state
        :param action: an action
        :return: a cost
        """
        return 1

    def value(self, state):
        """
        Returns the value of a state. This function is used for evaluating a state in the local search.
        (The higher the better)
        :param state: a state
        :return: the value of a state
        """
        return self.max_conflicts - self.conflicts(state)

    @staticmethod
    def random():
        """
        Generate a random chess with 8 queens
        :return: a tuple with 8 elements
        """
        chess = [random.randrange(0, 8) for _ in range(8)]
        return tuple(chess)

    @staticmethod
    def print_chess(state):
        print('\t', end='')
        for number in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"|  {number}  ", end='')
        print('|', end='')
        print('\n\t_________________________________________________')

        for row, letter in zip(range(8), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
            print(letter + '\t', end='')
            print('|', end='')

            for queen in state:
                if queen == row:
                    print('  Q  ', end='')
                else:
                    print('     ', end='')
                print('|', end='')
            print('\n', end='')
            print('\t_________________________________________________')

