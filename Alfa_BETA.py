def alpha_beta(current_number, is_computer_turn, alpha, beta):
    # Base case: if the current number is less than or equal to 10, or if it cannot be divided by 2 or 3,
    # return 0 indicating terminal state.
    if current_number <= 10 or (current_number % 2 != 0 and current_number % 3 != 0):
        return 0, None

    if is_computer_turn:
        max_score = float('-inf')
        best_move = None
        if current_number % 2 == 0:
            # Recursively call alphabeta function for the next move with a decreased number and opponent's turn,
            # and update alpha with the maximum score found so far.
            score, next_move = alphabeta(current_number // 2, False, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = 2
            alpha = max(alpha, max_score)
            # Perform alpha-beta pruning: if beta is less than or equal to alpha, prune the subtree.
            if beta <= alpha:
                return max_score, best_move
        if current_number % 3 == 0:
            score, next_move = alphabeta(current_number // 3, False, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = 3
            alpha = max(alpha, max_score)
            if beta <= alpha:
                return max_score, best_move
        return max_score, best_move
    else:
        min_score = float('inf')
        if current_number % 2 == 0:
            score, next_move = alphabeta(current_number // 2, True, alpha, beta)
            min_score = min(min_score, score)
            beta = min(beta, min_score)
            if beta <= alpha:
                return min_score, None
        if current_number % 3 == 0:
            score, next_move = alphabeta(current_number // 3, True, alpha, beta)
            min_score = min(min_score, score)
            beta = min(beta, min_score)
            if beta <= alpha:
                return min_score, None
        return min_score, None

# Function to choose the best move for the computer using alphabeta algorithm.
def computer_choose_number(current_number):
    next_move = None
    if current_number % 2 == 0:
        # Start alphabeta search with initial alpha and beta values.
        score, next_move = alphabeta(current_number // 2, True, float('-inf'), float('inf'))
    if current_number % 3 == 0  and not next_move:
        score, next_move = alphabeta(current_number // 3, True, float('-inf'), float('inf'))
    return next_move

# Example usage
number_to_divide = 17946
chosen_divisor = computer_choose_number(number_to_divide)
print(chosen_divisor)  # Output: 3 or 2