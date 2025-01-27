import curses
from Interface import shop
from Interface import map_module

def village(window, player):
    village_ascii = [
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
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                       M - Mapa                                         ",
    ]
    # Limpar tela
    window.clear()
    window.box()

    # Altura e largura da tela
    height, width = window.getmaxyx()

    start_y = (height - len(village_ascii)) // 2
    start_x = (width - len(village_ascii[0])) // 2

    # Desenhar vila
    for i, line in enumerate(village_ascii):
        window.addstr(start_y + i, start_x, line)

    window.refresh()

    # Loop para capturar teclas
    while True:
        key = window.getch()

        if key == ord('1'):
            # Chama loja de armas
            shop.village_menu(player)
            # Redesenhar vila após retornar da loja
            window.clear()
            for i, line in enumerate(village_ascii):
                window.addstr(start_y + i, start_x, line)
            window.refresh()
        
        elif key == ord('2'):
            # Chama loja de armaduras
            shop.village_menu(player)
            # Redesenhar vila após retornar da loja
            window.clear()
            for i, line in enumerate(village_ascii):
                window.addstr(start_y + i, start_x, line)
            window.refresh()
        
        elif key == ord('3'):
            # Chama loja de poções
            shop.village_menu(player)
            # Redesenhar vila após retornar da loja
            window.clear()
            for i, line in enumerate(village_ascii):
                window.addstr(start_y + i, start_x, line)
            window.refresh()
        
        elif key == ord('m') or key == ord('M'):
            window.clear()
            window.box()
            return True
        
        elif key == ord('q') or key == ord('Q'):
            return 'village'