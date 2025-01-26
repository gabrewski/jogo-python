import curses

# Arte ASCII do título
title = [
    " _______                             _______ _                                     _      ",
    "(_______)                           (_______) |                          _        (_)     ",
    "    _ _____  ____ ____ _____  ___    _____  | | _____ ____  _____ ____ _| |_ _____ _  ___ ",
    "   | | ___ |/ ___) ___|____ |/___)  |  ___) | || ___ |    \\| ___ |  _ (_   _|____ | |/___)",
    "   | | ____| |  | |   / ___ |___ |  | |_____| || ____| | | | ____| | | || |_/ ___ | |___ |",
    "   |_|_____)_|  |_|   \\_____(___/   |_______)\\_)_____)_|_|_|_____)_| |_| \\__)_____|_(___/ ",
    "                                                                                          "
]

# Opções do menu
options = [
    "1 ➣ Novo jogo",
    "2 ➣ Continuar",
    "3 ➣ Sair"
]

# titulo.py
def exibir_menu(stdscr):
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()
    inicio_y = (altura // 2) - (len(title) // 2)
    
    # Exibir título
    for i, linha in enumerate(title):
        inicio_x = (largura // 2) - (len(linha) // 2)
        stdscr.addstr(inicio_y + i, inicio_x, linha)
    
    # Exibir opções
    menu_inicio_y = inicio_y + len(title) + 2
    for i, option in enumerate(options):
        inicio_x = (largura // 2) - (len(option) // 2)
        stdscr.addstr(menu_inicio_y + i, inicio_x, option)
    
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        if key in [ord('1'), ord('2'), ord('3'), 27]:
            return key  # Return immediately without extra messages

