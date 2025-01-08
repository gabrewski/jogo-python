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

class Arma:
    def __init__(self,
                 name: str,
                 type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.type = type
        self.damage = damage
        self.value = value

espada = Arma(name="Espada",
              type="lâmina",
              damage=5,
              value=10)

adaga = Arma(name="Adaga",
             type="lâmina",
             damage=3,
             value=5)

arco = Arma(name="Arco",
            type="disparo",
            damage=4,
            value=8)

grimório = Arma(name="Grimório",
                type="mágico",
                damage=4,
                value=9)

punhos = Arma(name="Punhos",
              type="impacto",
              damage=2,
              value=0)