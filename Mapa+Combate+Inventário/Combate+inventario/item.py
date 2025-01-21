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

armor1 = Armor(name = "Armadura de Ferro", gold_value = 15, equipable = True, def_value = 5)
armor2 = Armor(name = "Armadura de Aço", gold_value = 30, equipable = True, def_value = 15)
armor3 = Armor(name = "Armadura de Platina", gold_value = 80, equipable = True, def_value = 40)
armor4 = Armor(name = "Armadura Divina", gold_value = 120, equipable = True, def_value = 80)


#subclasse: armas
class Weapon(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, atk_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.atk_value = atk_value

#armas equipáveis
espada1 = Weapon(name="Espada de Ferro", gold_value = 5, equipable = True, atk_value=5)
espada2 = Weapon(name="Espada de Aço", gold_value = 5, equipable = True, atk_value=5)
espada3 = Weapon(name="Espada Longa", gold_value = 5, equipable = True, atk_value=5)
porrete = Weapon(name="Porrete de Madeira", gold_value = 5, equipable = True, atk_value=2)
adaga = Weapon(name="Adaga de Aço", gold_value = 5, equipable = True, atk_value=3)                                
arco = Weapon(name="Arco e Flecha", gold_value = 5, equipable = True, atk_value=4)
machado = Weapon(name="Machado", gold_value = 5, equipable = True, atk_value=5)
cimitarra = Weapon(name="Cimitarra", gold_value=30, equipable=True, atk_value=25)
clava_gelo = Weapon(name="Clava de Gelo", gold_value=30, equipable=True, atk_value=40)
espada_flamejante = Weapon(name="Espada Flamejante", gold_value=150, equipable=True, atk_value=120)

#armas de inimigos
garras = Weapon(name="Garras", gold_value=None, equipable=False, atk_value=15)
magia = Weapon(name="Magia", gold_value=None, equipable=False, atk_value=12)
veneno = Weapon(name="Veneno", gold_value=None, equipable=False, atk_value=20)
cauda_veneno = Weapon(name="Cauda de Veneno", gold_value=None, equipable=False, atk_value=30)
lamina_escama = Weapon(name="Lâmina de Escama", gold_value=None, equipable=False, atk_value=35)
areia_solida = Weapon(name="Areia Sólida", gold_value=None, equipable=False, atk_value=40)
golpes_areia = Weapon(name="Golpes de Areia", gold_value=None, equipable=False, atk_value=45)
garras_gelo = Weapon(name="Garras de Gelo", gold_value=None, equipable=False, atk_value=45)
garras_gigantes = Weapon(name="Garras Gigantes", gold_value=None, equipable=False, atk_value=50)
mandibulas = Weapon(name="Mandíbulas", gold_value=None, equipable=False, atk_value=60)
raizes = Weapon(name="Raízes", gold_value=None, equipable=False, atk_value=55)
cabecas_veneno = Weapon(name="Cabeças de Veneno", gold_value=None, equipable=False, atk_value=70)
chamas_incandescentes = Weapon(name="Chamas Incandescentes", gold_value=None, equipable=False, atk_value=90)
magia_fogo = Weapon(name="Magia de Fogo", gold_value=None, equipable=False, atk_value=75)
erupcoes_lava = Weapon(name="Erupções de Lava", gold_value=None, equipable=False, atk_value=100)
sopro_lava = Weapon(name="Sopro de Lava", gold_value=None, equipable=False, atk_value=150)


#subclasse: itens de cura
class ItemCura(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool, hp_value: int):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable
        self.hp_value = hp_value

potion1 = ItemCura(name = "Poção Revigorante", gold_value = 8, equipable = False, hp_value = 8)
potion2 = ItemCura(name = "Poção de Cura Leve", gold_value = 15, equipable = False, hp_value = 15)
potion3 = ItemCura(name = "Poção de Cura Poderosa", gold_value = 30, equipable = False, hp_value = 30)
potion4 = ItemCura(name = "Poção de Cura Suprema", gold_value = 60, equipable = False, hp_value = 60)

#subclasse: ouro
class Ouro(Item):
    def __init__(self, name: str, gold_value: int, equipable: bool):
        super().__init__(name = name, gold_value = gold_value, equipable = equipable)
        self.name = name
        self.gold_value = gold_value
        self.equipable = equipable

ouro = Ouro(name = "Ouro", gold_value = 1, equipable = False)


#listas de drop items por fase
drop_items_1 = [espada1, porrete, armor1, armor2, potion1]
drop_items_2 = [espada2, adaga, armor2, armor3, potion2]
drop_items_3 = [espada3, arco, armor2, armor3, potion3]
drop_items_4 = [espada3, machado, armor3, armor4, potion4]

#itens de quest
item_quest_1 = "Amuleto da Floresta" #amuleto mágico protegido pelos espíritos da floresta, abre um portal que conecta a floresta ao deserto
item_quest_2 = "Fragmento do Coração do Faraó" #fragmento do colar do faraó antigoque abre o túmulo sagrado debaixo das dunas
item_quest_3 = "Cristal Congelado" #cristal de gelo raro necessário para alimentar uma antiga fonte de energia congelada e abre uma passagem para o pântano
item_quest_4 = "Pergaminho do Fogo Eterno" #revela um mapa secreto para a fase final.