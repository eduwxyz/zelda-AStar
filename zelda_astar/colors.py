from typing import List, Tuple


def colors() -> List[Tuple[int, int, int]]:
    """
    Retorna uma lista de tuplas contendo as cores para cada tipo de célula do grid.

    Returns:
        List[Tuple[int, int, int]]: Lista de tuplas contendo as cores para cada tipo de célula do grid.
    """
    colors = {
        "G": {"color": (147, 208, 77), "cost": 10},  # LIGHT_GREEN
        "S": {"color": (195, 187, 147), "cost": 20},  # LIGHT_BROWN
        "F": {"color": (3, 173, 72), "cost": 100},  # GREEN
        "M": {"color": (149, 137, 85), "cost": 150},  # BROWN
        "W": {"color": (86, 140, 207), "cost": 180},  # BLUE
        "B": {"color": (0, 0, 0), "cost": 1000},  # BLACK
        "C": {"color": (128, 128, 128), "cost": 10},  # GRAY
    }

    return colors
