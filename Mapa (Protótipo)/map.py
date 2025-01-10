class Map:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura
        self.map_info: list[list[str]] = []
        self.gerar_map()
        
    def gerar_map(self) -> None:
        map_info=[]
        for fila in range(self.altura):
            fila_info = []
            for coluna in range(self.largura):
                fila_info.append(".")
            self.map_info.append(fila_info)
            
    def mostrar_map(self)-> None:
        frame = "O" + self.largura * "=" + "O"
        print(frame)
        for fila in self.map_info:
            print("|" + "".join(fila) + "|")
        print(frame)
            
        




'''game_mapa = [
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
    [Tile(...), Tile(...), Tile(...)],
]'''