import curses
import time
from character import *
from item import *

def combat(stdscr, player, enemy):
    curses.curs_set(0) #esconde o cursor
    stdscr.clear() #limpa a tela
    height, width = stdscr.getmaxyx() #tamanho do terminal
    win = curses.newwin(height, width, 0, 0)
        
    while True:
        
        player_text = f"Jogador: {player.name} | HP: {player.hp}/{player.hp_max}"
        enemy_text = f"Inimigo: {enemy.name} | HP: {enemy.hp}/{enemy.hp_max}"

        win.clear()
        win.addstr(0, 0, player_text)
        start_x = width - len(enemy_text) - 1
        win.addstr(0, start_x, enemy_text)
        win.addstr(2, 0, "O que deseja fazer?")
        win.addstr(3, 0, "1. Atacar")
        win.addstr(4, 0, "2. Defender")
        win.addstr(5, 0, "3. Fugir")
        win.refresh()

        #ações do jogador
        opt = win.getch()
        if opt == ord('1'): #atacar
            atk_damage, crit = player.attack(enemy)
            if crit:
                win.addstr(8, 0, f"Ataque crítico! {player.name} deu {atk_damage} de dano ao {enemy.name}.")
            else:
                win.addstr(8, 0, f"{player.name} atacou e deu {atk_damage} de dano ao {enemy.name}.")

        elif opt == ord('2'): #defender
            def_damage, defend = player.defend(enemy)
            if defend:
                win.addstr(8, 0, f"{player.name} defendeu o ataque mas levou {def_damage} de dano.")
            else:
                win.addstr(8, 0, f"{player.name} não conseguiu defender o ataque e levou {def_damage} de dano.")

        elif opt == ord('3'): #fugir
            flee = player.flee()
            if flee:
                win.addstr(8, 0, f"{player.name} fugiu da batalha.")
                time.sleep(2)
                break
            else:
                win.addstr(8, 0, "Fuga malsucedida.")
        else:
            win.addstr(11, 0, "Opção inválida, escolha 1, 2, ou 3.")

        #checha se o inimigo está morto
        if enemy.hp == 0:
            win.addstr(10, 0, f"{player.name} venceu a batalha.")            
            win.refresh()
            time.sleep(1) 
            break

        #ações do inimigo  
        time.sleep(2) #retarda a ação do inimigo
        atk = enemy.take_action(player)
        if atk:
            atk_damage, atk = enemy.attack(player)
            if crit:
                win.addstr(9, 0, f"Ataque crítico! {enemy.name} deu {atk_damage} de dano ao {player.name}.")
            else:
                win.addstr(9, 0, f"{enemy.name} atacou e deu {atk_damage} de dano ao {player.name}.")
            player_text = f"Player: {player.name} | HP: {player.hp}/{player.hp_max}"
        else:
            def_damage, defend = enemy.defend(player)
            if defend:
                win.addstr(9, 0, f"{enemy.name} defendeu o ataque mas levou {def_damage} de dano.")
            else:
                win.addstr(9, 0, f"{enemy.name} não conseguiu defender o ataque e levou {def_damage} de dano.")

        #checha se o jogador está morto
        if player.hp == 0:
            win.addstr(10, 0, f"{enemy.name} venceu a batalha.")
            win.refresh()
            time.sleep(1) 
            break
        
        win.refresh()
        time.sleep(2)
        
    win.clear()
    win.addstr(height // 2, width //2 - len("A batalha terminou."), "A batalha terminou.")
    win.refresh()
    time.sleep(2)

player = Player(name="Dargia", hp=1000, atk=50, crit_chance=0.4, crit_damage=2.0)
enemy = yeti

if __name__ == "__main__":
    curses.wrapper(combat, player, enemy)
    
#to do:
#arrumar flee (mensagem não aparece)
#adicionar ação de usar item
#checar se função defend funciona corretamente (inimigos não tem armor, logo não tem armor.def_value)
#adicionar mensagem caso player ganhe (ouro, xp e drop)
#tentar fazer animação
