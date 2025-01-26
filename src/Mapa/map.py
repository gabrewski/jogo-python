#Map.py (Para funcionalidade do mapa)

from Mapa.tile import *
import msvcrt
from random import randint

#Criação da classe mapa e configuração dos terrenos
class Map:
    def __init__(self, 
                largura: int, 
                altura: int) -> None: #Inicialização do mapa
        self.largura = largura # Largura do mapa
        self.altura = altura # Altura do mapa
        self.init_map_info: list[list[Tile]] = [] # Mapa inicial
        self.full_map_info: list[list[Tile]] = [] # Mapa completo
        self.map_info: list[list[Tile]] = [] # Mapa atual
        self.explore_process: list[list[int]] = []  # Processo de exploração    
        self.explored_tiles = [player_marker] # Tiles exploradas
        self.create_map() # Criação do mapa
        self.copy_map() # Cópia do mapa
        
#Criação do mapa com tiles de planicie padrões (redundante, já é feito no arquivo map_stages.py)    
    def create_map(self) -> None:
    # Inicia o mapa com tiles de planicie padrões
        self.init_map_info = [[Tile("_", 2) for _ in range(self.largura)] for _ in range(self.altura)]
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
        for _ in range(num_terrenos): # Gera um número de terrenos
            largura = randint(min_size, max_size) # Gera um tamanho aleatório para o terreno
            altura = randint(min_size, max_size) 
            start_x = randint(0, max(0, self.largura - largura)) # Gera uma posição aleatória para o terreno
            start_y = randint(0, max(0, self.altura - altura)) # Gera uma posição aleatória para o terreno
            
            if imperfeito: # Gera imperfeições na geração de terrenos para que sejam mais naturais
                raw_start_x = randint(3, self.largura - max_size)   

            for i in range(altura):
                if imperfeito: 
                    size_x = randint(int(0.7 * max_size), max_size)  
                    start_x = raw_start_x - randint(1, 2)
                for j in range(largura):
                # Checa se a tile está dentro do mapa
                    if 0 <= start_y + i < self.altura and 0 <= start_x + j < self.largura:
                        self.init_map_info[start_y + i][start_x + j] = tile
                        
    #Função para definir o FOV do jogador, que é usado para gradualmente revelar o mapa, convertendo as tiles não exploradas em exploradas
    def reveal_map(self, pos: list[int]) -> None:
        x, y = pos
        sight_range = range(-4, 5)  # Alcance de -4 a +4 (9x9)
    
    # Matriz FOV 9x9 com padrão diamante simétrico
        fov = [
        [0,0,0,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1],  # Centro
        [1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,0,0,0],
        ]
    
        for y_index in sight_range:
            tile_y = y + y_index
            if 0 <= tile_y < self.altura:
                for x_index in sight_range:
                    tile_x = x + x_index
                    if 0 <= tile_x < self.largura and fov[y_index + 4][x_index + 4]:  # Ajuste de offset para +4
                        self.explore_process[tile_y][tile_x] = 1
                        revealed_tile = self.init_map_info[tile_y][tile_x]
                        if revealed_tile not in self.explored_tiles:
                            self.explored_tiles.append(revealed_tile)
                            
#Função para atualizar o mapa, posicionando o marcador do jogador e revelando as tiles ao redor dele
    def update_map(self, pos: list[int], marker: Tile) -> None: 
        x, y = pos
        self.copy_map()  # Reinicia o mapa pra estado inicial
        self.reveal_map(pos)  #Revela as tiles ao redor do jogador
        self.map_info[y][x] = marker  # Posiciona o marker do jogador no mapa
        
#Função para exibir o mapa, substituindo as tiles não exploradas por espaços vazios
    def display_map(self) -> list: 
        str_map = []
        for row, explored_row in zip(self.map_info, self.explore_process):
            str_map.append([tile if is_explored else " " for tile, is_explored in zip(row, explored_row)])
        return str_map
    
#Função para copiar o mapa para manter o estado inicial do mapa intacto e permitir a atualização dele sem alterar o estado inicial 
    def copy_map(self) -> None: 
        self.map_info = [[tile for tile in row] for row in self.init_map_info]
    
