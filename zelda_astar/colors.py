from typing import List, Tuple


def colors() -> List[Tuple[int, int, int]]:
    colors = {
        'G': {'color': (0, 255, 0), 'cost': 10}, # LIGHT_GREEN
        'D': {'color': (160, 140, 60), 'cost': 20}, # LIGHT_BROWN
        'F': {'color': (0, 150, 50), 'cost': 100}, # GREEN
        'M': {'color': (80, 40, 0), 'cost': 150}, # BROWN
        'R': {'color': (0, 150, 255), 'cost': 180}, # BLUE
    }
    
    return colors