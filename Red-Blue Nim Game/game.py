class NimGame:
    def __init__(self, num_red, num_blue, version='standard', first_player='computer', depth=None):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.first_player = first_player
        self.depth = depth
        self.current_player = first_player

    def is_game_over(self):
        return self.num_red == 0 or self.num_blue == 0

    def get_score(self):
        return self.num_red * 2 + self.num_blue * 3

    def play(self):
        while not self.is_game_over():
            if self.current_player == 'human':
                self.human_move()
                self.current_player = 'computer'
            else:
                self.computer_move()
                self.current_player = 'human'
        
        print("Game over!")
        if self.version == 'standard':
            print(f"Score: {self.get_score()}")
        else:
            print("Misère version: No scoring.")
