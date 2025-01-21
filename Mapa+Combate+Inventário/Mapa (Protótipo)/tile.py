ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

class Tile:
    def __init__(self, symbol: str, color:str = ANSI_RESET, colored: bool = True):
        if colored:
            self.symbol= f"{color}{symbol}{ANSI_RESET}"
        else:
            self.symbol=symbol

#Tipos de terreno usados nas diversas fases
planicie = Tile("_", ANSI_GREEN)
floresta = Tile("Y", ANSI_GREEN)
montanha = Tile("A", ANSI_WHITE)
agua = Tile("≈", ANSI_CYAN)
areia = Tile("~", ANSI_YELLOW)
player_marker = Tile("X", "player", ANSI_RED)
tundra = Tile ("‗", ANSI_WHITE)
pantano = Tile("#", ANSI_GREEN)
magma= Tile("≋", ANSI_RED)