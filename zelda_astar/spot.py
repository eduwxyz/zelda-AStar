from typing import List, Tuple

import pygame


class Spot:
    """
    A class to represent a spot on a grid.

    Attributes:
        row (int): The row of the spot.
        col (int): The column of the spot.
        x (int): The x-coordinate of the spot on the screen.
        y (int): The y-coordinate of the spot on the screen.
        size (int): The size of the spot in pixels.
        total_rows (int): The total number of rows in the grid.
        color (Tuple[int, int, int]): The color of the spot.
        cost (int): The cost to traverse the spot.
        is_start (bool): Whether the spot is the start node or not.
        is_end (bool): Whether the spot is the end node or not.
        is_intermediate (bool): Whether the spot is an intermediate node or not.
        open (bool): Whether the spot is open or not.
        neighbors (List[Spot]): The list of neighboring spots.

    Methods:
        draw(win): Draws the spot on the screen.
        is_barrier(): Returns True if the spot is a barrier, i.e. its color is black.
        make_path(): Changes the color of the spot to indicate that it is part of the path.
        update_neighbors(grid): Updates the list of neighboring spots.
        get_pos(): Returns a tuple representing the position of the spot in the grid.
    """

    def __init__(
        self, row: int, col: int, size: int, total_rows: int, color, cost
    ) -> None:
        """
        Initializes a new instance of the Spot class.

        Args:
            row (int): The row of the spot.
            col (int): The column of the spot.
            size (int): The size of the spot in pixels.
            total_rows (int): The total number of rows in the grid.
            color (Tuple[int, int, int]): The color of the spot.
            cost (int): The cost to traverse the spot.
        """
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
        """
        Draws the spot on the screen.

        Args:
            win (pygame.Surface): The window to draw the spot on.
        """
        if self.is_start:
            color = (0, 255, 0)
        elif self.is_end:
            color = (255, 0, 0)
        else:
            color = self.color
        pygame.draw.rect(win, self.color, (self.y, self.x, self.size, self.size))

    def is_barrier(self):
        """
        Returns True if the spot is a barrier, i.e. its color is black.

        Returns:
            bool: True if the spot is a barrier, False otherwise.
        """
        return self.color == (0, 0, 0)  # black

    def make_path(self):
        """
        Changes the color of the spot to indicate that it is part of the path.
        """
        if self.color == (128, 0, 128):
            self.color = (71, 0, 71)
        else:
            self.color = (128, 0, 128)  # purple

    def update_neighbors(self, grid: List[List[list]]) -> None:
        """
    Atualiza a lista de vizinhos do ponto no grid atual.
    Recebe uma matriz de pontos e adiciona os vizinhos de acordo com as posições
    do ponto no grid.

    Parâmetros:
        grid (List[List[Spot]]): Matriz de pontos representando o grid.

    Retorna:
        None
    """
        self.neighbors = []
        if self.row < self.total_rows - 1:  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0:  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1:  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0:  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def get_pos(self) -> Tuple[int, int]:
        """
    Retorna a posição (linha, coluna) do ponto no grid.

    Parâmetros:
        None

    Retorna:
        Tuple[int, int]: Tupla representando a posição (linha, coluna) do ponto.
    """
        return self.row, self.col