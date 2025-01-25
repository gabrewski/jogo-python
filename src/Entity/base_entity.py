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
        target.hp -= atk_damage
        target.hp = max(target.hp, 0)

        return (atk_damage, crit)


    def defend(self, attacker: 'Entity') -> tuple[int, bool]:
        defend = random.random() <= 0.6
        def_damage = 0

        if not defend:
            def_damage = attacker.atk_value - self.armor.def_value
            self.hp -= max(def_damage, 0)
            self.hp = max(self.hp, 0)

        return (def_damage, defend)