from map import *

def run() -> None:
    while True:
        game_map.gerar_map_map()
        input("> ")

if __name__ == "__main__":
    map_larg, map_alt = 30, 15
    game_map = Map(map_larg, map_alt)
    run()