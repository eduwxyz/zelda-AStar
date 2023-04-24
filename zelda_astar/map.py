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
