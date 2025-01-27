#enemy_list.py

from Entity.enemy import Enemy
from Item.item_list import *


#inimigos da fase 1
goblin = Enemy(name="Goblin", 
               hp=30, 
               atk_value=15, 
               crit_chance=0.2, 
               crit_damage=1.5, 
               weapon=garras,
               exp_range=(10,15),
               gold_range=(5,10))

lobo = Enemy(name="Lobo", 
             hp=50, 
             atk_value=17, 
             crit_chance=0.15, 
             crit_damage=1.8, 
             weapon=garras,
             exp_range=(15,25),
             gold_range=(7,12))

pixie = Enemy(name="Pixie", 
              hp=20, 
              atk_value=10, 
              crit_chance=0.3, 
              crit_damage=2.0, 
              weapon=garras,
              exp_range=(8,12),
              gold_range=(4,6))

aranha_gigante = Enemy(name="Aranha Gigante", 
                       hp=70, 
                       atk_value=20, 
                       crit_chance=0.1, 
                       crit_damage=2.5, 
                       weapon=garras,
                       exp_range=(20,30),
                       gold_range=(10,15))

mestre_aranhas = Enemy(name="Mestre das Aranhas", 
                       hp=150, 
                       atk_value=23, 
                       crit_chance=0.2, 
                       crit_damage=2.0, 
                       weapon=garras,
                       exp_range=(50,70),
                       gold_range=(20,30))

#inimigos da fase 2
escorpiao_gigante = Enemy(name="Escorpião Gigante", 
                          hp=100, 
                          atk_value=20, 
                          crit_chance=0.25, 
                          crit_damage=2.2, 
                          weapon=garras,
                          exp_range=(30,50),
                          gold_range=(20,30))

reptiliano = Enemy(name="Reptiliano", 
                   hp=120, 
                   atk_value=22, 
                   crit_chance=0.18, 
                   crit_damage=1.8, 
                   weapon=garras,
                   exp_range=(40,60),
                   gold_range=(18,25))

bandido_deserto = Enemy(name="Bandido do Deserto", 
                        hp=80, 
                        atk_value=18, 
                        crit_chance=0.2, 
                        crit_damage=2.0, 
                        weapon=garras,
                        exp_range=(25,40),
                        gold_range=(12,18))

golem_areia = Enemy(name="Golem de Areia", 
                    hp=150, 
                    atk_value=25, 
                    crit_chance=0.15, 
                    crit_damage=2.5, 
                    weapon=garras,
                    exp_range=(50,75),
                    gold_range=(20,35))

farao_esquecido = Enemy(name="Faraó Esquecido", 
                        hp=300, 
                        atk_value=32, 
                        crit_chance=0.1, 
                        crit_damage=3.0, 
                        weapon=garras,
                        exp_range=(100,150),
                        gold_range=(40,60))

#inimigos da fase 3
troll_gelo = Enemy(name="Troll de Gelo", 
                   hp=150, 
                   atk_value=25, 
                   crit_chance=0.2, 
                   crit_damage=2.0, 
                   weapon=garras,
                   exp_range=(50,75),
                   gold_range=(25,30))

urso_polar = Enemy(name="Urso Polar", 
                   hp=90, 
                   atk_value=30, 
                   crit_chance=0.15, 
                   crit_damage=1.8, 
                   weapon=garras,
                   exp_range=(30,50),
                   gold_range=(15,20))

yeti = Enemy(name="Yeti", 
             hp=120, 
             atk_value=28, 
             crit_chance=0.18, 
             crit_damage=2.2, 
             weapon=garras,
             exp_range=(40,60),
             gold_range=(20,30))

espirito_nevasca = Enemy(name="Espírito de Nevasca", 
                         hp=200, 
                         atk_value=35, 
                         crit_chance=0.12, 
                         crit_damage=2.8, 
                         weapon=garras,
                         exp_range=(60,90),
                         gold_range=(30,40))

