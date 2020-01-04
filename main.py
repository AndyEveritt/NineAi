from game import Game
from ai import Ai
from teams import Teams

import threading
import numpy as np


def check_game_end(game):
    prev_grid = np.zeros_like(game.grid)
    while black.is_alive() and white.is_alive():
        if not np.array_equal(game.grid, prev_grid):
            print(game.grid)
            prev_grid = game.grid.copy()
        pass

    print(game.winner)
    print(game.grid)


if __name__ == "__main__":
    game = Game(3)

    ai_black = Ai(Teams.black, game)
    ai_white = Ai(Teams.white, game)

    black = threading.Thread(target=ai_black.minimax_turn)
    white = threading.Thread(target=ai_white.minimax_turn)

    black.start()
    white.start()

    check_game_end(game)
    pass
