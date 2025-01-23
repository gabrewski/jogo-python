#main.py:

from map import *
import os 

os.system("cls")
def run() -> None:
    while True:
        game_map.display_map()
        input("> ")

if __name__ == "__main__":
    map_larg, map_alt = 60, 15
    game_map = Map(map_larg, map_alt)
    run()