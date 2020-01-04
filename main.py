from game import Game
from ai import Ai
from teams import Teams

import threading


def check_game_end(game):
    while black.is_alive() and white.is_alive():
        pass

    print(game.winner)
    print(game.grid)


if __name__ == "__main__":
    game = Game(3)

    ai_black = Ai(Teams.black, game)
    ai_white = Ai(Teams.white, game)

    black = threading.Thread(target=ai_black.random_turn)
    white = threading.Thread(target=ai_white.random_turn)

    black.start()
    white.start()

    check_game_end(game)
    pass
