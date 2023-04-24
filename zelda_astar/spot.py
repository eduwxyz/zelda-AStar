import pygame


class Spot:
    """
    A class to represent a spot on a grid.
    """

    def __init__(
        self, row: int, col: int, size: int, total_rows: int, color, cost
    ) -> None:
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.size = size
        self.total_rows = total_rows
        self.color = color
        self.cost = cost
        self.is_start = False
        self.is_end = False
        self.is_intermediate = False
        self.open = False
        self.neighbors = []

    def draw(self, win):
        if self.is_start:
            color = (0, 255, 0)
        elif self.is_end:
            color = (255, 0, 0)
        else:
            color = self.color
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))

    def is_barrier(self):
        return self.color == (0, 0, 0)  # black

    def make_path(self):
        if self.color == (128, 0, 128):
            self.color = (71, 0, 71)
        else:
            self.color = (128, 0, 128)  # purple

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1:  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0:  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1:  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0:  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def get_pos(self):
        return self.row, self.col