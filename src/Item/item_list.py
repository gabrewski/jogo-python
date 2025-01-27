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
espada2 = Weapon(name="Espada de Aço", gold_value = 5, atk_value=20)
espada3 = Weapon(name="Espada Longa", gold_value = 5, atk_value=30)
porrete = Weapon(name="Porrete de Madeira", gold_value = 5, atk_value=8)
adaga = Weapon(name="Adaga de Aço", gold_value = 5, atk_value=10)                                
arco = Weapon(name="Arco e Flecha", gold_value = 5, atk_value=17)
machado = Weapon(name="Machado", gold_value = 5, atk_value=32)
cimitarra = Weapon(name="Cimitarra", gold_value=30, atk_value=45)
clava_gelo = Weapon(name="Clava de Gelo", gold_value=30, atk_value=85)
espada_flamejante = Weapon(name="Espada Flamejante", gold_value=150, atk_value=120)

#armas de inimigos
garras = Weapon(name="Garras", gold_value=0, atk_value=0)

#itens de cura
potion1 = Healing(name = "Poção Revigorante", gold_value = 8, hp_value = 50)
potion2 = Healing(name = "Poção de Cura Leve", gold_value = 15, hp_value = 75)
potion3 = Healing(name = "Poção de Cura Poderosa", gold_value = 30, hp_value = 100)
potion4 = Healing(name = "Poção de Cura Suprema", gold_value = 60, hp_value = 200)

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

#itens da loja
armor_loja = [armor1, armor2, armor3, armor4]
weapon_loja = [espada1, espada2, espada3, porrete, adaga, arco, machado, cimitarra, clava_gelo, espada_flamejante]
potion_loja = [potion1, potion2, potion3, potion4]
