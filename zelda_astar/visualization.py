from typing import List

import pygame
from colors import colors
from spot import Spot

COLORS = colors()
SIZE = 672
DESTINATIONS = [(25, 28), (6, 33), (40, 18), (25, 2), (7, 6)]
WHITE = (255, 255, 255)
BLACK_BROW = (51, 0, 25)
WIN = pygame.display.set_mode((SIZE, SIZE))

def make_grid(maps: dict, title: str, size=SIZE) -> List[List[Spot]]:
    """
    Make the grid.
    """
    grid = maps[title]
    rows = len(grid)
    gap = size // rows
    win = []

    destinations = DESTINATIONS.copy()

    for i in range(rows):
        win.append([])
        for j in range(rows):
            color = COLORS[grid[i][j]]["color"]
            cost = COLORS[grid[i][j]]["cost"]

            if (i, j) == destinations[0]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_start = True

            elif (i, j) == destinations[1]:
                spot = Spot(i, j, gap, rows, BLACK_BROW, 0)
                spot.is_end = True

            elif (i, j) == destinations[2]:
                spot = Spot(i, j, gap, rows, BLACK_BROW, 0)
                spot.is_intermediate = True
            elif (i, j) == destinations[3]:
                spot = Spot(i, j, gap, rows, BLACK_BROW, 0)
                spot.is_intermediate = True

            elif (i, j) == destinations[4]:
                spot = Spot(i, j, gap, rows, (245, 196, 101), 0)
                spot.is_intermediate = True

            else:
                spot = Spot(i, j, gap, rows, color, cost)

            win[i].append(spot)

    return win


def draw_grid(win: pygame.Surface, rows: int, size: int) -> None:
    """
    Desenha a grade na tela.

    Parameters:
        win (pygame.Surface): Janela do pygame.
        rows (int): Número de linhas e colunas da grade.
        size (int): Tamanho da janela em pixels.
    """
    
    gap = size // rows

    for i in range(rows):
        pygame.draw.line(win, (32, 32, 32), (0, i * gap), (size, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (32, 32, 32), (j * gap, 0), (j * gap, size))



def draw(win: pygame.Surface, grid: List[List[Spot]], size: int, rows: int) -> None:
    """
    Desenha a janela.

    Parâmetros:
        - win: a janela na qual o desenho será feito (pygame.Surface)
        - grid: a matriz de espaços que será desenhada (List[List[Spot]])
        - size: o tamanho em pixels da janela (int)
        - rows: o número de linhas da matriz de espaços (int)
    """

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, size)
    pygame.display.update()
