from players.player import Player
def ask_column():
    try:
        return int(input("choose a column>   "))
    except:
        print("invalid int!!!")
        return ask_column()

class HumanPlayer(Player):
    def __init__(self, color):
         super().__init__(color)
    def get_move(self, boardstate):
        return ask_column()
    