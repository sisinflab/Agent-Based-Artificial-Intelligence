import random


class Random:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        moves = self.game.actions(state)
        return random.choice(moves)


class Custom:
    def __init__(self, game):
        self.game = game

    def next_move(self, state):
        moves = self.game.actions(state)
        print(moves)
        return input()


class CustomConnectFour(Custom):

    def next_move(self, state):
        moves = self.game.actions(state)
        print(f'Where do you want to insert the disk? The available moves are: {moves}')
        return int(input())
