from Interface.titulo import run
from Entity.player import Player
from Item.item_list import potion1, potion2, armor1
from curses import wrapper
from Interface.main import start_interface


player = Player(name="Dargia",hp=100, atk_value=10, crit_chance=0.4, crit_damage=2.0)


player.inventory.add_item(potion1)
player.inventory.add_item(potion1)
player.inventory.add_item(potion2)
player.inventory.add_item(armor1)


wrapper(start_interface, player)