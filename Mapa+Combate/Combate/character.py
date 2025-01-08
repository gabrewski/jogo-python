from weapon import * 

class Character:
    def __init__(self, name: str, hp: int, atk: int):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.weapon = iron_sword

    def attack(self, target) -> None:
        target.hp -= self.atk + self.weapon.atk
        target.hp = max(target.hp, 0)
        print(f"{self.name} deu {self.atk + self.weapon.atk} de dano ao {target.name}")

class Main_Character(Character):
    def __init__(self, name: str, hp:int) -> None:
        super().__init_(name=name, hp = hp)

