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

            if np.count_nonzero(self.game.grid) == self.game.grid.size:
                return

            remaining_locations = np.where(self.game.grid == 0)
            rand_index = np.random.randint(0, len(remaining_locations[0]))
            location = (remaining_locations[0][rand_index],
                        remaining_locations[1][rand_index]
                        )

            if self.game.winner:
                return

            self.game.play(location)
        return

    def minimax(self, grid, team, depth):
        if depth == 0 or np.count_nonzero(grid) == 1:
            tmp_grid = grid.copy()

            winner = self.game.check_win_grid(tmp_grid)

            return self.heuristic_value(winner)

        if team == self.team:
            value = -np.inf
            remaining_locations = np.where(self.game.grid == 0)

    def heuristic_value(self, winner):
        if winner == self.team:
            return 1
        elif winner == 'Draw':
            return 0
        else:
            return -1
