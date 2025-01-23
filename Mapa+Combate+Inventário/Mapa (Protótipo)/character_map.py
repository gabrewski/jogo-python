import msvcrt
#Classe para propriedades do player no mapa
class Character_map:
    def __init__(self) -> None:
        self.pos=[0, 0]
        self.marker = player
        
    def move(self, x: int, y:int):
        self.pos[0]+= x
        self.pos[1]+= y
        
    def calc_move_opt(self, largura, altura) -> dict[str, bool]:
        return {
            "up": self.pos[1] > 0,
            "down": self.pos[1]<altura,
            "left": self.pos[0],
            "right": self.pos[0]< largura
        }

def get_movement_input(self) -> None:
        choice = msvcrt.getch().decode('utf-8') if INSTANT_INPUT else input()

        if self.movement_options["up"] and choice in ("w", "W"):
            self.pos[1] -= 1
        elif self.movement_options["down"] and choice in ("s", "S"):
            self.pos[1] += 1
        elif self.movement_options["left"] and choice in ("a", "A"):
            self.pos[0] -= 1
        elif self.movement_options["right"] and choice in ("d", "D"):
            self.pos[0] += 1
            