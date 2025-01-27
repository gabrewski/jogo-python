#base_entity.py

import random

class Entity:
    def __init__(self, name: str, hp: int, atk_value: int, crit_chance: float, crit_damage: float):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk_value = atk_value
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage


    def attack(self, target: 'Entity') -> tuple[int, bool]:
        crit = random.random() <= self.crit_chance
        atk_damage = int((self.atk_value + self.weapon.atk_value) * (self.crit_damage if crit else 1))
        reduced_damage = max(atk_damage - target.armor.def_value, 0)
        target.hp -= reduced_damage
        target.hp = max(target.hp, 0)

        return (reduced_damage, crit)


    def defend(self: 'Entity') -> int:
        def_damage = 0

        return (def_damage)
    

    def revive(self):
        self.hp = self.hp_max
