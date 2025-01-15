from item import *
from inventario import *
import random

#Classe para todos os personagens
class Character:
    def __init__(self, name: str, hp: int, atk: int, crit_chance: int, crit_damage: float):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage

    def attack(self, target):
        roll = random.randint(1,100) #determina se o ataque vai ser crítico
        if roll <= self.crit_chance:
            damage = int(round(self.atk + self.weapon.atk) * self.crit_damage)
            print("\nAtaque crítico!")
        else:
            damage = self.atk + self.weapon.atk
        target.hp -= damage
        target.hp = max(target.hp, 0)
        print(f"\n{self.name} deu {damage} de dano ao {target.name}.")

    def defend(self, target):
        damage = target.atk - self.armor.value
        self.hp -= damage
        self.hp = max(self.hp, 0)
        print(f"\n{self.name} defendeu o ataque, mas levou {damage} de dano.")

#Classe do jogador
class Player (Character):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_damage: float):
        super().__init__(name = name, hp = hp, atk=atk, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = espada
        self.armor = armor
        self.inventory = Inventario(slots=inventory_slots, gold=0, player_items=[])

    def display_info(self):
        print(f"Nome: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Ataque: {self.atk}")
        print(f"Chance de Crítico: {self.crit_chance}%")
        print(f"Dano Crítico: {self.crit_damage}x")

    def equip_weapon(self, weapon: Item):
        self.weapon = weapon
        print(f"'{weapon.name}' foi equipado como arma.")

    def equip_armor(self, armor: Item):
        self.armor = armor
        print(f"'{armor.name}' foi equipado como armadura.")

    def use_item(self, item: Item):
        if item in self.inventory:

#Classe para inimigos
class Enemy(Character):
    def __init__(self, name: str, hp:int, atk:int, crit_chance: int, crit_damage: float):
        super().__init__(name=name, hp=hp, atk=atk, crit_chance = crit_chance, crit_damage = crit_damage)
        self.weapon = porrete
        
#Lista de inimigos segmentada por fases
enemy_list_fase_1 = [ #Floresta dos Ecos
    {"name": "Goblin", "hp": 30, "def": 5, "Weapon": "Adaga", "tiles": "Floresta", "xp-range": "10-15", "gold-range": "5-10"},
    {"name": "Lobo", "hp": 50, "def": 10, "Weapon": "Garras", "tiles": "Floresta", "xp-range": "15-25", "gold-range": "7-12"},
    {"name": "Pixie", "hp": 20, "def": 3, "Weapon": "Magia", "tiles": "Floresta", "xp-range": "8-12", "gold-range": "4-6"},
    {"name": "Aranha Gigante", "hp": 70, "def": 15, "Weapon": "Veneno", "tiles": "Floresta", "xp-range": "20-30", "gold-range": "10-15"},
    {"name": "Mestre das Aranhas", "hp": 150, "def": 20, "Weapon": "Machado", "tiles": "Floresta", "xp-range": "50-75", "gold-range": "20-30"} #mini boss
]
enemy_list_fase_2 = [ #Dunas do Desolado
    {"name": "Escorpião Gigante", "hp": 100, "def": 20, "Weapon": "Cauda de Veneno", "tiles": "Deserto", "xp-range": "30-50", "gold-range": "15-20"},
    {"name": "Reptiliano", "hp": 120, "def": 25, "Weapon": "Lâmina de Escama", "tiles": "Deserto", "xp-range": "40-60", "gold-range": "18-25"},
    {"name": "Bandido do Deserto", "hp": 80, "def": 15, "Weapon": "Cimitarra", "tiles": "Deserto", "xp-range": "25-40", "gold-range": "12-18"},
    {"name": "Golem de Areia", "hp": 150, "def": 40, "Weapon": "Areia Sólida", "tiles": "Deserto", "xp-range": "50-75", "gold-range": "20-35"},
    {"name": "Faraó Esquecido", "hp": 300, "def": 50, "Weapon": "Golpes de Areia", "tiles": "Deserto", "xp-range": "100-150", "gold-range": "40-60"} #mini boss
]
enemy_list_fase_3 = [ #Terra Congelada
    {"name": "Troll de Gelo", "hp": 150, "def": 30, "Weapon": "Clava de Gelo", "tiles": "Tundra", "xp-range": "50-75", "gold-range": "25-30"},
    {"name": "Urso Polar", "hp": 90, "def": 20, "Weapon": "Gélido", "tiles": "Tundra", "xp-range": "30-50", "gold-range": "15-20"},
    {"name": "Yeti", "hp": 120, "def": 25, "Weapon": "Garras de Gelo", "tiles": "Tundra", "xp-range": "40-60", "gold-range": "20-30"},
    {"name": "Espírito de Nevasca", "hp": 200, "def": 40, "Weapon": "Garras Gigantes", "tiles": "Tundra", "xp-range": "60-90", "gold-range": "30-40"},
    {"name": "Wendigo Congelado", "hp": 350, "def": 60, "Weapon": "Garras Gigantes", "tiles": "Tundra", "xp-range": "120-180", "gold-range": "50-70"} #mini boss
]
enemy_list_fase_4 = [ #Pântano das Àguas Místicas
    {"name": "Crocodilo Gigante", "hp": 250, "def": 35, "Weapon": "Mandíbulas", "tiles": "Pântano", "xp-range": "80-120", "gold-range": "35-50"},
    {"name": "Golem do Pântano", "hp": 200, "def": 45, "Weapon": "Raízes", "tiles": "Pântano", "xp-range": "70-100", "gold-range": "30-45"},
    {"name": "Hidra", "hp": 300, "def": 50, "Weapon": "Cabeças de Veneno", "tiles": "Pântano", "xp-range": "100-150", "gold-range": "40-60"},
    {"name": "Yeti", "hp": 250, "def": 40, "Weapon": "Garras de Gelo", "tiles": "Pântano", "xp-range": "80-120", "gold-range": "35-50"},
    {"name": "Vidente do Pântano", "hp": 500, "def": 70, "Weapon": "Cabeças Múltiplas", "tiles": "Pântano", "xp-range": "150-250", "gold-range": "70-100"} #mini boss
]
enemy_list_fase_5 = [ #Fornalha do Apocalipse
    {"name": "Salamandra Vulcânica", "hp": 350, "def": 60, "Weapon": "Chamas Incandescentes", "tiles": "Vulcão", "xp-range": "150-200", "gold-range": "50-80"},
    {"name": "Cultistas do Fogo", "hp": 200, "def": 40, "Weapon": "Magia de Fogo", "tiles": "Vulcão", "xp-range": "100-150", "gold-range": "30-50"},
    {"name": "Elemental de Magma", "hp": 400, "def": 70, "Weapon": "Erupções de Lava", "tiles": "Vulcão", "xp-range": "200-250", "gold-range": "60-90"},
    {"name": "Cavaleiro do Inferno", "hp": 500, "def": 90, "Weapon": "Espada Flamejante", "tiles": "Vulcão", "xp-range": "250-300", "gold-range": "80-120"},
    {"name": "Dragão de Magma", "hp": 800, "def": 100, "Weapon": "Sopro de Lava", "tiles": "Vulcão", "xp-range": "500-750", "gold-range": "150-200"} #boss final
]