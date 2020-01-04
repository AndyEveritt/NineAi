import numpy as np

from teams import Teams
from time import sleep


class Game:
    def __init__(self, size):
        dgrid = {(i,j): "" for i in range(3) for j in range(3)}
        self.grid = np.zeros(size, 'uint8')
        

    def play(self, team, location):
        x = location[0]
        y = location[1]

        self.grid[x][y] = team.value

    def display(self):
        pass


game = Game((40, 40))
game.play(Teams.black, (1, 2))
