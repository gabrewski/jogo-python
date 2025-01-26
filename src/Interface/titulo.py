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

def exibir_menu(stdscr):
    # Limpar a tela
    stdscr.clear()
    
    # Posição inicial para centralizar o título
    altura, largura = stdscr.getmaxyx()
    inicio_y = (altura // 2) - (len(title) // 2)
    
    # Exibe o título
    for i, linha in enumerate(title):
        inicio_x = (largura // 2) - (len(linha) // 2)  # Centraliza horizontalmente
        stdscr.addstr(inicio_y + i, inicio_x, linha)  # Adiciona cada linha na posição correta
    
    # Exibe as opções de menu
    menu_inicio_y = inicio_y + len(title) + 2  # Espaço abaixo do título
    for i, option in enumerate(options):
        inicio_x = (largura // 2) - (len(option) // 2)  # Centraliza horizontalmente
        stdscr.addstr(menu_inicio_y + i, inicio_x, option)  # Adiciona cada opção no menu
    
    # Atualiza a tela
    stdscr.refresh()
    
    # Aguardando a seleção do menu
    while True:
        key = stdscr.getch()

        # Se pressionar '1', '2', '3' ou '4', escolha do usuário
        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr("Novo jogo selecionado!\n")
            stdscr.refresh()
            stdscr.getch()
            break
        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr("Continuar selecionado!\n")
            stdscr.refresh()
            stdscr.getch()
            break
        elif key == ord('3'):
            stdscr.clear()
            stdscr.addstr("Saindo do jogo...\n")
            stdscr.refresh()
            stdscr.getch()
            break
        elif key == 27:  # ESC para sair
            break
    return key
# Inicializa o curses
curses.wrapper(exibir_menu)
