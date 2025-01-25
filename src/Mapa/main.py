#main.py

import os
from Mapa.map_stages import *
from Mapa.tile import *
from Mapa.map import *
from Mapa.encounter import roll_encounter
from Combat.combat_test import combat
import msvcrt


map_larg, map_alt = 60, 15

def map_loop(player, stage_choice:int):
    os.system('cls')
    maps = (ForestMap(60, 15), DesertMap(60, 15), SnowMap(60, 15), SwampMap(60, 15), FireMap(60, 15))
    game_map = maps[stage_choice-1]
    encounter_chance = 0

    while True:
        os.system('cls')
        game_map.display_map()
        print("\nPressione [W] para mover para cima, [S] para baixo, [A] para esquerda e [D] para direita.")
        print("\nPressione [1] para voltar ao mapa principal")

        key = player.get_movement_input(game_map.largura, game_map.altura)

        if key in ("w", "W", "s", "S", "a", "A", "d", "D"):
                enemy = roll_encounter(int(stage_choice), encounter_chance)
                if enemy:
                    os.system('cls')
                    encounter_chance = 0

                    if combat(player, enemy):
                        continue
                    else:
                        return

                else:
                    encounter_chance += 2

        elif key == '1':
             return

        game_map.update_map(player.pos, player.marker)

    