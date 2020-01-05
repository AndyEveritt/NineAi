import numpy as np

from teams import Teams


class Ai:

    def __init__(self, team, game):
        self.team = team
        self.opponent = self.other_team(team)
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

    def minimax_turn(self, depth=3):
        while not self.game.winner:
            while self.game.team != self.team:
                pass

            best_value = -np.inf
            remaining_locations = np.where(self.game.grid == 0)
            for i in range(len(remaining_locations[0])):
                location = (remaining_locations[0][i],
                            remaining_locations[1][i])
                tmp_grid = self.game.grid.copy()
                tmp_grid = self.game.grid.copy()
                tmp_grid[location] = self.team.value
                value = self.minimax(tmp_grid, False, depth)
                if value > best_value:
                    best_value = value
                    move = location

            if self.game.winner:
                return
            self.game.play(move)

        return

    def minimax(self, grid, maximising_player, depth):
        winner = self.game.check_win_grid(grid)
        if winner:
            return self.heuristic_value(winner)

        elif depth == 0:
            return 0

        # if depth == 0 or np.count_nonzero(grid) == grid.size - 1:
        #     tmp_grid = grid.copy()
        #     remaining_locations = np.where(grid == 0)
        #     location = (remaining_locations[0][0],
        #                 remaining_locations[1][0])
        #     if maximising_player:
        #         tmp_grid[location] = self.team.value
        #     else:
        #         tmp_grid[location] = self.opponent.value
        #     winner = self.game.check_win_grid(tmp_grid)

        #     return self.heuristic_value(winner)

        if maximising_player:
            best_value = -np.inf
            remaining_locations = np.where(grid == 0)
            for i in range(len(remaining_locations[0])):
                location = (remaining_locations[0][i],
                            remaining_locations[1][i])
                tmp_grid = grid.copy()
                tmp_grid[location] = self.team.value
                value = self.minimax(tmp_grid, False, depth-1)
                best_value = max((best_value, value))
            return best_value

        else:
            best_value = np.inf
            remaining_locations = np.where(grid == 0)
            for i in range(len(remaining_locations[0])):
                location = (remaining_locations[0][i],
                            remaining_locations[1][i])
                tmp_grid = grid.copy()
                tmp_grid[location] = self.opponent.value
                value = self.minimax(tmp_grid, True, depth-1)
                best_value = min((best_value, value))
            return best_value

    def heuristic_value(self, winner):
        if winner == self.team:
            return 10
        elif winner == 'Draw':
            return 0
        else:
            return -10

    def other_team(self, team):
        if team == Teams.black:
            return Teams.white
        else:
            return Teams.black
