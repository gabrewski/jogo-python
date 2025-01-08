class Weapon:
    def __init__(self,
                 name: str,
                 atk: int,
                 ) -> None:
        self.name = name
        self.atk = atk

#Criação de armas dentro da classe "Weapon"
iron_sword = Weapon(name="Iron Sword",atk=5)

short_bow = Weapon(name="Short Bow", atk=4)

fists = Weapon(name="Fists", atk=2)
