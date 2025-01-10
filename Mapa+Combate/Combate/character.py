from weapon import * 

#Classe para todos os personagens
class Character:
    def __init__(self, name: str, hp: int, atk: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk

    def attack(self, target) -> None:
        target.hp -= self.atk + self.weapon.atk
        target.hp = max(target.hp, 0)
        print(f"{self.name} deu {self.atk + self.weapon.atk} de dano ao {target.name}")

#Classe do jogador
class Player (Character):
    def __init__(self, name: str, hp:int, atk:int) -> None:
        super().__init__(name = name, hp = hp, atk=atk)
        self.weapon=espada

#Classe para inimigos
class Enemy(Character):
    def __init__(self, name: str, hp:int, atk:int) -> None:
        super().__init__(name=name, hp=hp, atk=atk)
        self.weapon=espada

#Lista de inimigos segmentada por fases
    enemy_list_fase_1=[
        {"name": "Goblin", "hp": 0, "def": 0, "Weapon": "xx", "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
    ]
    enemy_list_fase_2=[
        {"name": "Goblin"}
    ]
    enemy_list_fase_3=[
        {"name": "Goblin"}
    ]
    enemy_list_fase_4=[
        {"name": "Goblin"}
    ]
    enemy_list_fase_5=[
        {"name": "Goblin"}
    ]

