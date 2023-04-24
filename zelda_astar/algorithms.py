from queue import PriorityQueue
from time import sleep

import pygame
from spot import Spot
from visualization import draw

SIZE = 672

from typing import Any, Callable, Dict, List, Tuple


def h(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    """
    Heurística para encontrar a distância de Manhattan entre dois pontos.

    Args:
        start: Uma tupla contendo as coordenadas x e y do ponto de início.
        end: Uma tupla contendo as coordenadas x e y do ponto de destino.

    Returns:
        A distância de Manhattan entre os pontos de início e destino, calculada como a soma das diferenças absolutas
        das coordenadas x e y.

    Raises:
        TypeError: Se start ou end não forem tuplas contendo duas coordenadas numéricas inteiras.
    """
    if not isinstance(start, tuple) or len(start) != 2 or not isinstance(start[0], int) or not isinstance(start[1], int):
        raise TypeError("start deve ser uma tupla contendo duas coordenadas numéricas inteiras.")
    if not isinstance(end, tuple) or len(end) != 2 or not isinstance(end[0], int) or not isinstance(end[1], int):
        raise TypeError("end deve ser uma tupla contendo duas coordenadas numéricas inteiras.")
    
    x1, y1 = start
    x2, y2 = end
    
    return abs(x1 - x2) + abs(y1 - y2)



def reconstruct_path(came_from: Dict[Any, Any], current: Any, draw: Callable, total: int = 0) -> int:
    """
    Reconstrói o caminho percorrido de um ponto de destino até o ponto de partida a partir de um dicionário de
    pontos adjacentes.

    Args:
        came_from: Um dicionário contendo como chaves os pontos visitados e como valores os pontos adjacentes visitados anteriormente durante a busca.
        current: O ponto de destino do qual se deseja reconstruir o caminho percorrido.
        draw: Uma função responsável por desenhar os pontos e caminhos percorridos.
        total: A soma do custo de cada passo do caminho reconstruído (default: 0).

    Returns:
        A soma do custo de cada passo do caminho reconstruído.

    Raises:
        TypeError: Se came_from não for um dicionário, current não for um ponto ou draw não for uma função.
    """
    if not isinstance(came_from, dict):
        raise TypeError("came_from deve ser um dicionário.")
    if not callable(draw):
        raise TypeError("draw deve ser uma função.")
    # Verifica se o tipo do argumento current é compatível com a chave de came_from.
    if current not in came_from:
        raise TypeError("current não é um ponto válido para o dicionário came_from.")
    
    list_path = [current]
    while current in came_from:
        total = total + current.cost
        print(f"+ LINHA: {current.row} / COLUNA: {current.col} / CUSTO: {current.cost}")
        current = came_from[current]
        list_path.append(current)
        current.make_path()
        #sleep(0.25)
        draw()

    return total


def best_caminho(WIN: pygame.Surface, grid: List[List[Tuple[int, int, int]]]) -> Tuple[int, int, int]:
    """
    Encontra o melhor caminho a partir de três destinos pré-definidos.

    Args:
        WIN: Uma superfície do Pygame na qual o caminho será desenhado.
        grid: Uma matriz que representa o grid do jogo.

    Returns:
        As coordenadas do destino mais próximo.

    Raises:
        TypeError: Se WIN não for uma superfície do Pygame ou se grid não for uma matriz.
    """
    if not isinstance(WIN, pygame.Surface):
        raise TypeError("WIN deve ser uma superfície do Pygame.")
    if not isinstance(grid, list) or not all(isinstance(row, list) and all(isinstance(cell, tuple) and len(cell) == 3 for cell in row) for row in grid):
        raise TypeError("grid deve ser uma matriz de tuplas com três elementos (cores RGB).")
        
    lista_dungers = [grid[6][3], grid[2][18], grid[25][2]]
    best_cam = []
    for i in range(3):
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
        if cost < shortest_distance:
            shortest_distance = cost
            best_dunger = dunger

    return best_dunger


def algorithm(draw: Callable, grid: List[List[Spot]], start: Spot, end: Spot, flag: bool = False) -> int:
    """
    Implementa o algoritmo A* para encontrar o caminho mais curto em uma grade entre um nó de início e um nó
    final.

    Argumentos:
    - draw: uma função que desenha a grade e o caminho encontrado (usando pygame)
    - grid: uma matriz 2D de objetos Spot representando a grade
    - start: o nó de início (um objeto Spot)
    - end: o nó final (um objeto Spot)
    - flag (opcional): uma flag que indica se a função deve retornar apenas o custo total do caminho encontrado, sem
    desenhar a grade e o caminho

    Retorna:
    - Se flag=False, retorna o custo total do caminho encontrado e desenha a grade e o caminho encontrado usando a função
    draw().
    - Se flag=True, retorna apenas o custo total do caminho encontrado.
    """
    
    
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
