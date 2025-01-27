from Interface.titulo import run
from Entity.player import Player
from Item.item_list import potion1


player = Player(name="Dargia",hp=100, atk_value=10, crit_chance=0.4, crit_damage=2.0)


player.inventory.add_item(potion1)


run(player)