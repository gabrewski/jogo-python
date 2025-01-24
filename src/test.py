from Interface.main import run
from Entity.player import Player


player = Player(name="Dargia", hp=1000, atk_value=50, crit_chance=0.4, crit_damage=2.0)


run(player)