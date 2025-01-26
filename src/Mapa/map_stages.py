#map_stages.py (Modularização de fases diferentes)

from Mapa.map import Map
from Mapa.tile import *

#Cada classe de mapa é uma subclasse de Map, e cada uma tem um método setup_terreno() que define os tipos de terreno presentes no mapa
class ForestMap(Map): #Mapa de floresta
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
        
    def create_map(self):
        self.init_map_info = [[Tile("_", 2) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(tronco, 18, 1, 1)
        self.gerar_terreno(montanha, 12, 9, 14) #número de terrenos, tamanho mínimo e tamanho máximo
        self.gerar_terreno(floresta, 25, 10, 25)
        self.gerar_terreno(areia, 9, 6, 13)
        self.gerar_terreno(flores, 10, 4, 12)
        self.gerar_terreno(arbusto, 18, 1, 5)
        self.gerar_terreno(agua, 9, 8, 15)

class DesertMap(Map): #Mapa de deserto
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()

    def create_map(self): 
        self.init_map_info = [[Tile("_", 1) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha, 8, 9, 18)
        self.gerar_terreno(areia, 16, 10, 20)
        self.gerar_terreno(arbusto, 10, 8, 20)
        self.gerar_terreno(floresta, 9, 9, 15)
        self.gerar_terreno(duna, 30, 15, 30)
        self.gerar_terreno(cacto, 30, 1, 7)
        self.gerar_terreno(pedra_p, 12, 1, 3) 
        self.gerar_terreno(pedra_p, 14, 1, 3)
        self.gerar_terreno(agua, 4, 9, 19) 

class SnowMap(Map): #Mapa de neve
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()

    def create_map(self):
        self.init_map_info = [[Tile("_", 6) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(arbusto_gelo, 8, 2, 8)
        self.gerar_terreno(arbusto, 8, 2, 8)
        self.gerar_terreno(tundra, 5, 5, 12)
        self.gerar_terreno(flores_gelo, 6, 3, 5)
        self.gerar_terreno(flores, 6, 3, 5)
        self.gerar_terreno(floresta_gelo, 15, 5, 20)
        self.gerar_terreno(floresta, 7, 5, 20)
        self.gerar_terreno(pedra_p, 5, 1, 2) 
        self.gerar_terreno(pedra_p, 7, 1, 2)
        self.gerar_terreno(montanha, 8, 5, 10)
        self.gerar_terreno(montanha_gelo, 15, 4, 14)
        self.gerar_terreno(agua, 10, 5, 16) 

class SwampMap(Map): #Mapa de pântano
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()

    def create_map(self):
        self.init_map_info = [[Tile("_", 2) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(flores_claras, 10, 3, 5)
        self.gerar_terreno(flores_escuras, 10, 3, 5)
        self.gerar_terreno(flores_amarelas, 10, 3, 5)
        self.gerar_terreno(flores, 10, 3, 5)
        self.gerar_terreno(arbusto, 20, 1, 15)
        self.gerar_terreno(floresta, 15, 5, 20)
        self.gerar_terreno(pantano, 16, 5, 20)
        self.gerar_terreno(agua, 15, 10, 23)

class FireMap(Map): #Mapa de fogo
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()

    def create_map(self):
        self.init_map_info = [[Tile("_", 12) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        
        self.gerar_terreno(pedra_p, 8, 1, 2) 
        self.gerar_terreno(pedra_p, 9, 1, 2)
        self.gerar_terreno(pedra_vulc, 15, 3, 8)
        self.gerar_terreno(flores_sombrias, 10, 3, 5)
        self.gerar_terreno(arbusto_sombrio, 10, 5, 15)
        self.gerar_terreno(floresta_sombria, 10, 5, 15)
        self.gerar_terreno(fogo, 16, 3, 8)
        self.gerar_terreno(vulcao, 10, 5, 10)
        self.gerar_terreno(magma, 19, 4, 20)
