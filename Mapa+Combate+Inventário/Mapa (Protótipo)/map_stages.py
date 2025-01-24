#map_stages.py (Modularização de fases diferentes)

from map import Map
from tile import *

class ForestMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_GREEN) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha, 3, 3, 6) #número de terrenos, tamanho mínimo e tamanho máximo
        self.gerar_terreno(floresta, 4, 5, 12)
        self.gerar_terreno(areia, 3, 2, 5)
        self.gerar_terreno(tronco, 6, 1, 1)
        self.gerar_terreno(flores, 4, 3, 6)
        self.gerar_terreno(arbusto, 6, 1, 5)
        self.gerar_terreno(agua, 4, 5, 8)

class DesertMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_YELLOW) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha, 2, 3, 6)
        self.gerar_terreno(areia, 6, 5, 10)
        self.gerar_terreno(arbusto, 5, 2 ,5)
        self.gerar_terreno(floresta, 3, 3, 5)
        self.gerar_terreno(duna, 6, 5, 10)
        self.gerar_terreno(cacto, 6, 1, 2)
        self.gerar_terreno(agua, 2, 2, 5) 
        self.gerar_terreno(pedra_p, 6, 1, 3) 
        self.gerar_terreno(pedra_p, 7, 1, 3) 

class SnowMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_WHITE) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha_gelo, 4, 3, 7)
        self.gerar_terreno(arbusto_gelo, 4, 2, 5)
        self.gerar_terreno(tundra, 5, 5, 12)
        self.gerar_terreno(agua, 3, 4, 6)
        self.gerar_terreno(floresta_gelo, 4, 5, 8)
        self.gerar_terreno(flores_gelo, 6, 3, 5)
        self.gerar_terreno(pedra_p, 5, 1, 2) 
        self.gerar_terreno(pedra_p, 7, 1, 2) 

class SwampMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_GREEN) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(pantano, 10, 5, 12)
        self.gerar_terreno(floresta, 4, 3, 6)
        self.gerar_terreno(agua, 15, 3, 12)
        self.gerar_terreno(flores_claras, 3, 3, 5)
        self.gerar_terreno(flores_escuras, 3, 3, 5)
        self.gerar_terreno(flores_amarelas, 3, 3, 5)

class FireMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.setup_terreno()
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_DARK_GRAY) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(magma, 6, 4, 10)
        self.gerar_terreno(pedra_vulc, 5, 3, 8)
        self.gerar_terreno(fogo, 7, 3, 8)
        self.gerar_terreno(floresta_fogo, 5, 3, 8)
        self.gerar_terreno(pedra_p, 8, 1, 2) 
        self.gerar_terreno(pedra_p, 9, 1, 2) 
