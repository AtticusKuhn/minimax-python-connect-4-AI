class GameState:
    def __init__(self, colors, board, current_move=0):
        self.colors = colors
        self.board = board
        self.current_move = current_move
    def get_current_color(self):
        return self.colors[self.current_move % len(self.colors)]
    def get_current_move(self):
        return self.current_move
    def is_game_over(self):
        return self.board.is_game_over()
    def make_move(self, column):
        new_board = self.board.make_move(column, self.get_current_color())
        return GameState(self.colors, new_board, self.current_move+1)
    def mutable_make_move(self, column):
        self.board.mutable_make_move(column, self.get_current_color())
        self.current_move +=1
        return self
    def mutable_undo_move(self, column):
        self.board.mutable_undo_move(column)
        self.current_move -=1
        return self
    def __str__(self):
        return f'current turn: {self.current_move}\n Player to move: {self.get_current_color()} \n board:\n{self.board}'
