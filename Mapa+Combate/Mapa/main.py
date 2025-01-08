from map import Map
import os

os.system("")


def run() -> None:
    while True:
        game_map.display_map()
        input("> ")


if __name__ == "__main__":
    map_w, map_h = 45, 15
    game_map = Map(map_w, map_h)
    run()