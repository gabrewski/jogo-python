#main.py

import os
from Mapa.map_stages import *
from Mapa.tile import *
from Mapa.map import *
from Mapa.encounter import roll_encounter
from Combat.combat_test import combat
import msvcrt

def map_loop(player, stage_choice:int, size:tuple[int, int], interface):
    maps = (ForestMap(*size), DesertMap(*size), SnowMap(*size), SwampMap(*size), FireMap(*size))
    game_map = maps[stage_choice-1]
    encounter_chance = 0

    while True:
        interface(game_map.display_map())

        print("\nPressione [W] para mover para cima, [S] para baixo, [A] para esquerda e [D] para direita.")
        print("\nPressione [1] para voltar ao mapa principal")

        key = player.get_movement_input(game_map.largura, game_map.altura)

        # if key in ("w", "W", "s", "S", "a", "A", "d", "D"):
        #         enemy = roll_encounter(int(stage_choice), encounter_chance)
        #         if enemy:
        #             os.system('cls')
        #             encounter_chance = 0

        #             if combat(player, enemy):
        #                 continue
        #             else:
        #                 return

        #         else:
        #             encounter_chance += 2

        # elif key == '1':
        #      return

        game_map.update_map(player.pos, player.marker)


'''def map_loop(player, stage_choice:int, stdscr):
    maps = (ForestMap(166, 46), DesertMap(166, 46), SnowMap(166, 46), SwampMap(166, 46), FireMap(166, 46))
    game_map = maps[stage_choice-1]
    encounter_chance = 0

    while True:
        update(game_map.display_map())

        print("\nPressione [W] para mover para cima, [S] para baixo, [A] para esquerda e [D] para direita.")
        print("\nPressione [1] para voltar ao mapa principal")

        key = player.get_movement_input(game_map.largura, game_map.altura)

        # if key in ("w", "W", "s", "S", "a", "A", "d", "D"):
        #         enemy = roll_encounter(int(stage_choice), encounter_chance)
        #         if enemy:
        #             os.system('cls')
        #             encounter_chance = 0

        #             if combat(player, enemy):
        #                 continue
        #             else:
        #                 return

        #         else:
        #             encounter_chance += 2

        # elif key == '1':
        #      return

        game_map.update_map(player.pos, player.marker)'''

    