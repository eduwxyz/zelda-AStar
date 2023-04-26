from queue import PriorityQueue
from time import sleep
from typing import List

import pygame
from algorithms import algorithm
from colors import colors
from map import read_maps
from visualization import draw, make_grid

COLORS = colors()
screen_states = []
SIZE = 672
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Zelda A*")
DESTINATIONS = [(25, 28), (6, 33), (40, 18), (25, 2), (7, 6)]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()
    TOTAL_PERCORRIDO = 0
    aux = 0
    maps = read_maps()
    grid = make_grid(maps, "HYRULE")
    screen_states = []

    while True:
        draw(WIN, grid, SIZE, 42)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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

                        if i == 0:
                            dungeon = "DUNGEON 1"
                            start_dungeon_coords = (26, 14)
                            end_dungeon_coords = (3, 13)
                        elif i == 1:
                            dungeon = "DUNGEON 2"
                            start_dungeon_coords = (25, 13)
                            end_dungeon_coords = (2, 13)
                        elif i == 2:
                            dungeon = "DUNGEON 3"
                            start_dungeon_coords = (25, 14)
                            end_dungeon_coords = (19, 15)

                        aux = algorithm(
                            lambda: draw(WIN, grid, SIZE, 42),
                            grid,
                            end_point,
                            start_point,
                        )

                        TOTAL_PERCORRIDO += aux

                        screen_states.append(WIN.copy())

                        map_dunger = read_maps()
                        grid_dunger = make_grid(map_dunger, dungeon)
                        grid_dunger[end_dungeon_coords[0]][
                            end_dungeon_coords[1]
                        ].color = (245, 196, 101)
                        start_point_dunger = grid_dunger[start_dungeon_coords[0]][
                            start_dungeon_coords[1]
                        ]
                        end_point_dunger = grid_dunger[end_dungeon_coords[0]][
                            end_dungeon_coords[1]
                        ]
                        

                        for linha in grid_dunger:
                            for spot in linha:
                                spot.update_neighbors(grid_dunger)
                                
                        grid_dunger[25][2].color = BLACK
                        grid_dunger[7][6].color = BLACK
                    

                        if i<=2:
                            aux = algorithm(
                            lambda: draw(WIN, grid_dunger, SIZE, 28),
                            grid_dunger,
                            end_point_dunger,
                            start_point_dunger,
                            )

                        TOTAL_PERCORRIDO += aux

                        if i <= 2:
                            aux = algorithm(
                                lambda: draw(WIN, grid_dunger, SIZE, 28),
                                grid_dunger,
                                start_point_dunger,
                                end_point_dunger,
                            )

                            TOTAL_PERCORRIDO += aux

                        sleep(2)

                print(f"TOTAL PERCORRIDO: {TOTAL_PERCORRIDO}")

                if event.key == pygame.K_BACKSPACE:
                    # Restaura o estado anterior da tela principal
                    if screen_states:
                        last_state = screen_states.pop()
                        WIN.blit(last_state, (0, 0))
                        pygame.display.update()


if __name__ == "__main__":
    main()