wendigo_congelado = Enemy(name="Wendigo Congelado", 
                          hp=350, 
                          atk_value=43, 
                          crit_chance=0.1, 
                          crit_damage=3.0, 
                          weapon=garras,
                          exp_range=(120,180),
                          gold_range=(50,70))

#inimigos da fase 4
crocodilo_gigante = Enemy(name="Crocodilo Gigante", 
                          hp=250, 
                          atk_value=52, 
                          crit_chance=0.15, 
                          crit_damage=2.5, 
                          weapon=garras,
                          exp_range=(80,120),
                          gold_range=(35,50))

golem_pantano = Enemy(name="Golem do Pântano", 
                      hp=200, 
                      atk_value=55, 
                      crit_chance=0.12, 
                      crit_damage=2.2, 
                      weapon=garras,
                      exp_range=(70,100),
                      gold_range=(30,45))

hidra = Enemy(name="Hidra", 
              hp=300, 
              atk_value=68, 
              crit_chance=0.1, 
              crit_damage=2.8, 
              weapon=garras,
              exp_range=(100,150),
              gold_range=(40,60))

yeti_pantano = Enemy(name="Yeti", 
                     hp=250, 
                     atk_value=65, 
                     crit_chance=0.18, 
                     crit_damage=2.5, 
                     weapon=garras,
                     exp_range=(80,120),
                     gold_range=(35,50))

vidente_pantano = Enemy(name="Vidente do Pântano", 
                        hp=500, 
                        atk_value=77, 
                        crit_chance=0.05, 
                        crit_damage=3.5, 
                        weapon=garras,
                        exp_range=(150,250),
                        gold_range=(70,100))

#inimigos da fase 5
salamandra_vulcanica = Enemy(name="Salamandra Vulcânica", 
                             hp=350, 
                             atk_value=92, 
                             crit_chance=0.2, 
                             crit_damage=2.5, 
                             weapon=garras,
                             exp_range=(150,200),
                             gold_range=(50,80))

cultistas_fogo = Enemy(name="Cultistas do Fogo", 
                       hp=200, 
                       atk_value=76, 
                       crit_chance=0.18, 
                       crit_damage=2.2, 
                       weapon=garras,
                       exp_range=(100,150),
                       gold_range=(30,50))

elemental_magma = Enemy(name="Elemental de Magma", 
                        hp=400, 
                        atk_value=110, 
                        crit_chance=0.15, 
                        crit_damage=3.0, 
                        weapon=garras,
                        exp_range=(200,250),
                        gold_range=(60,90))

cavaleiro_inferno = Enemy(name="Cavaleiro do Inferno", 
                          hp=500, 
                          atk_value=137, 
                          crit_chance=0.1, 
                          crit_damage=3.5, 
                          weapon=garras,
                          exp_range=(250,300),
                          gold_range=(80,120))

dragao_magma = Enemy(name="Otsugua, o Dragão de Magma", 
                     hp=800, 
                     atk_value=166, 
                     crit_chance=0.05, 
                     crit_damage=4.0, 
                     weapon=garras,
                     exp_range=(500,750),
                     gold_range=(150,200))

#lista de inimigos por fase sem mini bosses
enemy_list1 = [(goblin, 0.8) , (lobo, 0.8), (pixie, 1.0), (aranha_gigante, 0.4), (mestre_aranhas, 0.1)]
enemy_list2 = [(escorpiao_gigante, 0.8), (reptiliano, 0.6), (bandido_deserto, 0.8), (golem_areia, 0.4), (farao_esquecido, 0.1)]
enemy_list3 = [(troll_gelo, 0.6), (urso_polar, 0.8), (yeti, 0.8), (espirito_nevasca, 0.4), (wendigo_congelado, 0.1)]
enemy_list4 = [(crocodilo_gigante, 0.8), (golem_pantano, 0.6), (hidra, 0.4), (yeti_pantano, 0.8), (vidente_pantano, 0.1)]
enemy_list5 = [(salamandra_vulcanica, 0.6), (cultistas_fogo, 0.8), (elemental_magma, 0.6), (cavaleiro_inferno, 0.4), (dragao_magma, 0.1)]