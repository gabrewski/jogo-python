from Entity.base_entity import Entity
from Item.inventory import Inventory
from Item.item_list import espada1, armor1
from Item.category import Weapon, Armor
import random


class Player (Entity):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_damage: float):
        super().__init__(name = name, hp = hp, atk=atk, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = espada1
        self.armor = armor1
        self.inventory = Inventory()

        # progressão
        self.exp = 0
        self.level = 1
        self.level_exp = {1:100, # exp necessário em cada nível
                          2:200, 
                          3:400, 
                          4:600, 
                          5:900, 
                          6:1200, 
                          7:1600, 
                          8:2000, 
                          9:2500}


    def gain_exp(self, exp_range:tuple[int, int]) -> tuple[bool, int] | None:
        '''
        Incrementa o exp do jogador.\n
        Ao atingir o limite de exp definido em 'level_exp', chama a função level_up().\n
        Chamar esta função ao finalizar o combate, e inserir o valor de 'exp_range' no formato (int, int)
        '''
        if self.level == 10: # nível max
            return

        exp_ganho = random.randint(*exp_range)
        self.exp += exp_ganho
        if self.exp >= self.level_exp[self.level]:
            self.exp = 0
            self.level_up()
            return (True, exp_ganho)
        else:
            return (False, exp_ganho)


    def level_up(self):
        '''Incrementa os atributos base do jogador.'''
        self.level += 1
        self.hp_max += 25
        self.atk += 10
        self.crit_chance += 0.1


    def gain_gold(self, gold_range:tuple[int, int]) -> int:
        '''
        Incrementa o gold do jogador.\n
        Chamar esta função ao finalizar o combate, e inserir o valor de 'gold_range' no formato (int, int)
        '''
        gold_ganho = random.randint(*gold_range)
        self.inventory.gold += gold_ganho
        return gold_ganho


    def display_info(self):
        print(f"Nome: {self.name}")
        print(f"HP: {self.hp}")
        if self.weapon is None:
            print(f"Ataque: {self.atk}")
        else:
            print(f"Ataque: {self.atk + self.weapon.atk_value}")
        print(f"Chance de Crítico: {self.crit_chance*10}%")
        print(f"Dano Crítico: {self.crit_damage}x")

    def equip_weapon(self, weapon: 'Weapon'):
        self.weapon = weapon
        print(f"'{weapon.name}' foi equipado como arma.")

    def equip_armor(self, armor: 'Armor'):
        self.armor = armor
        print(f"'{armor.name}' foi equipado como armadura.")


    def get_stats(self):
        return {"level": self.level,
                "hp": self.hp_max,
                "atk": self.atk_value + self.weapon.atk_value,
                "defense": self.def_value + self.armor.def_value,
                "exp": self.exp,
                "exp_to_next_level": self.level_exp[self.level] - self.exp}
