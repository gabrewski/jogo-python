#classe para todos os itens
class Item:
    def __init__(self, name: str, gold_value: int, equipable: bool) -> None:
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable

#subclasse: armaduras
class Armor(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, def_value: int) -> None:
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.def_value = def_value

armor = Armor(name = "Armadura de Ferro", gold_value = 5, equipable = True, def_value = 2)

#subclasse: armas
class Weapon(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, atk_value: int) -> None:
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.atk_value = atk_value

espada = Weapon(name="Espada de Ferro", gold_value = 5, equipable = True, atk_value=5)

porrete = Weapon(name="Porrete de Madeira", gold_value = 5, equipable = True, atk_value=2)

adaga = Weapon(name="Adaga", gold_value = 5, equipable = True, atk_value=3)                                

arco = Weapon(name="Arco", gold_value = 5, equipable = True, atk_value=4)

grimório = Weapon(name="Grimório", gold_value = 5, equipable = True, atk_value=4)

punhos = Weapon(name="Punhos", gold_value = 5, equipable = True, atk_value=2)

#subclasse: itens de cura
class ItemCura(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, hp_value: int) -> None:
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.hp_value = hp_value

apple = ItemCura(nome = "Maçã", gold_value = 2, equipable = False, hp_value = 2)

#subclasse: ouro
class Ouro(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool) -> None:
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable

ouro = Ouro(name = "Ouro", gold_value = 1, equipable = False)
