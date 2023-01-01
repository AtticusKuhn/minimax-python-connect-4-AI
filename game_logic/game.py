from game_logic.game_state import GameState
from game_logic.board import Board

class Game:
    def __init__(self,players):
        colors = [player.get_color() for player in players]
        self.players = players
        self.game_state = GameState(colors,Board(columns=7,rows=6))
    def play(self):
        print("starting connect-4 game")
        while not self.game_state.is_game_over():
            self.play_turn()
        print("----GAME OVER----")
        print(str(self.game_state))
    def increase_turn(self):
        self.current_turn += 1
    def get_current_player(self):
        return self.players[self.game_state.get_current_move() % len(self.players)]
    def play_turn(self):
        print(str(self.game_state))
        player = self.get_current_player()
        move = player.get_move(self.game_state)
        self.game_state = self.game_state.make_move(move)
        
                
        