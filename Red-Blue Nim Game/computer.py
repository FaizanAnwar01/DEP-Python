def computer_move(game):
    best_score = float('-inf')
    best_move = None
    moves = [(2, 0), (0, 2), (1, 0), (0, 1)]
    if game.version == 'misere':
        moves = [(0, 1), (1, 0), (0, 2), (2, 0)]
    
    for red, blue in moves:
        if red <= game.num_red and blue <= game.num_blue:
            new_num_red = game.num_red - red
            new_num_blue = game.num_blue - blue
            score = minmax(new_num_red, new_num_blue, False, float('-inf'), float('inf'))
            if score > best_score:
                best_score = score
                best_move = (red, blue)
    
    game.num_red -= best_move[0]
    game.num_blue -= best_move[1]
    print(f"Computer removes {best_move[0]} red marbles and {best_move[1]} blue marbles.")
