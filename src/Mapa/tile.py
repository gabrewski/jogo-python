#Tile.py (Funcionalidade de tiles e cores)
import curses

def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)  
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK) 
    curses.init_pair(7, curses.COLOR_MAGENTA, curses.COLOR_BLACK) 
    curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_BLACK)  
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_BLACK)

class Tile:
    def __init__(self, symbol: str, color_pair: int = 0, colored: bool = True):
        self.symbol = symbol
        self.color_pair = color_pair if colored else 0

# Tipos de terreno usados nas diversas fases
planicie = Tile("_", 2)
floresta = Tile("Y", 2)
montanha = Tile("A", 9)
flores = Tile("*", 7)
tronco = Tile("|", 1)
lagoa = Tile("@", 3)
areia = Tile("_", 1)
arbusto = Tile("w", 2)
montanha_gelo = Tile("▲", 6)
agua = Tile("~", 8)
duna = Tile("~", 1)
player_marker = Tile("X", 5)
tundra = Tile("‗", 6)
pantano = Tile("#", 2)
magma = Tile("≋", 5)
pedra_vulc = Tile("_", 9)
fogo = Tile("^", 5)
pedra_g = Tile("◻", 9)
pedra_p = Tile("□", 6)
flores_claras = Tile("*", 2)
flores_escuras = Tile("*", 2)
flores_amarelas = Tile("*", 1)
arbusto_gelo = Tile("w", 6)
flores_gelo = Tile("*", 6)
floresta_gelo = Tile("Y", 6)
cacto = Tile("|", 2)



