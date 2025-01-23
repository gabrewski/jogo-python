import curses
from curses import wrapper
import time

def main(stdscr):
    # configuração de cores
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    BLUE = curses.color_pair(1)
    CYAN = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    MAGENTA = curses.color_pair(4)
    RED = curses.color_pair(5)
    WHITE = curses.color_pair(6)
    YELLOW = curses.color_pair(7)

    # esconder o cursor
    curses.curs_set(0)

    # primeiro texto ASCII
    title_ascii = [
        "▄▄▄▄ . ▄▄·       .▄▄ ·      ·▄▄▄▄   ▄▄▄·      ▄▄▌  ▄• ▄▌ ▄▄▄· ",
        "█▄.▀·▐█ ▌▪▪     ▐█ ▀.      ██▪ ██ ▐█ ▀█      ██•  █▪ █▌▐█ ▀█  ",
        "▐▀▀▪▄██ ▄▄ ▄█▀▄ ▄▀▀▀█▄     ▐█· ▐█▌▄█▀▀█      ██▪  █▌▐█▌▄█▀▀█  ",
        "▐█▄▄▌▐███▌▐█▌.▐▌▐█▄▪▐█     ██. ██ ▐█ ▪▐▌     ▐█▌▐▌▐█▄█▌▐█ ▪▐▌ ",
        " ▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀▀▀▀      ▀▀▀▀▀•  ▀  ▀      .▀▀▀  ▀▀▀  ▀  ▀  "
    ]

    # segundo texto ASCII
    menu_ascii = [
        "                                            ┳┓        •             ",
        "                                        1 ➣ ┃┃┏┓┓┏┏┓  ┓┏┓┏┓┏┓       ",
        "                                            ┛┗┗┛┗┛┗┛  ┃┗┛┗┫┗┛       ",
        "                                                      ┛   ┛         ",
        "                                                                    ",
        "                                                 ┏┓     •           ",
        "                                             2 ➣ ┃ ┏┓┏┓╋┓┏┓┓┏┏┓┏┓   ",
        "                                                 ┗┛┗┛┛┗┗┗┛┗┗┻┗┻┛    ",
        "                                                                    ",
        "                                                      ┏┓   / ┓•     ",
        "                                                  3 ➣ ┃ ┏┓┏┓┏┫┓╋┏┓┏ ",
        "                                                      ┗┛┛ ┗ ┗┻┗┗┗┛┛ ",
        "                                                                    ",
        "                                                           ┏┓  •    ",
        "                                                       4 ➣ ┗┓┏┓┓┏┓  ",
        "                                                           ┗┛┗┻┗┛   ",
    ]

    # obter dimensões da tela
    height, width = stdscr.getmaxyx()
    
    # criar pads
    pad1 = curses.newpad(len(title_ascii) + 1, len(title_ascii[0]) + 1)
    pad2 = curses.newpad(len(menu_ascii) + 1, len(menu_ascii[0]) + 1)
    
    # adicionar os textos ASCII aos pads
    for i, line in enumerate(title_ascii):
        pad1.addstr(i, 0, line, WHITE)
    
    # calcular posições finais (centro da tela)
    final_y1 = max(0, (height - len(title_ascii)) // 2 - 4)  # primeiro texto fica um pouco acima
    final_y2 = final_y1 + len(title_ascii) + 3  # segundo texto fica abaixo do primeiro
    start_x1 = max(0, (width - len(title_ascii[0])) // 2)
    start_x2 = max(0, (width - len(menu_ascii[0])) // 2)

    # começar da parte inferior da tela
    current_y1 = height
    
    try:
        # movimento suave para cima do título
        while current_y1 > final_y1:
            stdscr.clear()
            stdscr.refresh()
            
            screen_start_y1 = max(0, int(current_y1))
            screen_end_y1 = min(height - 1, screen_start_y1 + len(title_ascii))
            screen_end_x1 = min(width - 1, start_x1 + len(title_ascii[0]))
            
            try:
                pad1.refresh(0, 0, screen_start_y1, start_x1, screen_end_y1, screen_end_x1)
            except curses.error:
                pass

            current_y1 -= 0.5
            time.sleep(0.2)

        # Aguardar 1 segundos
        time.sleep(1)

        # Adicionar instrução de seleção
        instruction1 = " Pressione ENTER ↲ para continuar"
        instruction1_x = (width - len(instruction1)) // 2
        instruction1_y = final_y1 + len(title_ascii) + 1
        stdscr.addstr(instruction1_y, instruction1_x, instruction1, YELLOW)
        stdscr.refresh()

        # Aguardar pressionamento de ENTER
        while True:
            key = stdscr.getch()
            if key == 10:  # Código para tecla ENTER
                instruction2 = "Selecione uma opção para continuar"
                instruction2_x = (width - len(instruction2)) // 2
                instruction2_y = final_y1 + len(title_ascii) + 1
                stdscr.addstr(instruction2_y, instruction2_x, instruction2, YELLOW)
                stdscr.refresh()
                
                break

        # Adicionar menu
        for i, line in enumerate(menu_ascii):
            pad2.addstr(i, 0, line, CYAN)

        # Mostrar menu na posição final
        pad2.refresh(0, 0, final_y2, start_x2,
                     min(height - 1, final_y2 + len(menu_ascii)),
                     min(width - 1, start_x2 + len(menu_ascii[0])))
        stdscr.refresh()

        # Aguardar seleção
        while True:
            key = stdscr.getch()
            if key != -1:
                break

    except KeyboardInterrupt:
        pass

wrapper(main)
