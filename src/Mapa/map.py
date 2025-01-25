#Map.py (Para funcionalidade do mapa)

from Mapa.tile import *
import msvcrt
from random import randint

#Criação da classe mapa e configuração dos terrenos
class Map:
    def __init__(self, 
                largura: int, 
                altura: int) -> None:
        self.largura = largura
        self.altura = altura
        self.init_map_info: list[list[Tile]] = []
        self.full_map_info: list[list[Tile]] = []
        self.map_info: list[list[Tile]] = []
        self.explore_process: list[list[int]] = []     
        self.explored_tiles = [player_marker]
        self.create_map()
        self.copy_map()
        
    def create_map(self) -> None:
    # Inicia o mapa com tiles de planicie padrões
        self.init_map_info = [[Tile("_", ANSI_GREEN) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
    # Inicializa o processo de exploração da matrix para simular uma névoa de guerra
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

#Geraçao de segmentos de terreno, preenchendo o mapa composto apenas de planicies com tipos de chão variados          
    def gerar_terreno(self, 
                tile: Tile, 
                num_terrenos: int, 
                min_size: int, 
                max_size: int, 
                imperfeito: bool = True) -> None:
        for _ in range(num_terrenos):
            largura = randint(min_size, max_size)
            altura = randint(min_size, max_size)
            start_x = randint(0, max(0, self.largura - largura))
            start_y = randint(0, max(0, self.altura - altura))
            
            if imperfeito:
                raw_start_x = randint(3, self.largura - max_size)   

            for i in range(altura):
                if imperfeito: #Gera imperfeições na geração de terrenos para que sejam mais naturais
                    size_x = randint(int(0.7 * max_size), max_size)  
                    start_x = raw_start_x - randint(1, 2)
                for j in range(largura):
                # Checagem de limites
                    if 0 <= start_y + i < self.altura and 0 <= start_x + j < self.largura:
                        self.init_map_info[start_y + i][start_x + j] = tile
                        
    #Função para definir o FOV do jogador, que é usado para gradualmente revelar o mapa, convertendo as tiles não exploradas em exploradas
    def reveal_map(self, pos: list[int]) -> None:
        x, y = pos
        sight_range = range(-2, 3)
        fov = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
        ]
        for y_index in sight_range:
            tile_y = y + y_index
            if 0 <= tile_y < self.altura:
                for x_index in sight_range:
                    tile_x = x + x_index
                    if 0 <= tile_x < self.largura and fov[y_index + 2][x_index + 2]:
                        self.explore_process[tile_y][tile_x] = 1
                        revealed_tile = self.init_map_info[tile_y][tile_x]
                        if revealed_tile not in self.explored_tiles:
                            self.explored_tiles.append(revealed_tile)

    def update_map(self, pos: list[int], marker: Tile) -> None:
        x, y = pos
        self.copy_map()  # Reinicia o mapa pra estado inicial
        self.reveal_map(pos)  #Revela as tiles ao redor do jogador
        self.map_info[y][x] = marker  # Posiciona o marker do jogador no mapa

    def display_map(self) -> list[str]:
        str_map = []
        for row, explored_row in zip(self.map_info, self.explore_process):
            str_map.append("".join([tile.symbol if is_explored else " " for tile, is_explored in zip(row, explored_row)]))
        return str_map

    def copy_map(self) -> None:
        self.map_info = [[tile for tile in row] for row in self.init_map_info]