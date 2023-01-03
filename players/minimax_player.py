from players.player import Player
from game_logic.colors import Grey

def get_possible_moves(game_state):
    return game_state.board.get_possible_moves()
    
def move_to_state(move, game_state):
    return game_state.make_move(move)
    
# the evaluation of a game state where I am gauranteed
# to win is infinity
INFINITY = 100000

# in a given sequence of 4, evaluate which colors could 
# possibly win in that sequence of 4
def score_sequence_of_four(possible_win):
    unique_colors =set(possible_win) # list(set(names))    
    if len(unique_colors) > 2:
        return (Grey(), 0)
    if len(unique_colors) == 2 and Grey() not in unique_colors:
        return (Grey(), 0)
    not_grey = list(filter(lambda x: x.not_grey(), possible_win))
    score = len(not_grey)
    if score == 0:
        return (Grey(), 0)
    return (not_grey[0], 3**score)

class MinimaxPlayer(Player):
    def __init__(self, color):
         super().__init__(color)
    # evaluate a game state using heuristics and rules-of-thumb
    # for example, count up the number of possible 4-in-a-rows
    # each player could make
    def heuristically_evaluate_state(player, game_state, is_my_turn ):    
        if game_state.board.is_full():
            return 0 # 0 represents a tie, or a perfectly even match
        if game_state.board.has_winner():
            winner = game_state.board.winner();
            if player.is_my_color(winner):
                # infinity represents that I am gauranteed to win
                return INFINITY 
            else:
                # -infinity represents that I am gauranteed to lose
                return -INFINITY
        my_advantage = 0
        # add all the ways I can win and subtract all the ways my opponent can win
        for possible_win in game_state.board.get_possible_wins():
            cells = [game_state.board.get_cell(*coord) for coord in possible_win]
            (color, score) = score_sequence_of_four(cells)
            # for every place where I could win, increase my advantage
            if player.is_my_color(color):
                my_advantage += score
            # for every place where my opponent could win
            # decrease my advantage
            if player.is_enemy_color(color):
                my_advantage -= score
        return my_advantage
    
    def mini_max(
        self,
        game_state,
        maximum_search_depth, 
        alpha=-INFINITY,
        beta=INFINITY,
        is_maximizing_player=True):
        # get a list of all possible moves we can make in this current game state
        list_of_possible_moves = get_possible_moves(game_state)
        # check what the heuristic thinks about this current game state
        eval = self.heuristically_evaluate_state(game_state,is_maximizing_player)
        # if there are no possible list_of_possible_moves to be made, assume the game is over
        if len(list_of_possible_moves) == 0:
            return (eval, None)
        # the convention is that I am the maximizer and my opponent is the minimizer
        optimization_function = max if is_maximizing_player else min
        # if we're not able to search any deeper, just pick the best move heuristically
        if maximum_search_depth <= 0:
            options = []
            for move in list_of_possible_moves:
                game_state.mutable_make_move(move)
                e = self.heuristically_evaluate_state(game_state, not is_maximizing_player)
                game_state.mutable_undo_move(move)
                options.append((e,move))
            return optimization_function(options, key= lambda x:x[0])
        # a list of tuples where the first element is the
        # evaluation of the move and the second element is
        # the move
        possible_moves_with_evaluation = []
        for move in list_of_possible_moves:
            game_state.mutable_make_move(move)
            result = self.mini_max(
                game_state,
                maximum_search_depth - 1,
                alpha,
                beta,
                not is_maximizing_player
            )
            game_state.mutable_undo_move(move)
            possible_moves_with_evaluation.append((result[0],move))
            if is_maximizing_player:
                alpha = optimization_function(alpha, result[0])
            else:
                beta = optimization_function(beta, result[0])
            # if beta <= alpha, then we know we've already found the best move
            # so don't search any more
            if beta <= alpha:
                break
        return optimization_function(possible_moves_with_evaluation, key = lambda x:x[0])
    
    def get_move(self, current_game_state):
        minimax_result = self.mini_max(current_game_state,maximum_search_depth=3)
        (evaluation, best_move) = minimax_result
        return best_move