#enemy.py

from Entity.base_entity import Entity
from Item.category import Weapon
from Item.item_list import no_armor
import random


class Enemy(Entity):
    def __init__(self, 
                 name: str, 
                 hp:int, 
                 atk_value:int, 
                 crit_chance: int, 
                 crit_damage: float, 
                 weapon: 'Weapon', 
                 exp_range: tuple[int, int] = (0,0), 
                 gold_range: tuple[int, int] = (0,0)):
                 
        super().__init__(name=name, hp=hp, atk_value=atk_value, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = weapon
        self.armor = no_armor
        self.exp_range = exp_range
        self.gold_range = gold_range


    def __repr__(self):
        return self.name


    def take_action(self, player):
        atk = random.random() <= 0.5
        return atk

    # def drop_item(self, player):
    #     drop = random.choice(drop_items_1) #lista de itens de cada fase
    #     drop_gold = random.randint(5,50)
    #     print(f"O inimigo dropou {drop_gold} moedas e {drop}.")
    #     player.inventory.gold += drop_gold
    #     while True:
    #         opt = input("Adicionar item ao inventário?  Sim (S) / Não (N): ").strip().lower()
    #         if opt == "s":
    #             player.inventory.player_items.append(drop)
    #             print("O item foi adicionado ao iventário.")
    #             break
    #         elif opt == "n":
    #                 break
    #         else:
    #             print("Digite uma opção válida.")