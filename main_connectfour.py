from game.games import ConnectFour
from game.search import *
from game.player import *

game = ConnectFour()
# first_player = Random(game=game)
# first_player = Minimax(game=game)
first_player = LimitedAlphaBeta(game=game, limit=3)
# first_player = CustomConnectFour(game)
# second_player = Random(game=game)
# second_player = LimitedMinimax(game=game, limit=3)
second_player = LimitedAlphaBeta(game=game, limit=3)
# second_player = Minimax(game=game)

moves = game.play(first_player, second_player)

print(moves)

