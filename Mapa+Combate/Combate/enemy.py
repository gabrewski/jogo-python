from character import *

class Enemy(Character):
    def __init__(self, name: str, hp:int) -> None:
        super().__init_(name=name, hp = hp)

#Lista de inimigos segmentada por fases
    enemy_list_fase_1=[
        {"name": "Goblin", "hp": 0, "def": 0, "tiles": "xx", "xp-range": 00-00, "gold-range": 00-00}
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