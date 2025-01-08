from character import *
from weapon import *
import os


main_character = Character (name="Dargia", hp=100, atk=10)
enemy = Character (name="Enemy", hp=100, atk=3)

while True:
    os.system("cls")
    main_character.attack(enemy)
    enemy.attack(main_character)
    if main_character.hp==0: 
        print ("Batalha perdida")
        break
    elif enemy.hp==0:
        print("Batalha vencida")
        break
    
    print(f"Vida do {main_character.name}: {main_character.hp}")
    print(f"Vida do {enemy.name}: {enemy.hp}")
    input()
    
#To do list:
#Transformar o combate em batalha por turnos
#Implementar defesa como atributo
#Elaborar a formula de defesa
#Implementar combate na exploração do mapa
#Implementar encontros de combate aleatórios ao explorar o mapa
#Preencher lista de inimigos
#Implementar método para escolher um inimigo aleatorio da lista de inimigos ao iniciar combate baseado no terreno.
#Elaborar interface de exploração de mapa
#Elaborar interface de combate e/ou vincula-la na interface de exploração de mapa.