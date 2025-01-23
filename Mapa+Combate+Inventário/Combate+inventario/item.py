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
        super().__init__(name = name, gold_value = gold_value, equipable = True, consumable = False, tradable = bool)
        self.atk_value = atk_value
        self.tradable = tradable


class Healing(Item):
    def __init__(self, name: str, gold_value: int, hp_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = False, consumable = True, tradable = True)
        self.hp_value = hp_value


class QuestItem(Item):
    def __init__(self, name: str, description: str):
        super().__init__(name = name, gold_value = 0, equipable = False, consumable = False, tradable = False)
        self.description = description


#armaduras
armor1 = Armor(name = "Armadura de Ferro", gold_value = 15, def_value = 5, tradable = True)
armor2 = Armor(name = "Armadura de Aço", gold_value = 30, def_value = 15, tradable = True)
armor3 = Armor(name = "Armadura de Platina", gold_value = 80, def_value = 40, tradable = True)
armor4 = Armor(name = "Armadura Divina", gold_value = 120, def_value = 80, tradable = True)
no_armor = Armor(name = "none", gold_value = 0, def_value = 0, tradable = True)

#armas equipáveis
espada1 = Weapon(name="Espada de Ferro", gold_value = 5, atk_value=5, tradable = True)
espada2 = Weapon(name="Espada de Aço", gold_value = 5, atk_value=5, tradable = True)
espada3 = Weapon(name="Espada Longa", gold_value = 5, atk_value=5, tradable = True)
porrete = Weapon(name="Porrete de Madeira", gold_value = 5, atk_value=2, tradable = True)
adaga = Weapon(name="Adaga de Aço", gold_value = 5, atk_value=3, tradable = True)                                
arco = Weapon(name="Arco e Flecha", gold_value = 5, atk_value=4, tradable = True)
machado = Weapon(name="Machado", gold_value = 5, atk_value=5, tradable = True)
cimitarra = Weapon(name="Cimitarra", gold_value=30, atk_value=25, tradable = True)
clava_gelo = Weapon(name="Clava de Gelo", gold_value=30, atk_value=40, tradable = True)
espada_flamejante = Weapon(name="Espada Flamejante", gold_value=150, atk_value=120, tradable = True)

#armas de inimigos
garras = Weapon(name="Garras", gold_value=None, atk_value=15, tradable = False)
magia = Weapon(name="Magia", gold_value=None, atk_value=12), tradable = False
veneno = Weapon(name="Veneno", gold_value=None, atk_value=20)
cauda_veneno = Weapon(name="Cauda de Veneno", gold_value=None, atk_value=30, tradable = False)
lamina_escama = Weapon(name="Lâmina de Escama", gold_value=None, atk_value=35, tradable = False)
areia_solida = Weapon(name="Areia Sólida", gold_value=None, atk_value=40, tradable = False)
golpes_areia = Weapon(name="Golpes de Areia", gold_value=None, atk_value=45, tradable = False)
garras_gelo = Weapon(name="Garras de Gelo", gold_value=None, atk_value=45, tradable = False)
garras_gigantes = Weapon(name="Garras Gigantes", gold_value=None, atk_value=50, tradable = False)
mandibulas = Weapon(name="Mandíbulas", gold_value=None, atk_value=60, tradable = False)
raizes = Weapon(name="Raízes", gold_value=None, atk_value=55, tradable = False)
cabecas_veneno = Weapon(name="Cabeças de Veneno", gold_value=None, atk_value=70, tradable = False)
chamas_incandescentes = Weapon(name="Chamas Incandescentes", gold_value=None, atk_value=90, tradable = False)
magia_fogo = Weapon(name="Magia de Fogo", gold_value=None, atk_value=75, tradable = False)
erupcoes_lava = Weapon(name="Erupções de Lava", gold_value=None, atk_value=100, tradable = False)
sopro_lava = Weapon(name="Sopro de Lava", gold_value=None, atk_value=150, tradable = False)

#itens de cura
potion1 = Healing(name = "Poção Revigorante", gold_value = 8, hp_value = 8, tradable = False)
potion2 = Healing(name = "Poção de Cura Leve", gold_value = 15, hp_value = 15, tradable = False)
potion3 = Healing(name = "Poção de Cura Poderosa", gold_value = 30, hp_value = 30, tradable = False)
potion4 = Healing(name = "Poção de Cura Suprema", gold_value = 60, hp_value = 60, tradable = False)

#listas de drop items por fase
drop_items_1 = [espada1, porrete, armor1, armor2, potion1]
drop_items_2 = [espada2, adaga, armor2, armor3, potion2]
drop_items_3 = [espada3, arco, armor2, armor3, potion3]
drop_items_4 = [espada3, machado, armor3, armor4, potion4]

#itens de quest
item_quest_1 = QuestItem(name = "Amuleto da Floresta",
                         description = "Amuleto mágico protegido pelos espíritos da floresta, abre um portal que conecta a floresta ao deserto.")

item_quest_2 = QuestItem(name = "Fragmento do Coração do Faraó",
                         description = "Fragmento do colar do faraó antigo que abre o túmulo sagrado debaixo das dunas.")

item_quest_3 = QuestItem(name = "Cristal Congelado", 
                         description = "Cristal de gelo raro necessário para alimentar uma antiga fonte de energia congelada e abre uma passagem para o pântano.")

item_quest_4 = QuestItem(name = "Pergaminho do Fogo Eterno",
                         description = "Revela um mapa secreto para a fase final.")