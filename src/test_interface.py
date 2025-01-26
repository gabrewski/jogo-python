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
    
'''Problemas:
-Não está sendo possivel entrar no modo de exploração no mapa principal
-Combate não está integrado na exploração de mapa
-Loja (Fase 1) não está pronta
-Botões de exit/quit e inventario não funcionando (botão de pausa e confirmar são desnecessários)
-É necessario integrar um botão de sair do modo de exploração e voltar para o mapa principal (M não funciona)
-Save/Load não está integrado no jogo
'''