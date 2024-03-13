def generate_game_tree(state):
    # Base case: check if the game is over
    if is_game_over(state):
        return evaluate_state(state)

    # Generate all possible moves
    moves = generate_moves(state)

    # Initialize an empty dictionary to store the game tree
    game_tree = {}

    # Recursively generate the game tree for each possible move
    for move in moves:
        # Make the move
        new_state = make_move(state, move)

        # Generate the game tree for the new state
        game_tree[move] = generate_game_tree(new_state)

    return game_tree