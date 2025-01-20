import curses
from character import *

def combat(stdscr, player, enemy):
    curses.curs_set(0) #esconde o cursor
    stdscr.clear() #limpa a tela
    height, width = stdscr.getmaxyx() #tamanho do terminal
    win = curses.newwin(height, width, 0, 0)

    player_text = f"Jogador: {player.name} | HP: {player.hp}/{player.hp_max}"
    enemy_text = f"Inimigo: {enemy.name} | HP: {enemy.hp}/{enemy.hp_max}"

    opt = win.getch()
    while True:
        win.clear()
        win.addstr(0, 0, player_text)
        start_x = width - len(enemy_text) - 1
        win.addstr(0, start_x, enemy_text)
        win.addstr(2, 0, "O que deseja fazer?")
        win.addstr(3, 0, "1. Atacar")
        win.addstr(4, 0, "2. Defender")
        win.addstr(5, 0, "3. Fugir")
        win.refresh()
        opt = win.getch()
        win.addstr(9, 0, f"Key pressed: {opt}")

        if opt == ord('1'):
            win.addstr(8, 0, "You attacked")
        elif opt == ord('2'):
            win.addstr(9, 0, "You defended")
        if opt == ord('3'):
            win.addstr(10, 0, "You fled")
            break
        else:
            win.addstr(11, 0, "Invalid input, choose 1, 2, or 3.")

        win.refresh()
        win.getch()

player = Player(name="Dargia", hp=100, atk=20, crit_chance=0.4, crit_damage=2.0)
enemy = Enemy(name="Goblin", hp=100, atk=20, crit_chance=0.4, crit_damage=2.0)


if __name__ == "__main__":
    curses.wrapper(combat, player, enemy)
    

