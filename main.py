from game import Game
from ai import Ai
from teams import Teams

import threading
import yappi
import numpy as np
from time import sleep


def check_game_end(game):
    prev_grid = np.zeros_like(game.grid)
    while black.is_alive() and white.is_alive():
        if not np.array_equal(game.grid, prev_grid):
            print(game.grid)
            print('\n')
            prev_grid = game.grid.copy()
        pass

    print(game.winner)
    print(game.grid)


if __name__ == "__main__":
    yappi.start()

    game = Game(3)

    ai_black = Ai(Teams.black, game)
    ai_white = Ai(Teams.white, game)

    black = threading.Thread(target=ai_black.minimax_turn, args=(3,))
    white = threading.Thread(target=ai_white.minimax_turn, args=(5,))

    black.start()
    white.start()

    check_game_end(game)

    yappi.get_func_stats().print_all()
    yappi.get_thread_stats().print_all()
    pass
