from typing import List, Tuple


def colors() -> List[Tuple[int, int, int]]:
    colors = {
        "G": {"color": (147, 208, 77), "cost": 10},  # LIGHT_GREEN
        "S": {"color": (195, 187, 147), "cost": 20},  # LIGHT_BROWN
        "F": {"color": (3, 173, 72), "cost": 100},  # GREEN
        "M": {"color": (149, 137, 85), "cost": 150},  # BROWN
        "W": {"color": (86, 140, 207), "cost": 180},  # BLUE
        "B": {"color": (0, 0, 0), "cost": 1000},  # BLACK
        "C": {"color": (46, 65, 38), "cost": 10},  # GRAY
    }

    return colors
