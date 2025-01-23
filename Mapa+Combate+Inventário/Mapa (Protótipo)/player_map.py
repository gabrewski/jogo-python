'''#player_map.py(para funcionalidade do personagem a se movimentar no mapa):
from tile import *
import msvcrt
#Classe para propriedades do player no mapa
class Player_map:
    def __init__(self) -> None:
        self.pos=[0, 0]
        self.marker = player_marker
        
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
            self.pos[0] += 1'''
            