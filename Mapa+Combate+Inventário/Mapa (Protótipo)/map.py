from tile import Tile, planicie, floresta, montanha, agua
from random import randint

class Map:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura
        
        self.map_info: list[list[Tile]]
        
        self.create_map()
        self.gerar_terreno(floresta, 12, 5, 15)
        self.gerar_terreno(agua, 10, 6, 12)
        self.gerar_terreno(montanha, 10, 3, 6)
#Opções de movimento      
        self.move_opt = {
            "up": "[W] - UP",
            "down": "[S] - DOWN",
            "left": "[A] - LEFT",
            "right": "[D] - RIGHT"
        }
    def create_map(self) -> None:
        self.map_info = [[planicie for _ in range(self.largura)] for _ in range(self.altura)]
            
    def gerar_terreno(self, tile: Tile, num_terrenos: int, min_size:int, max_size:int, imperfeito: bool = True) -> None:
        for _ in range(num_terrenos):
            largura = randint(min_size, max_size)
            altura = randint(min_size, max_size)
            start_x = randint(0, self.largura - largura)
            start_y = randint(0, self.largura - altura)
            
            if imperfeito:
                init_start_x=randint(3, self.largura-max_size)
            
#debug de posicionamento dos terrenos
            print(f"terreno'{tile.symbol}' criado em ({start_x}, {start_y}) com largura {largura} e altura {altura}.")

            for i in range(altura):
                if imperfeito:
                    largura = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(largura):
                    if 0 <= start_y + i < self.altura and 0 <= start_x + j < self.largura:
                        self.map_info[start_y + i][start_x + j] = tile

    def display_map(self)-> None:
        frame = "X" + self.largura * "=" + "X"
        print(frame)
        for fila in self.map_info:
            fila_tiles = [tile.symbol for tile in fila]
            print("|" + "".join(fila_tiles) + "|")
        print(frame)

'''game_map = [
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
]'''