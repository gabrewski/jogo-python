from character import *
from weapon import * 
import os

def combat_encounter(player, enemy):
    while True:
        os.system("cls")
        player.attack(enemy)
        enemy.attack(player)
        if player.hp==0: 
            print ("Batalha perdida")
            break
        elif enemy.hp==0:
            print("Batalha vencida")
            break
    
        print(f"Vida do {player.name}: {player.hp}")
        print(f"Vida do {enemy.name}: {enemy.hp}")
        input()