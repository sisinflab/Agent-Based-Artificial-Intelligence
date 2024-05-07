from game.games import PacmanGame
from game.search import *
from game.player import *

game = PacmanGame(board=5)
# first_player = Random(game=game)
first_player = LimitedAlphaBeta(game=game, limit=10)
# first_player = Custom(game)
# second_player = Random(game=game)
second_player = LimitedAlphaBeta(game=game, limit=10)

moves = game.play(first_player, second_player)

print(moves)

