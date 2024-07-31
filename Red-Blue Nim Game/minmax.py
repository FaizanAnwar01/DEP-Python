def minmax(num_red, num_blue, is_maximizing, alpha, beta):
    if num_red == 0 or num_blue == 0:
        return num_red * 2 + num_blue * 3

    if is_maximizing:
        max_eval = float('-inf')
        moves = [(2, 0), (0, 2), (1, 0), (0, 1)]
        if version == 'misere':
            moves = [(0, 1), (1, 0), (0, 2), (2, 0)]
        
        for red, blue in moves:
            if red <= num_red and blue <= num_blue:
                new_num_red = num_red - red
                new_num_blue = num_blue - blue
                eval = minmax(new_num_red, new_num_blue, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        moves = [(2, 0), (0, 2), (1, 0), (0, 1)]
        if version == 'misere':
            moves = [(0, 1), (1, 0), (0, 2), (2, 0)]
        
        for red, blue in moves:
            if red <= num_red and blue <= num_blue:
                new_num_red = num_red - red
                new_num_blue = num_blue - blue
                eval = minmax(new_num_red, new_num_blue, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
