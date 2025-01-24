#main.py

import os
from map_stages import *
from tile import *
from map import *
import msvcrt
from encounter import roll_encounter

os.system("cls")
map_larg, map_alt = 60, 15

player = Player_map()

def map_loop():
    stage_choice = input("Escolha a fase: 1 - Floresta, 2 - Deserto, 3 - Neve, 4 - Pântano, 5 - Fogo: ")

    if stage_choice == "1":
        game_map = ForestMap(60, 15)
    elif stage_choice == "2":
        game_map = DesertMap(60, 15)
    elif stage_choice == "3":
        game_map = SnowMap(60, 15)
    elif stage_choice == "4":   
        game_map = SwampMap(60, 15)
    elif stage_choice == "5":
        game_map = FireMap(60, 15)

    encounter_chance = 0

    while True:
        os.system("cls") 
        game_map.display_map()  
        print("\nPressione [W] para mover para cima, [S] para baixo, [A] para esquerda e [D] para direita.")
        print("\nPressione [1] para voltar ao mapa principal")

        if player.get_movement_input(game_map.largura, game_map.altura):
            enemy = roll_encounter(int(stage_choice), encounter_chance)
            if enemy:
                encounter_chance = 0

                # iniciar combate

            else:
                encounter_chance += 2

        game_map.update_map(player.pos, player.marker)

map_loop()

#Inserir chance de iniciar loop de combate
