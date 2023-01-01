from players.player import Player
from minimax import best_move
from game_logic.colors import Grey
def remove_duplicates(list):
    ret = []
    l = len(list)
    for i in range(l):
        is_unique = True
        for j in range(i):
            if list[i] == list[j]:
                is_unique = False
        if is_unique:
            ret.append(list[i]) 
    return ret
def is_acceptable(possible_win):
    # names = list(map(lambda color:color.short,possible_win))
    unique_names =remove_duplicates(possible_win) # list(set(names))
    # print(f'unique_names: {", ".join(list(map(str, unique_names)))}')
    if len(unique_names) > 2:
        return (Grey(), 0)
    if len(unique_names) == 2 and unique_names[0].not_grey() and unique_names[1].not_grey():
        return (Grey(), 0)
    score = len(list(filter(lambda x: x.not_grey(), possible_win)))
    return (unique_names[0], 3**score)

class MinimaxPlayer(Player):
    def __init__(self, color):
         super().__init__(color)
    def get_move(self, game_state):
        def get_possible_moves(game_state):
            # print("game_state", game_state)
            return game_state.board.get_possible_moves()
        def move_to_state(move, game_state):
            return game_state.make_move(move)
        def heuristically_evaluate_state(game_state, is_my_turn):
            if game_state.board.is_full():
                return 0
            if game_state.board.has_winner():
                winner = game_state.board.winner();
                # print(f'{self.get_color()} sees that {winner} could win on turn {game_state.get_current_move()}')
                # print(str(game_state))
                if self.is_my_color(winner):
                    return 1000
                else:
                    # print("returning -infinity")
                    return -1000
            adv = 0
            for win in game_state.board.get_possible_wins():
                cells = [game_state.board.get_cell(*coord) for coord in win]
                (color, score) = is_acceptable(cells)
                # print(f'(color, score)=({color}, {score})')
                if self.is_my_color(color):
                    adv += score
                if self.is_enemy_color(color):
                    adv -= score
            if is_my_turn:
                adv += 10
            else:
                adv -=10
                # if is_acceptable()
            # print(f'adv: {adv}')
            return adv
        move = best_move(game_state,
                        False,
                        get_possible_moves,
                        move_to_state,
                        heuristically_evaluate_state,
                        3)
        print(f'move: {move}')
        return move[1]