#item_list.py

from Item.category import Armor, Weapon, Healing, QuestItem


#armaduras
armor1 = Armor(name = "Armadura de Ferro", gold_value = 15, def_value = 5)
armor2 = Armor(name = "Armadura de Aço", gold_value = 30, def_value = 15)
armor3 = Armor(name = "Armadura de Platina", gold_value = 80, def_value = 40)
armor4 = Armor(name = "Armadura Divina", gold_value = 120, def_value = 80)
no_armor = Armor(name = "none", gold_value = 0, def_value = 0)

#armas equipáveis
espada1 = Weapon(name="Espada de Ferro", gold_value = 5, atk_value=5)
espada2 = Weapon(name="Espada de Aço", gold_value = 5, atk_value=5)
espada3 = Weapon(name="Espada Longa", gold_value = 5, atk_value=5)
porrete = Weapon(name="Porrete de Madeira", gold_value = 5, atk_value=2)
adaga = Weapon(name="Adaga de Aço", gold_value = 5, atk_value=3)                                
arco = Weapon(name="Arco e Flecha", gold_value = 5, atk_value=4)
machado = Weapon(name="Machado", gold_value = 5, atk_value=5)
cimitarra = Weapon(name="Cimitarra", gold_value=30, atk_value=25)
clava_gelo = Weapon(name="Clava de Gelo", gold_value=30, atk_value=40)
espada_flamejante = Weapon(name="Espada Flamejante", gold_value=150, atk_value=120)

#armas de inimigos
garras = Weapon(name="Garras", gold_value=0, atk_value=15)
magia = Weapon(name="Magia", gold_value=0, atk_value=12)
veneno = Weapon(name="Veneno", gold_value=0, atk_value=20)
cauda_veneno = Weapon(name="Cauda de Veneno", gold_value=0, atk_value=30)
lamina_escama = Weapon(name="Lâmina de Escama", gold_value=0, atk_value=35)
areia_solida = Weapon(name="Areia Sólida", gold_value=0, atk_value=40)
golpes_areia = Weapon(name="Golpes de Areia", gold_value=0, atk_value=45)
garras_gelo = Weapon(name="Garras de Gelo", gold_value=0, atk_value=45)
garras_gigantes = Weapon(name="Garras Gigantes", gold_value=0, atk_value=50)
mandibulas = Weapon(name="Mandíbulas", gold_value=0, atk_value=60)
raizes = Weapon(name="Raízes", gold_value=0, atk_value=55)
cabecas_veneno = Weapon(name="Cabeças de Veneno", gold_value=0, atk_value=70)
chamas_incandescentes = Weapon(name="Chamas Incandescentes", gold_value=0, atk_value=90)
magia_fogo = Weapon(name="Magia de Fogo", gold_value=0, atk_value=75)
erupcoes_lava = Weapon(name="Erupções de Lava", gold_value=0, atk_value=100)
sopro_lava = Weapon(name="Sopro de Lava", gold_value=0, atk_value=150)

#itens de cura
potion1 = Healing(name = "Poção Revigorante", gold_value = 8, hp_value = 8)
potion2 = Healing(name = "Poção de Cura Leve", gold_value = 15, hp_value = 15)
potion3 = Healing(name = "Poção de Cura Poderosa", gold_value = 30, hp_value = 30)
potion4 = Healing(name = "Poção de Cura Suprema", gold_value = 60, hp_value = 60)

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