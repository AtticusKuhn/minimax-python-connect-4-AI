from game_logic.colors import Grey
from itertools import product
from operator import add
from copy import deepcopy
from functools import lru_cache

direction_deltas = list(product(list(range(-1,2)), list(range(-1,2))))
direction_deltas.pop(4)
directions = [[tuple(i*elem for elem in direction_delta) for i in range(4)] for direction_delta in direction_deltas]
@lru_cache(maxsize=None)
def get_possible_wins(rows, columns):
    cell_coords = list(product(list(range(columns)),list(range(rows))))
    cell_coords_directions = list(product(cell_coords, directions))
    coords_list = [[tuple(map(add, cell_coords, dir_coords))for dir_coords in direction] for (cell_coords, direction) in cell_coords_directions]
    def in_bounds(x,y):
        return  0 <= x and x < columns and 0 <= y and y < rows
    filtered_coords = [coords for coords in coords_list if all(map(lambda coord : in_bounds(*coord), coords))]
    return filtered_coords
class Board:
    @lru_cache(maxsize=None)
    def __init__(self, rows, columns, initial_board = None):
        self.rows = rows
        self.columns = columns 
        board = []
        for i in range(columns):
            board.append([])
        self.board = board         
        self.possible_wins = get_possible_wins(rows, columns)
    @staticmethod
    def from_list(rows, my_list):
        new_board = Board(rows, len(my_list))
        new_board.board = my_list
        return new_board
    def mutable_make_move(self, column, player):
        self.board[column].append(player)
    def mutable_undo_move(self, column):
        self.board[column].pop()
    @lru_cache(maxsize=None)
    def make_move(self, column, player):
        board_copy = deepcopy(self.board)
        if 0 > column or column > self.columns:
            raise Exception(f'column {column} is outside of the board, you cannnot go there.')
        if len(board_copy[column]) >= self.rows:
            raise Exception(f'column {column} is already full. You cannot go there')
        board_copy[column].append(player)
        return Board.from_list(self.rows, board_copy)
    def is_full(self):
        return all([len(column) ==  self.rows for column in self.board])
    def is_in_bounds(self, x,y):
        return  0 <= x and x < self.columns and 0 <= y and y < self.rows
    def has_winner(self):
        return self.winner() is not None
    def is_game_over(self):
        return self.is_full() or self.has_winner()
    def get_possible_wins(self):
        return self.possible_wins
    def winner(self):
        possible_wins = self.get_possible_wins()
        for possible_win in possible_wins:
            cells = [self.get_cell(*coord) for coord in possible_win]
            if self.homogenous(cells) and self.not_blank(cells[0]):
                return cells[0]
        return None
    def not_blank(self, cell):
        return cell.not_grey()
    def get_possible_moves(self):
        if self.is_game_over():
            return []
        return list(filter(lambda x:len(self.board[x]) < self.rows,list(range(self.columns))))
    def homogenous(self, cells):
        return all([c.equals(cells[0]) for c in cells])
    def get_cell(self, x,y):
        if y >= len(self.board[x]):
            return Grey()
        return self.board[x][y]
    def __str__(self):
        return " ".join([ str(i)  for i in range(self.columns)] ) + "\n"  + "\n".join(reversed([" ".join([str(self.get_cell(x,y)) for x in range(self.columns)]) for y in range(self.rows)]))
