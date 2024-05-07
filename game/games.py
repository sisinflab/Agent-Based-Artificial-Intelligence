import numpy as np
import random
import itertools


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


class TicTacToe(Game):
    def __init__(self, initial_state=None, height=3, width=3, player='MAX'):
        self.height = height
        self.width = width
        if initial_state is None:
            initial_state = self.init_state()
        super(TicTacToe, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.squares = self.height * self.width
        self.empty = '.'
        self.X = 'X'
        self.O = 'O'

    @staticmethod
    def init_state():
        state = {'cells': [], 'to_move': 'MAX', 'max_cells': [], 'min_cells': []}
        # state['board'] = []
        return state

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        action_list = [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in state['cells']]
        return action_list

    def result(self, state, action):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()
        copy_state['to_move'] = state['to_move']
        if copy_state['to_move'] == 'MAX':
            copy_state['max_cells'].insert(0, action)
            copy_state['cells'].insert(0, action)
            copy_state['to_move'] = 'MIN'
            return copy_state
        elif copy_state['to_move'] == 'MIN':
            copy_state['min_cells'].insert(0, action)
            copy_state['cells'].insert(0, action)
            copy_state['to_move'] = 'MAX'
            return copy_state
        else:
            raise ValueError

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        # squares = sum([len(v) for k, v in state.items() if k != 'to_move'])
        if self.utility(state) != 0 or len(state['cells']) == self.squares:
            return True
        else:
            return False

    def utility(self, state):
        # vertical case
        for i in range(self.width):
            if len([el for el in state['max_cells'] if i == el[0]]) == 3:
                return 1
            if len([el for el in state['min_cells'] if i == el[0]]) == 3:
                return -1

        # horizontal case
        for j in range(self.height):
            if len([el for el in state['max_cells'] if j == el[1]]) == 3:
                return 1
            if len([el for el in state['min_cells'] if j == el[1]]) == 3:
                return -1

        # diagonal case
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        temp1.append([el for el in state['max_cells'] if el in [(0, 0), (1, 1), (2, 2)]])
        temp2.append([el for el in state['min_cells'] if el in [(0, 0), (1, 1), (2, 2)]])
        if len(temp1[0]) == 3:
            return 1
        if len(temp2[0]) == 3:
            return -1
        temp3.append([el for el in state['max_cells'] if el in [(0, 2), (1, 1), (2, 0)]])
        temp4.append([el for el in state['min_cells'] if el in [(0, 2), (1, 1), (2, 0)]])
        if len(temp3[0]) == 3:
            return 1
        if len(temp4[0]) == 3:
            return -1
        return 0

    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    if self.utility(state) == 0:
                        print("IT'S A DRAW! \n\n")
                    elif self.utility(state) == 1:
                        print("MAX WINS! \n\n")
                    elif self.utility(state) == -1:
                        print("MIN WINS! \n\n")
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.width):
            print(column, '\t\t', end='')
        print()
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        for i in range(0, self.height):
            print(i, end='')
            for j in range(0, self.width):
                if (i, j) in state['max_cells']:
                    print('\t{}\t|'.format(self.X), end=" ")
                elif (i, j) in state['min_cells']:
                    print('\t{}\t|'.format(self.O), end=" ")
                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()


