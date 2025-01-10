# Standard library imports
import msvcrt

# Local folder imports
from tile import player_marker


INSTANT_INPUT = False


# ------------ parent class ------------
class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health


# ------------ subclass------------
class Player(Character):
    def __init__(self, name: str = "Player", health: int = 100) -> None:
        super().__init__(name=name, health=health)

        self.pos = [0, 0]
        self.marker = player_marker

        self.movement_options: dict[str, bool]

    def move(self, x: int, y: int) -> None:
        self.pos[0] += x
        self.pos[1] += y

    def calculate_movement_options(self, width, height) -> None:
        self.movement_options = {
            "up": self.pos[1] > 0,  # can go up
            "down": self.pos[1] < height - 1,  # can go down
            "left": self.pos[0] > 0,  # can go left
            "right": self.pos[0] < width - 1  # can go right
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
