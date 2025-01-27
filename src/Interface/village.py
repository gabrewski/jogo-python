import curses
from Interface import shop
from Interface import map_module

def village(window, player, update_inv):
    village_ascii = [
        "                                                                                        ",
        "                                                                                        ",
        "                                 « VILA DO ALVORECER »                                  ",
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
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                                                                        ",
        "                                       M - Mapa                                         "
    ]
    # Limpar tela
    window.clear()
    window.box()

    # Altura e largura da tela
    height, width = window.getmaxyx()

    start_y = (height - len(village_ascii)) // 2
    start_x = (width - len(village_ascii[0])) // 2

    while True:
        window.clear()
        window.box()
        
        for i, line in enumerate(village_ascii):
            window.addstr(start_y + i, start_x, line)
        
        window.refresh()
        
        key = window.getch()

        if key == ord('1'):
            shop.open_weapon_shop(window, player, update_inv)  # Ajuste o player_level conforme necessário
        elif key == ord('2'):
            shop.open_armor_shop(window, player, update_inv)
        elif key == ord('3'):
            shop.open_potion_shop(window, player, update_inv)
        elif key == ord('m') or key == ord('M'):
            return True
