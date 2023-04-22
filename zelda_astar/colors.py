from typing import List, Tuple


def colors() -> List[Tuple[int, int, int]]:
    colors = {
        "G": {"color": (0, 255, 0), "cost": 10},  # LIGHT_GREEN
        "S": {"color": (160, 140, 60), "cost": 20},  # LIGHT_BROWN
        "F": {"color": (0, 150, 50), "cost": 100},  # GREEN
        "M": {"color": (80, 40, 0), "cost": 150},  # BROWN
        "W": {"color": (0, 150, 255), "cost": 180},  # BLUE
        "B": {"color": (0, 0, 0), "cost": 200},  # BLACK
        "C": {"color": (128, 128, 128), "cost": 250},  # GRAY
    }

    return colors
