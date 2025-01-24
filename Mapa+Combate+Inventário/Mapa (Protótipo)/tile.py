#Tile.py (Funcionalidade de tiles e cores)
ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_LIGHT_GREEN = "\033[1;32m"
ANSI_BLUE = "\033[34m"
ANSI_LIGHT_BLUE = "\033[1;34m"
ANSI_RED = "\033[31m"
ANSI_LIGHT_RED = "\033[1;31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"
ANSI_LIGHT_GRAY = "\033[0;37m"
ANSI_DARK_GRAY = "\033[1;30m"
ANSI_BROWN = "\033[0;33m"

class Tile:
    def __init__(self, symbol: str, color:str = ANSI_RESET, colored: bool = True):
        if colored:
            self.symbol= f"{color}{symbol}{ANSI_RESET}"
        else:
            self.symbol=symbol

#Tipos de terreno usados nas diversas fases
planicie = Tile("_", ANSI_GREEN)
floresta = Tile("Y", ANSI_GREEN)
montanha = Tile("A", ANSI_DARK_GRAY)
flores = Tile("*", ANSI_MAGENTA)
tronco = Tile("|", ANSI_BROWN)
lagoa = Tile("@", ANSI_LIGHT_BLUE)
areia = Tile("_", ANSI_BROWN)
arbusto = Tile("w", ANSI_LIGHT_GREEN)
montanha_gelo = Tile("▲", ANSI_WHITE)
agua = Tile("~", ANSI_CYAN)
duna = Tile("~", ANSI_YELLOW)
player_marker = Tile("X", color=ANSI_RED)
tundra = Tile ("‗", ANSI_WHITE)
pantano = Tile("#", ANSI_GREEN)
magma= Tile("≋", ANSI_RED)
pedra_vulc=Tile("_", ANSI_DARK_GRAY)
fogo = Tile("^", ANSI_BROWN)
pedra_g = Tile("◻", ANSI_DARK_GRAY)
pedra_p = Tile("□", ANSI_LIGHT_GRAY)
flores_claras = Tile("*", ANSI_LIGHT_GREEN)
flores_escuras = Tile("*", ANSI_GREEN)
flores_amarelas = Tile("*", ANSI_YELLOW)
arbusto_gelo = Tile("w", ANSI_WHITE)
flores_gelo = Tile("*", ANSI_WHITE)
floresta_gelo = Tile("Y", ANSI_WHITE)
floresta_fogo = Tile("T", ANSI_LIGHT_GRAY)
cacto = Tile("|", ANSI_GREEN)

