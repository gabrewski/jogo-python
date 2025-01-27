from Entity.player import Player
from Item.item_list import potion1
from Interface.main import start_interface
from curses import wrapper


player = Player(name="Dargia",hp=100, atk_value=10, crit_chance=0.1, crit_damage=2.0)


player.inventory.add_item(potion1)


wrapper(start_interface, player)