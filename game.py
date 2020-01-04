import numpy as np

from ai import Ai
from teams import Teams
from time import sleep


class Game:
    def __init__(self, size, line_length=3):
        self.grid = np.zeros((size, size), 'uint8')
        self.line_length = line_length  # how many squares in a line to win

        self.team = Teams.black
        self.winner = None

    def change_team(self):
        if self.team == Teams.black:
            self.team = Teams.white
        else:
            self.team = Teams.black

    def play(self, location):
        self.grid[location] = self.team.value
        self.check_win_grid(self.grid)
        self.change_team()

    def check_win_grid(self, grid):
        def check_winner(array):
            if len(array) == 1:
                winner = array.pop()
                if winner in Teams._value2member_map_:
                    self.winner = Teams._value2member_map_[winner]

        # check draw
        if np.count_nonzero(grid) == grid.size:
            self.winner = 'Draw'

        # check rows
        for i in range(grid.shape[0]):
            row = set(grid[i])
            check_winner(row)

        # check columns
        for j in range(grid.shape[1]):
            column = set(grid[:, j])
            check_winner(column)

        # check main diagonal
        diagonal = set(grid.diagonal())
        check_winner(diagonal)

        # check anti-diagonal
        diagonal = set(np.fliplr(grid).diagonal())
        check_winner(diagonal)

        return self.winner

    def display(self):
        pass
