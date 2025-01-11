from character import *
from item import *
from combat import *
import os


player = Player (name="Dargia", hp=100, atk=10, crit_chance = 50, crit_damage = 2)
enemy = Enemy (name="Goblin", hp=100, atk=5, crit_chance = 50, crit_damage = 1.5)

combat_encounter(player,enemy)

#To do list:
#Implementar combate na exploração do mapa
#Implementar encontros de combate aleatórios ao explorar o mapa
#Elaborar interface de exploração de mapa
#Elaborar interface de combate e/ou vincula-la na interface de exploração de mapa.