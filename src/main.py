#main.py (Game loop)
# test_interface.py
import curses
from Interface.titulo import *
from Interface.main import *
from Entity.player import Player
from Item.item_list import potion1, potion2, armor1

def main(stdscr):
    while True:
        key = exibir_menu(stdscr)
        
        if key == ord('1'):
            
            player = Player(
                name="Dargia",
                hp=100,
                atk_value=5,
                crit_chance=0.4,
                crit_damage=2.0
                
            )
            player.inventory.add_item(potion1)
            player.inventory.add_item(potion1)
            player.inventory.add_item(potion2)
            player.inventory.add_item(armor1)
            
            
            
            start_interface(stdscr, player)
            break
            
        elif key in [ord('3'), 27]:
            break

if __name__ == "__main__":
    curses.wrapper(main)
    
