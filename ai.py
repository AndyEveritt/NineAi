import numpy as np

from teams import Teams


class Ai:

    def __init__(self, team, game):
        self.team = team
        self.game = game

    def random_turn(self):
        while not self.game.winner:
            while self.game.team != self.team:
                pass

            location = (np.random.randint(0, self.game.grid.shape[0]),
                        np.random.randint(0, self.game.grid.shape[1]))
            while(self.game.grid[location]):
                location = (np.random.randint(0, self.game.grid.shape[0]),
                            np.random.randint(0, self.game.grid.shape[1]))

            self.game.play(location)
            # self.game.check_win_grid(self.game.grid)
        # print(self.game.winner)
        return

    def minimax(self, grid, team, depth):
        if depth == 0 or np.count_nonzero(grid) == 1:
            tmp_grid = grid.copy()

            self.game.check_win_grid(tmp_grid)
            pass
