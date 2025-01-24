class ProgressionSystem:
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100

    def gain_exp(self, amount):     #gerencia o ganho de xp e progressão de nível.
        print(f"Você ganhou {amount} EXP!")
        self.exp += amount
        while self.exp >= self.exp_to_next_level and self.level < 10:
            self.level_up()

    def level_up(self):   #avança o personagem para o próximo nível.
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level += 50        #aumenta o xp necessário para o próximo nível
        print(f"Você subiu para o nível {self.level}!")

    def get_stats(self):    #retorna os atributos baseados no nível atual.
        hp = 10 + (self.level - 1) * 4
        atk = 3 + (self.level - 1) * 2
        defense = 2 + (self.level - 1) * 2
        return {
            "level": self.level,
            "hp": hp,
            "atk": atk,
            "defense": defense,
            "exp": self.exp,
            "exp_to_next_level": self.exp_to_next_level
        }
