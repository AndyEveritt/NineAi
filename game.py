import numpy as np

from teams import Teams
from time import sleep


class Game:
    def __init__(self, size, line_length=3):
        self.grid = np.zeros((size, size), 'uint8')
        self.line_length = line_length  # how many squares in a line to win

        self.team = Teams.black
        self.winner = None

    def change_team(self):
        # sleep(0.2)
        if self.team == Teams.black:
            self.team = Teams.white
        else:
            self.team = Teams.black

    def play(self, location):
        sleep(0.2)
        self.grid[location] = self.team.value
        self.winner = self.check_win_grid(self.grid)
        self.change_team()

    def check_win_grid(self, grid):
        def check_winner(array):
            if len(array) == 1:
                winner_num = array.pop()
                if winner_num in Teams._value2member_map_:
                    winner = Teams._value2member_map_[winner_num]
                    return winner

        winner = None

        # check rows
        for i in range(grid.shape[0]):
            row = set(grid[i])
            winner = check_winner(row)
            if winner:
                return winner

        # check columns
        for j in range(grid.shape[1]):
            column = set(grid[:, j])
            winner = check_winner(column)
            if winner:
                return winner

        # check main diagonal
        diagonal = set(grid.diagonal())
        winner = check_winner(diagonal)
        if winner:
            return winner

        # check anti-diagonal
        diagonal = set(np.fliplr(grid).diagonal())
        winner = check_winner(diagonal)
        if winner:
            return winner

        # check draw
        if winner is None and np.count_nonzero(grid) == grid.size:
            winner = 'Draw'

        return winner

    def display(self):
        pass
