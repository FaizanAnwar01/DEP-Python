def human_move(game):
    print(f"Red marbles: {game.num_red}, Blue marbles: {game.num_blue}")
    while True:
        try:
            red = int(input("Enter number of red marbles to remove (1 or 2): "))
            blue = int(input("Enter number of blue marbles to remove (1 or 2): "))
            if (red in [1, 2] and blue in [1, 2]) and (red <= game.num_red and blue <= game.num_blue):
                game.num_red -= red
                game.num_blue -= blue
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
