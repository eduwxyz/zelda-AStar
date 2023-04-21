import math
from queue import PriorityQueue
from typing import List, Tuple

import pygame

from zelda_astar.colors import colors

colors = colors()

ROWS = 42
WIDTH = 672
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Zelda A*")
START_COLOR = (255, 255, 255)  # verde
END_COLOR = (128, 128, 128)  # preto
DESTINATIONS = [(25,28), (6, 33), (40, 18), (25, 2), (7,6)]
COLORS = colors()

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
ROSA = (255, 0, 255)


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
        
    def make_path(self):
        self.color = ROSA
        
    def get_pos(self):
        return self.row, self.col
        
    def is_barrier(self):
        return self.color == BLACK
        
    def update_neighbors(self,grid):


        ()
        self.neighbors = []
        if self.row < self.total_rows - 1:
            self.neighbors.append(grid[self.row+1][self.col])
        if self.row > 0:
            self.neighbors.append(grid[self.row-1][self.col])
        if self.col < self.total_rows -1:
            self.neighbors.append(grid[self.row][self.col +1])
        if self.col > 0: 
            self.neighbors.append(grid[self.row][self.col-1])
        
    def make_closed(self):
        self.color = RED
    
    def __lt__(self, other):
        return False

#-------------------------------ALGORITMO A*-----------------------------------#

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)



def reconstruct_path(came_from, current, draw): 
    list_path = [current]
    while current in came_from:
        current = came_from[current]
        list_path.append(current)
        current.make_path()
        draw()
    #breakpoint()
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

        #breakpoint()
        for neighbor in current.neighbors:
            #breakpoint()
            temp_g_score = g_score[current] + neighbor.cost

            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set:
                    count += temp_g_score
                    closed_set.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)






#-------------------------------ALGORITMO A*-----------------------------------#
        

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


def make_grid(maps: dict, width=WIDTH) -> List[List[Spot]]:
    """
    Make the grid.
    """
    
    title = "HYRULE"
    grid = maps[title]
    rows = len(grid)
    gap = width // rows
    win = []
    

    
    
    destinations = DESTINATIONS.copy()
    
    for i in range(rows):
        win.append([])
        for j in range(rows):
            color = COLORS[grid[i][j]]["color"]
            cost = COLORS[grid[i][j]]["cost"]
            
            if (i,j) == destinations[0]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_start = True
                
            elif (i,j) == destinations[-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_end = True
                
                
            elif (i,j) == destinations[1:-1]:
                spot = Spot(i, j, gap, rows, WHITE, 0)
                spot.is_intermediate = True
            else:
                spot = Spot(i, j, gap, rows, color, cost)
                
            
            win[i].append(spot)
            
            
        
            
    return win


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
        ()
        for spot in row:
            for aux in spot:
                aux.draw(win)
        

    draw_grid(win, rows, width)  # Chamar a função para desenhar a grade
    pygame.display.update()




grid = make_grid()
while True: 
    draw(WIN, grid, 42, WIDTH)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for row in grid:
                    for spot in row:
                        spot.update_neighbors(grid)

                ()
                algorithm(lambda: draw(WIN, grid, 42, WIDTH), grid, grid[25][28], grid[7][6])
            

    
