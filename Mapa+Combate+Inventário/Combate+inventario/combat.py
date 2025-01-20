from character import *
from item import * 
from inventario import *
import os
import time
import random

def display_stats(player, enemy):
    print(f"Vida de {player.name}: {player.hp}")
    print(f"Vida de {enemy.name}: {enemy.hp}")

def get_player_choice():
    try:
        opt = int(input("\nO que deseja fazer? "))
        return opt
    except ValueError:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        return None
    
def atk_action(player, enemy):
    player.attack(enemy)
    enemy.attack(player)
    if player.hp == 0:
        print("\nBatalha perdida.")
        return False
    elif enemy.hp == 0:
        print("\nBatalha vencida.")
        enemy.drop_item(player)
        return False
    return True

'''def combat_encounter(player, enemy):
    while True:
        os.system("cls")
        print("Batalha em andamento!\n") 
        display_stats(player, enemy)
        print("\nAtacar (1)\nDefender (2)\nUsar item (3)\nFugir (4)")
        
        opt = get_player_choice()
        if opt is None:
            continue #input inválido, reinicia o loop

        if opt==1:
            if not atk_action(enemy):
                break #termina o combate ao fim da batalha
        elif opt==2:
            player.defend(enemy)
            time.sleep(1)
        elif opt==3: 
            player.use_item()
            time.sleep(1)
        elif opt == 4:
            print("Você fugiu da batalha.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)'''
        

#To do list:
#opçao de usar item
#integrar item drop no combate

#Implementar método para escolher um inimigo aleatorio da lista de inimigos ao iniciar combate baseado no terreno
    #ideias:
    #enemy = random.choice(enemy_list_fase_1)

