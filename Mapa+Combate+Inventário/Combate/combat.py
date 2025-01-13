from character import *
from item import * 
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
                #definir drop items para cada fase e fazer condicional com randint
                '''
                    drop_items_1 = []
                    if fase 1:
                        roll = random.randint(1,100) 
                            if roll <= drop_chance:
                            drop_item = random.choice(drop_items_1)
                    else:
                        print("O inimigo não dropou loot.")
                '''
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
#opçao de usar item
#integrar item drop no combate

#Implementar método para escolher um inimigo aleatorio da lista de inimigos ao iniciar combate baseado no terreno
    #ideias:
    #enemy = random.choice(enemy_list_fase_1)

