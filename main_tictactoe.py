from game.games import TicTacToe
from game.search import *
from game.player import *

game = TicTacToe()
# first_player = Random(game=game)
# first_player = Custom(game=game)
first_player = LimitedMinimax(game=game, limit=3)
# first_player = Minimax(game)
# second_player = Random(game=game)
# second_player = LimitedMinimax(game=game, limit=2)
# second_player = Minimax(game=game)
second_player = LimitedMinimax(game=game, limit=3)

moves = game.play(first_player, second_player)

print(moves)
