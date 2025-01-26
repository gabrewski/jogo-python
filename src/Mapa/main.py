#main.py (Map Main)
#
import os
from Mapa.map_stages import *
from Mapa.tile import *
from Mapa.map import *
from Mapa.encounter import roll_encounter
from Interface.main import *
from Combat.combat_test import combat
import msvcrt


# Função que roda o loop principal do modo de exploração de mapa aleatório 
def map_loop(player, stage_choice:int, size:tuple[int, int], interface, stdscr):
    maps = (ForestMap(*size), DesertMap(*size), SnowMap(*size), SwampMap(*size), FireMap(*size))
    game_map = maps[stage_choice-1]
    encounter_chance = 0
    
    # Função que desenha a interface do modo de exploração 
    while True: # Loop principal do modo de exploração
        interface(game_map.display_map()) # Desenha o mapa
        key = stdscr.getch() # Pega a tecla pressionada
        key_char = chr(key).lower() if key != -1 else '' # Converte a tecla para string
        
        if key_char == 'm': # Voltar para o mapa principal 
            break 
        
        
        # Movimentação do jogador
        if key_char in ('w', 'a', 's', 'd'): 
            
            new_pos = player.pos.copy()
            if key_char == 'w': new_pos[1] -= 1
            elif key_char == 's': new_pos[1] += 1
            elif key_char == 'a': new_pos[0] -= 1
            elif key_char == 'd': new_pos[0] += 1
            
            if 0 <= new_pos[0] < game_map.largura and 0 <= new_pos[1] < game_map.altura:
                player.pos = new_pos

        
        game_map.update_map(player.pos, player.marker)

'''# Função que roda o loop principal do modo de exploração de mapa aleatório 
def map_loop(player, stage_choice:int, size:tuple[int, int], interface):
    maps = (ForestMap(*size), DesertMap(*size), SnowMap(*size), SwampMap(*size), FireMap(*size))
    game_map = maps[stage_choice-1]
    encounter_chance = 0

    while True:
        interface(game_map.display_map())

        print("\nPressione [W] para mover para cima, [S] para baixo, [A] para esquerda e [D] para direita.")

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
