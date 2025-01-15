#classe para todos os itens
class Item:
    def __init__(self, name: str, gold_value: int, equipable: bool):
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable

    def __str__(self): #define que objeto vai ser representado como string 
        return self.name

#subclasse: armaduras
class Armor(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, def_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.def_value = def_value

armor = Armor(name = "Armadura de Ferro", gold_value = 5, equipable = True, def_value = 2)

#subclasse: armas
class Weapon(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, atk_value: int):
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
    def __init__(self, name: str, gold_value: int, equipable: bool, hp_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.hp_value = hp_value

maça = ItemCura(name = "Maçã", gold_value = 2, equipable = False, hp_value = 2)

#subclasse: ouro
class Ouro(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable

ouro = Ouro(name = "Ouro", gold_value = 1, equipable = False)


#listas de drop items por fase
drop_items_1 = [espada, porrete, adaga, maça]

#itens de quest
item_quest_1 = "Amuleto da Floresta" #amuleto mágico protegido pelos espíritos da floresta, abre um portal que conecta a floresta ao deserto
item_quest_2 = "Fragmento do Coração do Faraó" #fragmento do colar do faraó antigoque abre o túmulo sagrado debaixo das dunas
item_quest_3 = "Cristal Congelado" #cristal de gelo raro necessário para alimentar uma antiga fonte de energia congelada e abre uma passagem para o pântano
item_quest_4 = "Pergaminho do Fogo Eterno" #revela um mapa secreto para a fase final.