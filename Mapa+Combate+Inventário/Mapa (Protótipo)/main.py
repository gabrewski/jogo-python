#main.py

import os
from map import *
from tile import *

os.system("cls") 


map_larg, map_alt = 60, 15
game_map = Map(map_larg, map_alt)
player = Player_map()


def map_loop():
    while True:
        os.system("cls")  
        game_map.display_map()
        player.get_movement_input(game_map.largura, game_map.altura)
        game_map.update_map(player.pos, player.marker)

map_loop()
