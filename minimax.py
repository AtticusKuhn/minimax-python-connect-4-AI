from functools import lru_cache

# minimax takes in the current state of the game
# whether the current player is the maximizing player
# a function to get all possible states
# a function to heuristically evalute states
# and a maximum depth and it returns the score
# eval of the current state
infinity = 1000
searched = 0
@lru_cache(maxsize=None)
def minimax(state,
            is_maximizing_player, 
            get_possible_states,
            heuristically_evaluate_state, 
            max_depth,
           alpha = -infinity,
           beta = infinity):
    # print(f'I am exploring {state}')
    global searched
    searched +=1
    if max_depth <= 0:
        return heuristically_evaluate_state(state, is_maximizing_player)
    scores = []
    for new_state in get_possible_states(state):
        scores.append(
            score := minimax(
                new_state, 
                not is_maximizing_player,
                get_possible_states,
                heuristically_evaluate_state, 
                max_depth-1,
                alpha, 
                beta)
        )
        if is_maximizing_player:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            # print("minimax optimization!")
            break
    # print(f'scores: {scores}')
    if len(scores) == 0:
        # print("no scores!")
        return heuristically_evaluate_state(state, is_maximizing_player)
    return (max if is_maximizing_player else min)(scores)

def best_move(state,
            is_maximizing_player, 
            get_possible_moves,
            move_to_state,
            heuristically_evaluate_state, 
            max_depth):
    # moves = []
    # if max_depth <= 0:
    moves = get_possible_moves(state)
    # else:
    #     moves = best_move(state, is_maximizing_player,get_possible_moves, move_to_state,heuristically_evaluate_state, max_depth-1)
    #     moves.sort(key=lambda s:s[0], reverse=True )
    #     moves = [m[1] for m in moves]
    def get_possible_states(the_state):
        my_states =[move_to_state(move, the_state) for move in get_possible_moves(the_state)]
        my_states.sort(key=lambda s: heuristically_evaluate_state(s,is_maximizing_player), reverse=True)
        return my_states
    # searched = 0
    states = [(minimax(move_to_state(move, state),
                       is_maximizing_player,
                       get_possible_states,
                       heuristically_evaluate_state,
                      max_depth), move) for move in moves]
    print(states)
    global searched
    print(f'searched {searched} states')
    searched = 0
    func = min if is_maximizing_player else max 
    # states.sort(key=lambda x:x[0], reverse=(not is_maximizing_player))
    best = func(states, key=lambda x:x[0])
    return best