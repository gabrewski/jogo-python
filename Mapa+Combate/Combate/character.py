from weapon import *
from armor import * 
from item import *
import random

#Classe para todos os personagens
class Character:
    def __init__(self, name: str, hp: int, atk: int, crit_chance: int, crit_rate: float):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.crit_chance = crit_chance
        self.crit_rate = crit_rate

    def attack(self, target) -> None:
        roll = random.randint(1,100) #determina se o ataque vai ser crítico
        if roll <= self.crit_chance:
            damage = int(round(self.atk + self.weapon.atk) * self.crit_rate)
            print("\nAtaque crítico!")
        else:
            damage = self.atk + self.weapon.atk
        target.hp -= damage
        target.hp = max(target.hp, 0)
        print(f"\n{self.name} deu {damage} de dano ao {target.name}.")

    def defend(self, target) -> None:
        damage = target.atk - self.armor.value
        self.hp -= damage
        self.hp = max(self.hp, 0)
        print(f"\n{self.name} defendeu o ataque, mas levou {damage} de dano.")
    
'''    def use_item(self) -> None:
        if item = potion:
            self.hp += self.potion.value
            self.hp = max(self.hp, 0)'''


#Classe do jogador
class Player (Character):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_rate: float) -> None:
        super().__init__(name = name, hp = hp, atk=atk, crit_chance = crit_chance, crit_rate = crit_rate)
        self.weapon = espada
        self.armor = armor
        self.item = potion


#Classe para inimigos
class Enemy(Character):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_rate: float) -> None:
        super().__init__(name=name, hp=hp, atk=atk, crit_chance = crit_chance, crit_rate = crit_rate)
        self.weapon=porrete

#Lista de inimigos segmentada por fases
    enemy_list_fase_1=[ #floresta
        {"name": "Goblin", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Lobo", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Pixie", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Aranha Gigante", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]
    enemy_list_fase_2=[ #deserto
        {"name": "Escorpião Gigante", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Reptiliano", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Bandido do Deserto", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Golem de Areia", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]
    enemy_list_fase_3=[ #tundra
        {"name": "Troll de Gelo", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Espírito de Nevasca", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Filhote de Dragão Branco", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Yeti", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]
    enemy_list_fase_4=[ #pântano
        {"name": "Crocodilo Gigante", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Golem do Pântano", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Hidra", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Yeti", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]
    enemy_list_fase_5=[ #vulcão
        {"name": "Boss", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00},
        {"name": "Cultistas do Fogo", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]

#adicionar mini-bosses