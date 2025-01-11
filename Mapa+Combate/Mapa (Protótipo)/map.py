from tile import *
from random import randint

class Map:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura
        self.map_info: list[list[str]] = []
        self.create_map()
        
    def create_map(self) -> None:
        self.map_info=[]
        for fila in range(self.altura):
            fila_info = []
            for coluna in range(self.largura):
                fila_info.append(planice)
            self.map_info.append(fila_info)
            
    def gerar_terreno(self, tile: Tile, num_terrenos: int, min_size:int, max_size:int ) -> None:
        largura=randint(min_size, max_size)
        altura = randint(min_size, max_size)
        start_x = randint(1, self.largura - largura - 1)
        start_y = randint(1, self.largura - altura - 1)
        
        for i in range(altura):
            for j in range(largura):
                self.map_info[start_y + start_x]
            
    def display_map(self)-> None:
        frame = "X" + self.largura * "=" + "X"
        print(frame)
        for fila in self.map_info:
            fila_tiles = [tile.symbol for tile in fila]
            print("|" + "".join(fila_tiles) + "|")
        print(frame)


game_map = [
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
]