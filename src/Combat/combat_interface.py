import curses
import time
from Entity.player import Player
from Entity.enemy_list import yeti


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
        win.addstr(5, 0, "3. Curar")
        win.addstr(6, 0, "4. Fugir")
        win.refresh()

        #ações do jogador
        opt = win.getch()
        if opt == ord('1'): #atacar
            win.addstr(8, 0, f"{player.name} atacou.")
            atk_damage, crit = player.attack(enemy)
            if crit:
                time.sleep(2) 
                win.addstr(10, 0, f"Ataque crítico! {player.name} deu {atk_damage} de dano ao {enemy.name}.")
            else:
                time.sleep(2) 
                win.addstr(10, 0, f"{player.name} atacou e deu {atk_damage} de dano ao {enemy.name}.")

        elif opt == ord('2'): #defender
            win.addstr(8, 0, f"{player.name} defendeu.")
            def_damage, defend = player.defend(enemy)
            if defend:
                time.sleep(2) 
                win.addstr(10, 0, f"{player.name} defendeu o ataque mas levou {def_damage} de dano.")
            else:
                time.sleep(2) 
                win.addstr(10, 0, f"{player.name} não conseguiu defender o ataque e levou {def_damage} de dano.")

        elif opt == ord('3'): #curar
            potions = player.inventory.get_consumables()
            if potions:
                win.addstr(8, 0, f"Qual poção deseja usar? Inventário: {', '.join([f'{i + 1}: {item.name} ({item.quantity})' for i, item in enumerate(potions)])}")
                win.refresh()
                win.addstr(8, 0, f"{player.name} utilizou um item.")
                win.refresh()

                while True:
                    item_choice = win.getch()
                    choice_index = item_choice - ord('1')  #converte para index
                    if 0 <= choice_index < len(potions):
                        selected_item = potions[choice_index]
                        heal_amount = selected_item.healing_points
                        player.hp = min(player.hp + heal_amount, player.hp_max)  #limita heal para hp_max
                        selected_item.quantity -= 1

                        if selected_item.quantity <= 0: #remove o item se a quantidade chegar a 0
                            player.inventory.remove(selected_item)
                        time.sleep(2) 
                        win.addstr(10, 0, f"Você usou {selected_item.name} e recuperou {heal_amount} HP!")
                        win.refresh()
            else:
                win.addstr(8, 0, f"{player.name} não tem itens para utilizar.")


        elif opt == ord('4'): #fugir
            flee = player.flee()
            if flee:
                win.addstr(8, 0, f"{player.name} fugiu da batalha.")
                win.refresh()
                time.sleep(1)
                break
            else:
                win.addstr(8, 0, "Fuga malsucedida.")
        else:
            win.addstr(14, 0, "Opção inválida, escolha 1, 2, 3 ou 4.")

        #checha se o inimigo está morto
        if enemy.hp == 0:
            win.addstr(13, 0, f"{player.name} venceu a batalha.")
            win.refresh()

            # ganhar EXP e Gold 
            lvl_up, exp_ganho = player.gain_exp(enemy.exp_range)
            gold_ganho = player.gain_gold(enemy.gold_range)

            time.sleep(1)
            break

        #ações do inimigo  
        time.sleep(1) #retarda a ação do inimigo
        if opt == ord('3'): #se o jogador curar, inimigo pode apenas atacar
            win.addstr(9, 0, f"{enemy.name} atacou.")
            atk_damage, crit = enemy.attack(player)
            if crit:
                time.sleep(3) 
                win.addstr(11, 0, f"Ataque crítico! {enemy.name} deu {atk_damage} de dano ao {player.name}.")
            else:
                time.sleep(3) 
                win.addstr(11, 0, f"{enemy.name} atacou e deu {atk_damage} de dano ao {player.name}.")
            player_text = f"Player: {player.name} | HP: {player.hp}/{player.hp_max}"
        else:
            atk = enemy.take_action(player)
            if atk: #se o jogador atacar ou defender, inimigo pode fazer o mesmo
                atk_damage, crit = enemy.attack(player)
                win.addstr(9, 0, f"{enemy.name} atacou.")
                if crit:
                    time.sleep(3) 
                    win.addstr(11, 0, f"Ataque crítico! {enemy.name} deu {atk_damage} de dano ao {player.name}.")
                else:
                    time.sleep(3) 
                    win.addstr(11, 0, f"{enemy.name} atacou e deu {atk_damage} de dano ao {player.name}.")
                player_text = f"Player: {player.name} | HP: {player.hp}/{player.hp_max}"
            else:
                def_damage, defend = enemy.defend(player)
                if defend:
                    win.addstr(9, 0, f"{enemy.name} defendeu.")
                    time.sleep(3) 
                    win.addstr(11, 0, f"{enemy.name} defendeu o ataque mas levou {def_damage} de dano.")
                else:
                    time.sleep(3) 
                    win.addstr(11, 0, f"{enemy.name} não conseguiu defender o ataque e levou {def_damage} de dano.")

        #checha se o jogador está morto
        if player.hp == 0:
            win.addstr(12, 0, f"{enemy.name} venceu a batalha.")
            win.refresh()
            time.sleep(1) 
            break
        
        win.refresh()
        time.sleep(1)
        
    win.clear()
    win.addstr(height // 2, width //2 - len("A batalha terminou."), "A batalha terminou.")
    win.refresh()
    time.sleep(1)

# test
player = Player(name="Dargia", hp=1000, atk_value=50, crit_chance=0.4, crit_damage=2.0)

def start_combat(enemy):
    curses.wrapper(combat, player, enemy)