import math
from queue import PriorityQueue
from typing import List, Tuple

import pygame

from zelda_astar.colors import colors


colors = colors()

WIDTH = 672
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

    def __init__(self, row: int, col: int, width: int, total_rows: int, color, cost, t):
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
        self.color = color
        self.cost = cost
        self.color = color  # Define a cor como um atributo da classe.
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.t = t

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


def read_map() -> dict:
    maps = {}
    
    current_map = ""
    with open("mapa_principal.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:  
                continue

            if line.startswith("#"):
                current_map = line.lstrip("#").strip()
                maps.setdefault(current_map, [])  

            else:
                maps[current_map].append(line)
        

    return maps


def make_grid(maps=read_map(), title= "HYRULE", width=WIDTH) -> List[List[Spot]]:
    """
    Create a grid of spots.

    Args:
        maps (dict): The maps to create the grid.
        width (int): The width of the grid.

    Returns:
        List[List[Spot]]: The grid of spots.
    """
    grid = maps[title]
    rows = len(grid)
    gap = width // rows
    aux = []
    

    # Validar argumentos
    if rows <= 0 or width <= 0:
        raise ValueError("rows and width must be positive integers")

    def create_spot(i: int, j: int, gap: int, rows: int, color, cost, t) -> Spot:
        """
        Create a Spot object.

        Args:
            i (int): The row index of the spot.
            j (int): The column index of the spot.
            gap (int): The width of the spot.
            rows (int): The total number of rows in the grid.
            color (Tuple[int, int, int]): The color of the spot.
            cost (int): The cost of the spot.

        Returns:
            Spot: The created spot.
        """
        return Spot(i, j, gap, rows, color, cost, t)

    
    for i in range(rows):
        for j in range(rows):
            spot = create_spot(i, j, gap, rows, colors[grid[i][j]]["color"], colors[grid[i][j]]["cost"], grid[i][j])
            #breakpoint()
            aux.append([spot])

    return aux


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

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)  # Chamar a função para desenhar a grade
    pygame.display.update()


grid = make_grid()
while True: 
    draw(WIN, grid, 42, WIDTH)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