class ConnectFour(Game):
    def __init__(self, initial_state=None, height=6, width=7, player='MAX'):
        self.height = height
        self.width = width
        if initial_state is None:
            initial_state = self.init_state()
        super(ConnectFour, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.squares = self.height * self.width
        self.empty = '.'

    def init_state(self):
        state = {i: [] for i in range(self.width)}
        # state['board'] = []
        state['to_move'] = 'MAX'
        return state

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        action_list = [k for k, v in state.items() if len(v) < self.height and k != 'to_move']
        return action_list

    def result(self, state, action):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()
        copy_state['to_move'] = state['to_move']
        if copy_state['to_move'] == 'MAX':
            copy_state[action].insert(0, 'MAX')
            copy_state['to_move'] = 'MIN'
            return copy_state
        elif copy_state['to_move'] == 'MIN':
            copy_state[action].insert(0, 'MIN')
            copy_state['to_move'] = 'MAX'
            return copy_state
        else:
            raise ValueError

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        squares = sum([len(v) for k, v in state.items() if k != 'to_move'])
        if abs(self.utility(state)) == 1000000 or squares == self.squares:
            return True
        else:
            return False

    def utility(self, state):
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        max_twos = 0
        max_threes = 0
        max_fours = 0
        min_twos = 0
        min_threes = 0
        min_fours = 0

        # vertical case
        for k, v in copy_state.items():
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(v)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(v)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1

        # horizontal case
        temp = [[] for _ in range(self.height)]
        help = 0
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, help)
                help += 1
        for k, v in copy_state.items():
            for i in range(len(v)):
                temp[i].append(v[i])
        for el in temp:
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1

        # diagonal case
        temp = []
        help = 0
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, help)
                help += 1
            temp.append(v)
        a = np.array(temp)
        diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
        diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
        diags = [n.tolist() for n in diags]
        for el in diags:
            count_dups = [sum(1 for g in group if g == 'MAX') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    max_twos += 1
                elif c == 3:
                    max_threes += 1
                elif c >= 4:
                    max_fours += 1
            count_dups = [sum(1 for g in group if g == 'MIN') for _, group in itertools.groupby(el)]
            for c in count_dups:
                if c == 2:
                    min_twos += 1
                elif c == 3:
                    min_threes += 1
                elif c >= 4:
                    min_fours += 1
        if max_fours > 0:
            return 1000000
        elif min_fours > 0:
            return -1000000
        else:
            return max_fours * 10 + max_threes * 5 + max_twos * 2 - (min_fours * 10 + min_threes * 5 + min_twos * 2)

    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    if self.utility(state) == 1000000:
                        print("MAX WINS! \n\n")
                    elif self.utility(state) == -1000000:
                        print("MIN WINS! \n\n")
                    else:
                        print("IT'S A DRAW! \n\n")
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.width):
            print(column, '\t\t', end='')
        print()
        copy_state = {}
        for k, v in state.items():
            if k != 'to_move':
                copy_state[k] = state[k].copy()

        temp = []
        for k, v in copy_state.items():
            while len(v) < self.height:
                v.insert(0, 0)
            temp.append(v)

        for i in range(0, self.height):
            print(i, end='')
            for j in range(0, self.width):
                if copy_state[j][i] == 0:
                    print('\t{}\t|'.format(self.empty), end=" ")
                else:
                    print('\t{}\t|'.format(copy_state[j][i]), end=" ")
            print()
        print()


