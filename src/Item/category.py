#category.py

class Item:
    '''
    Classe base para todos os itens.
    '''
    def __init__(self, name: str, gold_value: int, equipable: bool, consumable: bool, tradable: bool):
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.consumable = consumable
        self.tradable = tradable

    def __str__(self): #define que objeto vai ser representado como string 
        return self.name


class Armor(Item):
    def __init__(self, name: str, gold_value: int, def_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = True, consumable = False, tradable = True)
        self.def_value = def_value


class Weapon(Item):
    def __init__(self, name: str, gold_value: int, atk_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = True, consumable = False, tradable = True)
        self.atk_value = atk_value


class Healing(Item):
    def __init__(self, name: str, gold_value: int, hp_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = False, consumable = True, tradable = True)
        self.hp_value = hp_value


class QuestItem(Item):
    def __init__(self, name: str, description: str):
        super().__init__(name = name, gold_value = 0, equipable = False, consumable = False, tradable = False)
        self.description = description