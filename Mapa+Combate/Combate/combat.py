from character import *
from weapon import * 
import os
import time

def combat_encounter(player, enemy):
    while True:
        os.system("cls")
        print("Batalha em andamento!\n") 
        print(f"Vida de {player.name}: {player.hp}")
        print(f"Vida de {enemy.name}: {enemy.hp}")
        print("\nAtacar (1)\nDefender (2)\nUsar item (3)\nFugir(4)")
        
        try: #safeguard contra input que não pode ser convertido em int
            opt = int(input("O que deseja fazer? "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
            continue

        if opt==1:
            player.attack(enemy)
            enemy.attack(player)
            if player.hp==0: 
                print ("Batalha perdida.")
                break
            elif enemy.hp==0:
                print("Batalha vencida.")
                break
            time.sleep(1) 
            continue
        elif opt==2:
            player.defend(enemy)
            time.sleep(1)
        elif opt==3: 
            self.use_item()
        elif opt == 4:
            print("Você fugiu da batalha.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
        

#To do list:
#Opções de combate: 
#>Atacar (Chance de acerto critico (10%) - 100% de dano extra) x
#>Guarda (100% ou % alta de redução de dano) x 
#>Item - Criar classe de item para ser usada no meio do combate: P
#>Fugir (Termina o combate) x
