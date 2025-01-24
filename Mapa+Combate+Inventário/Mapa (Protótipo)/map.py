#Map.py (Para funcionalidade do mapa)

from tile import *
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
        self.full_map_info: list[[Tile]] = []
        self.map_info: list[list[Tile]] = []
        self.explore_process: list[list[int]] = []     
        self.explored_tiles = [player_marker]
        self.create_map()
        self.gerar_terreno(montanha, 3, 3, 6)
        self.gerar_terreno(floresta, 4, 5, 12)
        self.gerar_terreno(terra, 3, 2, 5)
        self.gerar_terreno(tronco, 6, 1, 1)
        self.gerar_terreno(flores, 4, 3, 6)
        self.gerar_terreno(arbusto, 6, 1, 5)
        self.gerar_terreno(agua, 4, 5, 8)
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

    def display_map(self) -> None:
        frame = "X" + self.largura * "=" + "X"
        print(frame)
        for row, explored_row in zip(self.map_info, self.explore_process):
            print(
                "|" + "".join(
                    [
                        tile.symbol if is_explored else " "
                        for tile, is_explored in zip(row, explored_row)
                    ]
                ) + "|"
            )
        print(frame)

    def copy_map(self) -> None:
        self.map_info = [[tile for tile in row] for row in self.init_map_info]

#Classe para propriedades do player no mapa
class Player_map:
    def __init__(self) -> None:
        self.pos=[0, 0]
        self.marker = player_marker
        
        #Opções de movimento      
        self.move_opt = {
            "up": "[W] - UP",
            "down": "[S] - DOWN",
            "left": "[A] - LEFT",
            "right": "[D] - RIGHT"
        }

    def move(self, x: int, y:int):
        self.pos[0]+= x
        self.pos[1]+= y

    def calc_move_opt(self, largura, altura) -> dict[str, bool]:
        return {
            "up": self.pos[1] > 0,
            "down": self.pos[1]<altura - 1,
            "left": self.pos[0] > 0,
            "right": self.pos[0]< largura - 1
        }

    def get_movement_input(self, map_largura, map_altura) -> None:
        move_opt = self.calc_move_opt(map_largura, map_altura)
        choice = msvcrt.getch().decode('utf-8')
        
        if move_opt["up"] and choice in ("w", "W"):
            self.pos[1] -= 1
        elif move_opt["down"] and choice in ("s", "S"):
            self.pos[1] += 1
        elif move_opt["left"] and choice in ("a", "A"):
            self.pos[0] -= 1
        elif move_opt["right"] and choice in ("d", "D"):
            self.pos[0] += 1
            
#Modularização de geração de mapa de diferentes fases
class ForestMap:
    def __init__(self):
        pass

class DesertMap:
    def __init__(self):
        pass

class SnowMap:
    def __init__(self):
        pass
    
class SwampMap:
    def __init__(self):
        pass

class FireMap:
    def __init__(self):
        pass
            