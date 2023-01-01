from game_logic.game import Game
from game_logic.game_state import GameState
from game_logic.board import Board

from players.human_player import HumanPlayer
from players.minimax_player import MinimaxPlayer
import cProfile

from game_logic.colors import Red, Blue, Grey
r =Red()
b = Blue()
g = Grey()
def main():
    player1 = MinimaxPlayer(Red())
    player2 = MinimaxPlayer(Blue())
    game = Game(players=[player1, player2])
    game.play()

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
if __name__ == "__main__":
    main()
    # test()
    # cProfile.run('test()')

