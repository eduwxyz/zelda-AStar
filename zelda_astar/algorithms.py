from queue import PriorityQueue

import pygame
from visualization import draw

SIZE = 672

def h(start, end):  # Heurística
    x1, y1 = start
    x2, y2 = end
    return abs(x1 + x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw, total=0):
    list_path = [current]
    while current in came_from:
        # print(current.cost)
        total = total + current.cost
        print(f"+ {current.cost}")
        current = came_from[current]
        list_path.append(current)
        current.make_path()
        #sleep(1)
        draw()

    # print(TOTAL)
    return total


def best_caminho(WIN, grid):
    lista_dungers = [grid[6][3], grid[2][18], grid[25][2]]
    best_cam = []
    for i in range(3):
        # breakpoint()
        total = algorithm(
            lambda: draw(WIN, grid, SIZE, 42),
            grid,
            grid[25][28],
            lista_dungers[i],
            True,
        )
        best_cam.append((lista_dungers[i], total))

    shortest_distance = float("inf")
    for dunger, cost in best_cam:
        # breakpoint()
        if cost < shortest_distance:
            shortest_distance = cost
            best_dunger = dunger

    return best_dunger


def algorithm(draw, grid, start, end, flag=False):
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
            total = 0
            if flag:
                list_path = [current]
                while current in came_from:
                    total = total + current.cost

                    current = came_from[current]
                    list_path.append(current)
                return total
            else:
                total = reconstruct_path(came_from, current, draw)
                return total

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + neighbor.cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set:
                    count += temp_g_score
                    closed_set.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
