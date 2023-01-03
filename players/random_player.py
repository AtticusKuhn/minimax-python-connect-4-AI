from players.player import Player
from random import choice

class RandomPlayer(Player):
    def __init__(self, color):
         super().__init__(color)
    def get_move(self, current_game_state):
        possible_moves = current_game_state.board.get_possible_moves()
        return choice(possible_moves)
    