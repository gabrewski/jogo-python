from item import *
from inventario import *
import random

#Classe para todos os personagens
class Character:
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

#Classe do jogador
class Player (Character):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_damage: float):
        super().__init__(name = name, hp = hp, atk=atk, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = espada1
        self.armor = armor1
        self.inventory = player_inventory

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

    def equip_weapon(self, weapon: Item):
        self.weapon = weapon
        print(f"'{weapon.name}' foi equipado como arma.")

    def equip_armor(self, armor: Item):
        self.armor = armor
        print(f"'{armor.name}' foi equipado como armadura.")

    def use_item(self):
        potions = [item for item in self.inventory.player_items if item.consumable]
        return potions
    

#Classe para inimigos
class Enemy(Character):
    def __init__(self, 
                 name: str, 
                 hp:int, 
                 atk:int, 
                 crit_chance: int, 
                 crit_damage: float, 
                 weapon: Weapon, 
                 exp_range: tuple[int, int] = (0,0), 
                 gold_range: tuple[int, int] = (0,0)):
                 
        super().__init__(name=name, hp=hp, atk=atk, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = weapon
        self.armor = no_armor
        self.exp_range = exp_range
        self.gold_range = gold_range

    def take_action(self, player):
        atk = random.random() <= 0.5
        return atk

    def drop_item(self, player):
        drop = random.choice(drop_items_1) #lista de itens de cada fase
        drop_gold = random.randint(5,50)
        print(f"O inimigo dropou {drop_gold} moedas e {drop}.")
        player.inventory.gold += drop_gold
        while True:
            opt = input("Adicionar item ao inventário?  Sim (S) / Não (N): ").strip().lower()
            if opt == "s":
                player.inventory.player_items.append(drop)
                print("O item foi adicionado ao iventário.")
                break
            elif opt == "n":
                    break
            else:
                print("Digite uma opção válida.")

#inimigos da fase 1
goblin = Enemy(name="Goblin", 
               hp=30, 
               atk=15, 
               crit_chance=0.2, 
               crit_damage=1.5, 
               weapon=adaga,
               exp_range=(10,15),
               gold_range=(5,10))

lobo = Enemy(name="Lobo", 
             hp=50, 
             atk=20, 
             crit_chance=0.15, 
             crit_damage=1.8, 
             weapon=garras,
             exp_range=(15,25),
             gold_range=(7,12))

pixie = Enemy(name="Pixie", 
              hp=20, 
              atk=10, 
              crit_chance=0.3, 
              crit_damage=2.0, 
              weapon=magia,
              exp_range=(8,12),
              gold_range=(4,6))

aranha_gigante = Enemy(name="Aranha Gigante", 
                       hp=70, 
                       atk=25, 
                       crit_chance=0.1, 
                       crit_damage=2.5, 
                       weapon=veneno,
                       exp_range=(20,30),
                       gold_range=(10,15))

mestre_aranhas = Enemy(name="Mestre das Aranhas", 
                       hp=150, 
                       atk=35, 
                       crit_chance=0.2, 
                       crit_damage=2.0, 
                       weapon=machado,
                       exp_range=(50,70),
                       gold_range=(20,30))

#inimigos da fase 2
escorpiao_gigante = Enemy(name="Escorpião Gigante", 
                          hp=100, 
                          atk=30, 
                          crit_chance=0.25, 
                          crit_damage=2.2, 
                          weapon=cauda_veneno,
                          exp_range=(30,50),
                          gold_range=(20,30))

reptiliano = Enemy(name="Reptiliano", 
                   hp=120, 
                   atk=40, 
                   crit_chance=0.18, 
                   crit_damage=1.8, 
                   weapon=lamina_escama,
                   exp_range=(40,60),
                   gold_range=(18,25))

bandido_deserto = Enemy(name="Bandido do Deserto", 
                        hp=80, 
                        atk=25, 
                        crit_chance=0.2, 
                        crit_damage=2.0, 
                        weapon=cimitarra,
                        exp_range=(25,40),
                        gold_range=(12,18))

golem_areia = Enemy(name="Golem de Areia", 
                    hp=150, 
                    atk=50, 
                    crit_chance=0.15, 
                    crit_damage=2.5, 
                    weapon=areia_solida,
                    exp_range=(50,75),
                    gold_range=(20,35))

farao_esquecido = Enemy(name="Faraó Esquecido", 
                        hp=300, 
                        atk=70, 
                        crit_chance=0.1, 
                        crit_damage=3.0, 
                        weapon=golpes_areia,
                        exp_range=(100,150),
                        gold_range=(40,60))

#inimigos da fase 3
troll_gelo = Enemy(name="Troll de Gelo", 
                   hp=150, 
                   atk=40, 
                   crit_chance=0.2, 
                   crit_damage=2.0, 
                   weapon=clava_gelo,
                   exp_range=(50,75),
                   gold_range=(25,30))

urso_polar = Enemy(name="Urso Polar", 
                   hp=90, 
                   atk=35, 
                   crit_chance=0.15, 
                   crit_damage=1.8, 
                   weapon=garras_gigantes,
                   exp_range=(30,50),
                   gold_range=(15,20))

yeti = Enemy(name="Yeti", 
             hp=120, 
             atk=45, 
             crit_chance=0.18, 
             crit_damage=2.2, 
             weapon=garras_gelo,
             exp_range=(40,60),
             gold_range=(20,30))

espirito_nevasca = Enemy(name="Espírito de Nevasca", 
                         hp=200, 
                         atk=55, 
                         crit_chance=0.12, 
                         crit_damage=2.8, 
                         weapon=garras_gigantes,
                         exp_range=(60,90),
                         gold_range=(30,40))

wendigo_congelado = Enemy(name="Wendigo Congelado", 
                          hp=350, 
                          atk=80, 
                          crit_chance=0.1, 
                          crit_damage=3.0, 
                          weapon=garras_gigantes,
                          exp_range=(120,180),
                          gold_range=(50,70))

#inimigos da fase 4
crocodilo_gigante = Enemy(name="Crocodilo Gigante", 
                          hp=250, 
                          atk=60, 
                          crit_chance=0.15, 
                          crit_damage=2.5, 
                          weapon=mandibulas,
                          exp_range=(80,120),
                          gold_range=(35,50))

golem_pantano = Enemy(name="Golem do Pântano", 
                      hp=200, 
                      atk=55, 
                      crit_chance=0.12, 
                      crit_damage=2.2, 
                      weapon=raizes,
                      exp_range=(70,100),
                      gold_range=(30,45))

hidra = Enemy(name="Hidra", 
              hp=300, 
              atk=80, 
              crit_chance=0.1, 
              crit_damage=2.8, 
              weapon=cabecas_veneno,
              exp_range=(100,150),
              gold_range=(40,60))

yeti_pantano = Enemy(name="Yeti", 
                     hp=250, 
                     atk=70, 
                     crit_chance=0.18, 
                     crit_damage=2.5, 
                     weapon=garras_gelo,
                     exp_range=(80,120),
                     gold_range=(35,50))

vidente_pantano = Enemy(name="Vidente do Pântano", 
                        hp=500, 
                        atk=100, 
                        crit_chance=0.05, 
                        crit_damage=3.5, 
                        weapon=magia,
                        exp_range=(150,250),
                        gold_range=(70,100))

#inimigos da fase 5
salamandra_vulcanica = Enemy(name="Salamandra Vulcânica", 
                             hp=350, 
                             atk=90, 
                             crit_chance=0.2, 
                             crit_damage=2.5, 
                             weapon=chamas_incandescentes,
                             exp_range=(150,200),
                             gold_range=(50,80))

cultistas_fogo = Enemy(name="Cultistas do Fogo", 
                       hp=200, 
                       atk=60, 
                       crit_chance=0.18, 
                       crit_damage=2.2, 
                       weapon=magia_fogo,
                       exp_range=(100,150),
                       gold_range=(30,50))

elemental_magma = Enemy(name="Elemental de Magma", 
                        hp=400, 
                        atk=110, 
                        crit_chance=0.15, 
                        crit_damage=3.0, 
                        weapon=erupcoes_lava,
                        exp_range=(200,250),
                        gold_range=(60,90))

cavaleiro_inferno = Enemy(name="Cavaleiro do Inferno", 
                          hp=500, 
                          atk=130, 
                          crit_chance=0.1, 
                          crit_damage=3.5, 
                          weapon=espada_flamejante,
                          exp_range=(250,300),
                          gold_range=(80,120))

dragao_magma = Enemy(name="Dragão de Magma", 
                     hp=800, 
                     atk=150, 
                     crit_chance=0.05, 
                     crit_damage=4.0, 
                     weapon=sopro_lava,
                     exp_range=(500,750),
                     gold_range=(150,200))

#lista de inimigos por fase sem mini bosses
enemy_list1 = [goblin , lobo, pixie, aranha_gigante]
enemy_list2 = [escorpiao_gigante, reptiliano, bandido_deserto, golem_areia]
enemy_list3 = [troll_gelo, urso_polar, yeti, espirito_nevasca]
enemy_list4 = [crocodilo_gigante, golem_pantano, hidra, yeti_pantano]
enemy_list5 = [salamandra_vulcanica, cultistas_fogo, elemental_magma, cavaleiro_inferno]