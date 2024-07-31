import sys
from game import NimGame
from human import human_move
from computer import computer_move
from minmax import minmax

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <num-red> <num-blue> <version> <first-player> <depth>")
        return

    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else 'standard'
    first_player = sys.argv[4] if len(sys.argv) > 4 else 'computer'
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else None

    game = NimGame(num_red, num_blue, version, first_player, depth)
    game.play()

if __name__ == "__main__":
    main()
