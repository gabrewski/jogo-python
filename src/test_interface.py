#test_interface.py (Usada para testar interface)

from Interface.main import start_interface
from Entity.player import Player
from Item.item_list import potion1, potion2


player = Player(name="Dargia", hp=100, atk_value=5, crit_chance=0.4, crit_damage=2.0)
player.inventory.add_item(potion1)
player.inventory.add_item(potion1)
player.inventory.add_item(potion2)

start_interface(player)