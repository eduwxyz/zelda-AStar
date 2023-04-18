import math
from queue import PriorityQueue
from typing import List, Tuple

import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Zelda A*")

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    """
    A class to represent a spot on a grid.
    """

    def __init__(self, row: int, col: int, width: int, total_rows: int):
        """
        Initialize the Spot class.

        Args:
            row (int): The row index of the spot.
            col (int): The column index of the spot.
            width (int): The width of the spot.
            total_rows (int): The total number of rows in the grid.
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)  # Define a cor como um atributo da classe.
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self) -> Tuple[int, int]:
        """
        Get the position of the spot.

        Returns:
            Tuple[int, int]: The row and column index of the spot.
        """
        return self.row, self.col

    def draw(self, win: pygame.Surface) -> None:
        """
        Draw the spot on the given window.

        Args:
            win (pygame.Surface): The window to draw on.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))



#FIXME: criar lógica para cores

def make_grid(rows: int, width: int) -> List[List[Spot]]:
    """
    Create a grid of spots.

    Args:
        rows (int): The number of rows in the grid.
        width (int): The width of the grid.

    Returns:
        List[List[Spot]]: The grid of spots.
    """
    grid = []
    gap = width // rows

    # Validar argumentos
    if rows <= 0 or width <= 0:
        raise ValueError("rows and width must be positive integers")

    def create_spot(i: int, j: int, gap: int, rows: int) -> Spot:
        """
        Create a Spot object.

        Args:
            i (int): The row index of the spot.
            j (int): The column index of the spot.
            gap (int): The width of the spot.
            rows (int): The total number of rows in the grid.

        Returns:
            Spot: The created spot.
        """
        return Spot(i, j, gap, rows)

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = create_spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows: int, width: int) -> None:
    """
    Draw the grid lines on the window.

    Args:
        win (pygame.Surface): The window to draw on.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid.

    Returns:
        None
    """
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid: List[List[Spot]], rows: int, width: int) -> None:
    """
    Draw the grid and the spots on the window.

    Args:
        win (pygame.Surface): The window to draw on.
        grid (List[List[Spot]]): The grid of spots.
        rows (int): The number of rows in the grid.
        width (int): The width of the grid.

    Returns:
        None
    """
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)  # Chamar a função para desenhar a grade
    pygame.display.update()


