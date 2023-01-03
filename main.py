from game_logic.game import Game
from game_logic.game_state import GameState
from game_logic.board import Board

from players.human_player import HumanPlayer
from players.minimax_player import MinimaxPlayer
from players.random_player import RandomPlayer

from game_logic.colors import Red, Blue, Grey

def main():
    player1 = MinimaxPlayer(Red())
    player2 = HumanPlayer(Blue())
    game = Game(players=[player1, player2])
    game.play()

if __name__ == "__main__":
    main()

