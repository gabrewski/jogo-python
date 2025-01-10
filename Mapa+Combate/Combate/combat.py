from character import *
from weapon import * 
import os

def combat_encounter(player, enemy):
    while True:
        os.system("cls")
        print("Batalha iniciada!\n")
        
        player.attack(enemy)
        enemy.attack(player)
    
        print(f"Vida do {player.name}: {player.hp}")
        print(f"Vida do {enemy.name}: {enemy.hp}\n")
        print("\nAtacar (1)\nGuarda (2)\nFugir (3)\n")
        opt = input("O que deseja fazer? ")
        
        if opt==1:
            player.attack(enemy)
            enemy.attack(player)
            if player.hp==0: 
                print ("Batalha perdida")
                break
            elif enemy.hp==0:
                print("Batalha vencida")
                break
        elif opt==2:
            player.defense()
        else:
            print("Você fugiu da batalha.")
            break
        

#To do list:
#Opções de combate:
#>Atacar (Chance de acerto critico (10%) - 100% de dano extra)
#>Guarda (100% ou % alta de redução de dano)
#>Item - Criar classe de item para ser usada no meio do combate: P
#>Fugir (Termina o combate)
