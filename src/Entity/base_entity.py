import random


class Entity:
    def __init__(self, name: str, hp: int, atk: int, crit_chance: float, crit_damage: float):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage

    def attack(self, target):
        crit = random.random() <= self.crit_chance
        atk_damage = int(round(self.atk + self.weapon.atk_value) * self.crit_damage) if crit else (self.atk + self.weapon.atk_value)
        target.hp -= atk_damage
        target.hp = max(target.hp, 0)
        return atk_damage, crit

    def defend(self, target):
        defend = random.random() <= 0.6
        def_damage = target.atk - self.armor.def_value if defend else target.atk
        self.hp -= def_damage
        self.hp = max(self.hp, 0)
        return def_damage, defend

    def flee(self):
        flee = random.random() <= 0.7
        return flee       