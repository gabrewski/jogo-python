import curses
import shop

def display_village(stdscr, player_level):
    village_ascii = [
        "                                                                                        ",
        "                                                                                        ",
        "                                      ________                                          ",
        "                                     /--------\                                 (  )    ",
        "                                    /__________\                                ( )     ",
        "                                   /|          |\                               ()      ",
        "    _______       ________∥___      | []    [] |       ______     ______________∥______ ",
        "   /-------\     /------------\     |          |      /------\     |-----------------|  ",
        "  /_________\   /______________\    |2.Ferraria|     /3.Poção \    |  [ ]  [ ]  [ ]  |  ",
        " /|  ___ [] |\   | []     ___ |     |  ___     |    /|   ___  |\   |  _____          |  ",
        "  |  |`|    |    |1.Forja |´| |     |  |`|     |     |   |´|  |    |  |´  |   [0]    |  ",
        "__|__|_|____|____|________|_|_|_____|__|_|_____|_____|___|_|__|____|__|___|__________|__",
    ]
    # Limpar tela
    stdscr.clear()

    # Altura e largura da tela
    height, width = stdscr.getmaxyx()

    # Desenhar vila
    for i, line in enumerate(village_ascii):
        stdscr.addstr(i, (width - len(line)) // 2, line)

    # Opções do menu
    menu_options = [
        "1. Forja",
        "2. Ferraria", 
        "3. Poções",
        "0. Voltar"
    ]

    # Posicionar opções
    menu_start_y = len(village_ascii) + 2
    for i, option in enumerate(menu_options):
        stdscr.addstr(menu_start_y + i, (width - len(option)) // 2, option)

    stdscr.refresh()

    # Loop para capturar teclas
    while True:
        key = stdscr.getch()

        if key == ord('1'):
            # Chama loja de armas
            shop.village_menu(player_level)
            # Redesenhar vila após retornar da loja
            stdscr.clear()
            for i, line in enumerate(village_ascii):
                stdscr.addstr(i, (width - len(line)) // 2, line)
            for i, option in enumerate(menu_options):
                stdscr.addstr(menu_start_y + i, (width - len(option)) // 2, option)
            stdscr.refresh()
        
        elif key == ord('2'):
            # Chama loja de armaduras
            shop.village_menu(player_level)
            # Redesenhar vila após retornar da loja
            stdscr.clear()
            for i, line in enumerate(village_ascii):
                stdscr.addstr(i, (width - len(line)) // 2, line)
            for i, option in enumerate(menu_options):
                stdscr.addstr(menu_start_y + i, (width - len(option)) // 2, option)
            stdscr.refresh()
        
        elif key == ord('3'):
            # Chama loja de poções
            shop.village_menu(player_level)
            # Redesenhar vila após retornar da loja
            stdscr.clear()
            for i, line in enumerate(village_ascii):
                stdscr.addstr(i, (width - len(line)) // 2, line)
            for i, option in enumerate(menu_options):
                stdscr.addstr(menu_start_y + i, (width - len(option)) // 2, option)
            stdscr.refresh()
        
        elif key == ord('0'):
            break