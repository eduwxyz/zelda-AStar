from queue import PriorityQueue
from time import sleep
from typing import List

import pygame

from colors import colors

COLORS = colors()
screen_states = []
SIZE = 672
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Zelda A*")
START_COLOR = (255, 255, 255)  # verde
END_COLOR = (128, 128, 128)  # preto
DESTINATIONS = [(25, 28), (40, 18), (6, 33), (25, 2), (7, 6)]
DUNGEON_WINDOWS = {}
DUNGEON_WINDOW_SIZES = {
    "Dungeon 1": (640, 480),
    "Dungeon 2": (800, 600),
    "Dungeon 3": (1024, 768),
}

WHITE = (255, 255, 255)


def h(start, end):  # Heurística
    x1, y1 = start
    x2, y2 = end
    return abs(x1 + x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    list_path = [current]
    while current in came_from:
        current = came_from[current]
        list_path.append(current)
        current.make_path()
        draw()
    # breakpoint()
    return list_path


def algorithm(draw, grid, start, end):
    count = 0
    came_from = {}

    open_set = {start}

    closed_set = PriorityQueue()
    closed_set.put((0, count, start))

    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    while not closed_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = closed_set.get()[2]
        open_set.remove(current)

        if current == end:
            return reconstruct_path(came_from, current, draw)

        # breakpoint()
        for neighbor in current.neighbors:
            # breakpoint()
            temp_g_score = g_score[current] + neighbor.cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set:
                    count += temp_g_score
                    closed_set.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)


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


def read_maps() -> dict:
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


def read_dunger() -> dict:
    maps = {}

    current_map = ""
    with open("dunger.txt", "r") as file:
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


def make_grid(maps: dict, size=SIZE) -> List[List[Spot]]:
    """
    Make the grid.
    """

    title = "HYRULE"
    grid = maps[title]
    rows = len(grid)
    gap = size // rows
    win = []

    start_row, start_col = 25, 28
    end_row, end_col = 7, 6

    destinations = DESTINATIONS.copy()

    for i in range(rows):
        win.append([])
        for j in range(rows):
            color = COLORS[grid[i][j]]["color"]
            cost = COLORS[grid[i][j]]["cost"]

            if (i, j) == destinations[0]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_start = True

            elif (i, j) == destinations[-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_end = True

            elif (i, j) == destinations[1:-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_intermediate = True
            else:
                spot = Spot(i, j, gap, rows, color, cost)

            win[i].append(spot)

    return win


def make_grid_dunger(maps: dict, size=SIZE) -> List[List[Spot]]:
    """
    Make the grid.
    """

    title = "DUNGEON 1"
    grid = maps[title]
    rows = len(grid)
    gap = size // rows
    win = []

    start_row, start_col = 25, 28
    end_row, end_col = 7, 6

    destinations = DESTINATIONS.copy()

    for i in range(rows):
        win.append([])
        for j in range(rows):
            color = COLORS[grid[i][j]]["color"]
            cost = COLORS[grid[i][j]]["cost"]

            if (i, j) == destinations[0]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_start = True

            elif (i, j) == destinations[-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_end = True

            elif (i, j) == destinations[1:-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_intermediate = True
            else:
                spot = Spot(i, j, gap, rows, color, cost)

            win[i].append(spot)

    return win


def open_dungeon_window(dungeon_idx):
    if dungeon_idx not in DUNGEON_WINDOWS:
        size = DUNGEON_WINDOW_SIZES[dungeon_idx]
        DUNGEON_WINDOWS[dungeon_idx] = pygame.display.set_mode((size, size))
    pygame.display.update(DUNGEON_WINDOWS[dungeon_idx])


def draw_grid(win, rows, size):
    """
    Draw the grid.
    """

    gap = size // rows

    for i in range(rows):
        pygame.draw.line(win, (128, 128, 128), (0, i * gap), (size, i * gap))
        for j in range(rows):
            pygame.draw.line(win, (128, 128, 128), (j * gap, 0), (j * gap, size))


def draw(win, grid, size, rows) -> None:
    """
    Draw the window.
    """

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, size)
    pygame.display.update()


def main():
    run = True
    maps = read_maps()
    grid = make_grid(maps)

    intermediate_points = [(40, 18), (6, 33), (25, 2)]

    while run:
        draw(WIN, grid, SIZE, 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in grid:
                        for point in row:
                            point.update_neighbors(grid)

                    for i in range(len(DESTINATIONS) - 1):
                        start_coords = DESTINATIONS[i]
                        end_coords = DESTINATIONS[i + 1]

                        start_point = grid[start_coords[0]][start_coords[1]]
                        end_point = grid[end_coords[0]][end_coords[1]]
                        algorithm(
                            lambda: draw(WIN, grid, SIZE, 42),
                            grid,
                            start_point,
                            end_point,
                        )

                        screen_states.append(WIN.copy())
                        map_dunger = read_dunger()
                        grid_dunger = make_grid_dunger(map_dunger)
                        draw(WIN, grid_dunger, SIZE, 42)
                        pygame.display.update()
                        sleep(2)

                if event.key == pygame.K_BACKSPACE:
                    # restaura o estado anterior da tela principal
                    if screen_states:
                        last_state = screen_states.pop()
                        WIN.blit(last_state, (0, 0))
                        pygame.display.update()


if __name__ == "__main__":
    main()
