from character import *
from item import *
from combat_interface import *
from inventario import *
import curses

player = Character (name="Dargia", hp=100, atk=20, crit_chance=0.4, crit_damage=2.0)
enemy = Character (name="Goblin", hp=100, atk=20, crit_chance=0.4, crit_damage=2.0)


#To do list:
#Implementar combate na exploração do mapa
#Implementar encontros de combate aleatórios ao explorar o mapa
#Elaborar interface de exploração de mapa
#Elaborar interface de combate e/ou vincula-la na interface de exploração de mapa.


#pesos para cada inimigo e chance de dropar item
#interface de combate: stats jogadores, opções, animação de ações, animação de barra de hp