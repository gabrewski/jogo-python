class Weapon:
    def __init__(self, name: str, atk: int) -> None:
        self.name = name
        self.atk = atk

espada = Weapon(name="Espada de Ferro", atk=5)

porrete = Weapon(name="Porrete de Madeira", atk=2)

adaga = Weapon(name="Adaga", atk=3)                                

arco = Weapon(name="Arco", atk=4)

grimório = Weapon(name="Grimório", atk=4)

punhos = Weapon(name="Punhos", atk=2)
