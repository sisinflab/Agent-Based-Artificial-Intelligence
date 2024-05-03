import random
import numpy as np


class Minimax:
    def __init__(self, game):
        self.game = game

    def max_value(self, state):
        """
        A function that computes the value given by player MAX to a node
        @param state: a state
        @return: the value associated by max to the node
        """
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        values = [self.min_value(s) for s, a in self.game.successors(state)]
        return max(values)

    def min_value(self, state):
        """
        A function that computes the value given by player MIN to a node
        @param state: a state
        @return: the value associated by max to the node
        """
        if self.game.terminal_test(state):
            return self.game.player_utility(state)
        values = [self.max_value(s) for s, a in self.game.successors(state)]
        return min(values)

    def next_move(self, state):
        """
        Compute the final move suggested to the player MAX
        @param state: a state
        @return: a move
        """
        moves = self.game.actions(state)
        return max(moves, key=lambda move: self.min_value(self.game.result(state, move)))


class AlphaBeta:

    def __init__(self, game):
        self.game = game

    def max_value(self, state, alpha, beta):
        """
        A function that computes the value given by player MAX to a node
        @param state: a state
        @param alpha:
        @param beta:
        @return: the value associated by max to the node
        """
        # game end check
        if self.game.terminal_test(state):
            return self.game.player_utility(state)

        best_value = -np.inf
        for s, a in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            best_value = max(best_value, value)
            # beta test (if MAX choice will never be the choice of MIN, stop searching)
            if best_value >= beta:
                return best_value
            # update the best value for MAX
            alpha = max(alpha, best_value)
        return best_value

    def min_value(self, state, alpha, beta):
        """
        A function that computes the value given by player MIN to a node
        @param state: a state
        @param alpha:
        @param beta:
        @return: the value associated by max to the node
        """
        # game end check
        if self.game.terminal_test(state):
            return self.game.player_utility(state)

        best_value = np.inf
        for s, a in self.game.successors(state):
            value = self.max_value(s, alpha, beta)
            best_value = min(best_value, value)
            # beta test (if MIN choice will never be the choice of MAX, stop searching)
            if best_value <= alpha:
                return best_value
            # update the best value for MIN
            beta = min(beta, best_value)
        return best_value

    def next_move(self, state):
        """
        Compute the final move suggested to the player MAX
        @param state: a state
        @return: a move
        """
        alpha = -np.inf
        beta = np.inf

        best_move = None

        for s, move in self.game.successors(state):
            value = self.min_value(s, alpha, beta)
            if value >= alpha:
                # update the best value for MAX
                alpha = value
                best_move = move
        return best_move


class Random:

    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        moves = self.game.actions(state)
        return random.choice(moves)
