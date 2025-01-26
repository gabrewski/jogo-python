#main.py (Map Main)
#
import os
from Mapa.map_stages import *
from Mapa.tile import *
from Mapa.map import *
import msvcrt


class Exploration:
    def __init__(self, size:tuple[int, int]) -> bool:
        self.maps = (ForestMap(*size), DesertMap(*size), SnowMap(*size), SwampMap(*size), FireMap(*size))


    def map_loop(self, player, stage_choice:int, interface, window):
        game_map = self.maps[stage_choice-1]
        encounter_chance = 0

        while True:
            interface(game_map.display_map())
            key = window.getch() # Pega a tecla pressionada
            key_char = chr(key).lower() if key != -1 else '' # Converte a tecla para string
            
            if key_char == 'm': # Voltar para o mapa principal 
                return False 
            
            # Movimentação do jogador
            if key_char in ('w', 'a', 's', 'd'): 
                
                new_pos = player.pos.copy()
                if key_char == 'w': new_pos[1] -= 1
                elif key_char == 's': new_pos[1] += 1
                elif key_char == 'a': new_pos[0] -= 1
                elif key_char == 'd': new_pos[0] += 1
                
                if 0 <= new_pos[0] < game_map.largura and 0 <= new_pos[1] < game_map.altura:
                    player.pos = new_pos

                if randint(1, 1000) <= encounter_chance:
                    return True
                else:
                    encounter_chance += 2
            
            game_map.update_map(player.pos, player.marker)