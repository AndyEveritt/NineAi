import numpy as np

from teams import Teams
from time import sleep


class Game:
    def __init__(self, size, line_length=3):
        self.grid = np.zeros(size, 'uint8')
        self.line_length = line_length  # how many squares in a line to win

        self.team = Teams.black
        self.winner = None

    def next_turn(self):
        x_location = np.random.randint(0, 3)
        y_location = np.random.randint(0, 3)
        self.play(self.team, (x_location, y_location))
        self.check_win_grid(self.grid)

        if self.winner:
            return self.winner

        self.change_team()
        self.next_turn()

    def change_team(self):
        if self.team == Teams.black:
            self.team = Teams.white
        else:
            self.team = Teams.black

    def play(self, team, location):
        self.grid[location] = team.value

    def check_win_grid(self, grid):
        def check_winner(array):
            if len(array) == 1:
                winner = array.pop()
                if winner == Teams.black.value:
                    self.winner = Teams.black
                elif winner == Teams.white.value:
                    self.winner = Teams.white
                else:
                    winner = None

        # check rows
        for i in range(grid.shape[0]):
            row = set(grid[i])
            check_winner(row)

        # check columns
        for j in range(grid.shape[1]):
            column = set(grid[:, j])
            check_winner(column)
        
        # check diagonal
        # for i in range

    def display(self):
        pass


game = Game((3, 3))
game.next_turn()
pass