class PacmanGame(Game):
    def __init__(self, initial_state=None, player='MAX', board=4):
        self.board = board
        if initial_state is None:
            initial_state = self.init_state()
        super(PacmanGame, self).__init__(initial_state, player)
        self.initial_state = initial_state
        self.player = player
        self.to_eat = len(initial_state['specials'])
        self.min = 'MIN'
        self.max = 'MAX'
        self.empty = '.'
        self.special = '*'
        self.met = 'X'

    def init_state(self):
        temp_specials = list(itertools.permutations(range(self.board-1), 2))
        random.shuffle(temp_specials)
        state = {
            'max_pos': (0, 0),
            'min_pos': (self.board-1, self.board-1),
            'specials': temp_specials[: round(self.board ** 2 / 4)],
            'to_move': 'MAX'
        }

        return state

    def actions(self, state):
        """
        Given a state return the list of possible actions
        @param state: a state of the game
        @return: a list
        """
        action_list = ['Up', 'Down', 'Right', 'Left']
        if state['to_move'] == 'MAX':
            pos = state['max_pos']
        elif state['to_move'] == 'MIN':
            pos = state['min_pos']
        else:
            raise ValueError

        if pos[0] == 0:
            action_list.remove("Up")
        if pos[0] == self.board - 1:
            action_list.remove("Down")
        if pos[1] == 0:
            action_list.remove("Left")
        if pos[1] == self.board - 1:
            action_list.remove("Right")
        return action_list

    def result(self, state, action):
        if state['to_move'] == 'MAX':
            pos = state['max_pos']
            reached_pos = self.compute_reached_pos(action, pos)
            specials = [sp_pos for sp_pos in state['specials'] if sp_pos != reached_pos]
            reached_state = {
                'max_pos': reached_pos,
                'min_pos': state['min_pos'],
                'specials': specials,
                'to_move': 'MIN'
            }
            return reached_state

        elif state['to_move'] == 'MIN':
            pos = state['min_pos']
            reached_pos = self.compute_reached_pos(action, pos)
            reached_state = {
                'max_pos': state['max_pos'],
                'min_pos': reached_pos,
                'specials': state['specials'],
                'to_move': 'MAX'
            }
            return reached_state
        else:
            raise ValueError

    @staticmethod
    def compute_reached_pos(action, pos):
        if action == 'Up':
            reached_pos = (pos[0] - 1, pos[1])
        if action == 'Down':
            reached_pos = (pos[0] + 1, pos[1])
        if action == 'Left':
            reached_pos = (pos[0], pos[1] - 1)
        if action == 'Right':
            reached_pos = (pos[0], pos[1] + 1)
        return reached_pos

    def terminal_test(self, state):
        """
        Returns True if the state is a final state (the game is over), False otherwise
        @param state: a state of the game
        @return: True or False
        """
        if state['max_pos'] == state['min_pos'] or len(state['specials']) == 0:
            return True
        else:
            return False

    def utility(self, state):
        """
        Given a state returns its utility
        @param state: a state of the game
        @return: a utility value (integer)
        """
        manhattan = abs(state['max_pos'][0] - state['min_pos'][0]) + abs(state['max_pos'][1] - state['min_pos'][1])
        food = self.to_eat - len(state['specials'])
        return manhattan + food

    def play(self, player_one, player_two):
        """
        A function that simulates the game between two players
        @param player_one: function that models the first player
        @param player_two:  function that models the second player
        """
        state = self.initial_state
        print("----- THE GAME STARTS! -----\n\n")
        self.draw_board(self.initial_state)
        players = [player_one, player_two]
        moves = []
        while True:
            for player in players:
                if self.terminal_test(state):
                    print('----- GAME OVER -----\n\n')
                    return moves
                else:
                    print(f'{self.player} plays!')
                move = player.next_move(state)
                state = self.result(state, move)
                self.draw_board(state)
                moves.append((move, self.player))
                self.player = self.next_player()
                print('_____________________')

    def display(self, state):
        print('_____________________')
        if self.player == 'MAX':
            print(self.player, 'in ', state['max_pos'], self.player_utility(state))
        elif self.player == 'MIN':
            print(self.player, 'in ', state['min_pos'], self.player_utility(state))
        else:
            raise ValueError

    def display_move(self, state, move):
        print(self.player, f'--{move}--> ', state)

    def draw_board(self, state):
        # print header
        print('\t', end='')
        for column in range(0, self.board):
            print(column, '\t\t', end='')
        print()

        for i in range(0, self.board):
            print(i, end='')
            for j in range(0, self.board):
                if (i, j) == state['min_pos'] == state['max_pos']:
                    print('\t{}\t|'.format(self.met), end=" ")
                elif (i, j) == state['min_pos']:
                    print('\t{}\t|'.format(self.min), end=" ")
                elif (i, j) == state['max_pos']:
                    print('\t{}\t|'.format(self.max), end=" ")
                elif (i, j) in state['specials']:
                    print('\t{}\t|'.format(self.special), end=" ")

                else:
                    print('\t{}\t|'.format(self.empty), end=" ")
            print()
        print()



