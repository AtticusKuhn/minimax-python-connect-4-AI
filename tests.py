# getting minimax right is very difficult,
# so be sure that you have some good tests

import cProfile
from game_logic.game import Game
from game_logic.game_state import GameState
from game_logic.board import Board
from players.minimax_player import MinimaxPlayer

r = Red()
b = Blue()
g = Grey()


def test():
    player = MinimaxPlayer(Blue())
    
    board = Board.from_list(6, [
        [],
        [b],
        [],
        [r,r,b],
        [r,r,b],
        [b,r,b],
        [r]
    ])
    
    game_state = GameState([Red(), Blue()],board, current_move= 11)
    print(str(game_state))
    move  = player.get_move(game_state)
    print(move)
def test2():
    player = MinimaxPlayer(Red())
    board = Board.from_list(6, [
        [],[],[],[],[],[],[]
    ])
    game_state = GameState([Red(), Blue()],board, current_move= 0)
    print(str(game_state))
    move  = player.get_move(game_state)
    print(move)
def test3():
    player = MinimaxPlayer(Red())
    board = Board.from_list(6, [
        [],[],[b,b,b],[r,b,r,r,r],[],[],[]
    ])
    game_state = GameState([Red(), Blue()],board, current_move= 8)
    print(str(game_state))
    move  = player.get_move(game_state)
    print(move)