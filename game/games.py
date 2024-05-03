# let's build the skeleton of our game class
class Game:
    def __init__(self, initial_state, player):
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        return []

    def result(self, state, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        return []

    def successors(self, state):
        """
        Given a state returns the reachable states with the respective actions
        :param state: actual state
        :return: list of successor states and actions
        """
        possible_actions = self.actions(state)
        return [(self.result(state, a), a) for a in possible_actions]

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value
        """
        return 0

    def player_utility(self, state):
        """
        Given a state, returns the utility of the state from the view of the MAX or the MIN player
        @param state: a state
        @return: a utility value
        """
        if self.player == 'MAX':
            # for MAX player
            return self.utility(state)
        elif self.player == 'MIN':
            # for MIN player
            return -self.utility(state)
        else:
            raise ValueError

    def next_player(self):
        """
        Return the next player to move
        @return: MAX or MIN
        """
        if self.player == 'MAX':
            return 'MIN'
        else:
            return 'MAX'

    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                self.display(state)
                move = player.next_move(state)
                state = self.result(state, move)
                self.display_move(state, move)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        print(self.player, 'in ', state)

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)


# let's populate the skeleton with our dummy game
class DummyGame(Game):
    def __init__(self, initial_state=None, player='MAX'):
        if initial_state is None:
            initial_state = 'A'
        super(DummyGame, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        actions = {
            'A': ['a1', 'a2', 'a3'],
            'B': ['b1', 'b2', 'b3'],
            'C': ['c1', 'c2', 'c3'],
            'D': ['d1', 'd2', 'd3'],
        }
        if state in actions:
            return actions[state]
        else:
            return []

    def result(self, state, action):
        """
        Given a state and an action returns the reached state
        @param state: a state of the game
        @param action: a possible action in the state
        @return: a new state
        """
        result = {
            'A': {
                'a1': 'B',
                'a2': 'C',
                'a3': 'D'},
            'B': {
                'b1': 'B1',
                'b2': 'B2',
                'b3': 'B3'},
            'C': {
                'c1': 'C1',
                'c2': 'C2',
                'c3': 'C3'},
            'D': {
                'd1': 'D1',
                'd2': 'D2',
                'd3': 'D3'},
        }
        return result[state][action]

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        if state in ('B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3'):
            return True
        else:
            return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        utility = {'B1': 3,
                   'B2': 12,
                   'B3': 8,
                   'C1': 2,
                   'C2': 4,
                   'C3': 6,
                   'D1': 14,
                   'D2': 5,
                   'D3': 2}
        return utility[state]

