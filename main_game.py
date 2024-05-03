from game.games import DummyGame
from game.search import *

game = DummyGame()
first_player = Minimax(game=game)
second_player = Minimax(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

game = DummyGame()
first_player = AlphaBeta(game=game)
second_player = AlphaBeta(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

print(moves)

