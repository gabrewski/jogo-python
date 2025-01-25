#animação_titulo.py

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
    title_ascii1 = [
        "▄▄▄▄▄ ▄· ▄▌ ▄▄▄·▄▄▄ .    .▄▄ ·       • ▌ ▄ ·. ▄▄▄ .▄▄▄▄▄ ▄ .▄▪   ▐ ▄  ▄▄ • ",
        "•██  ▐█▪██▌▐█ ▄█▀▄.▀·    ▐█ ▀. ▪     ·██ ▐███▪▀▄.▀·•██  ██▪▐███ •█▌▐█▐█ ▀ ▪",
        " ▐█.▪▐█▌▐█▪ ██▀·▐▀▀▪▄    ▄▀▀▀█▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄ ▐█.▪██▀▐█▐█·▐█▐▐▌▄█ ▀█▄",
        " ▐█▌· ▐█▀·.▐█▪·•▐█▄▄▌    ▐█▄▪▐█▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌ ▐█▌·██▌▐▀▐█▌██▐█▌▐█▄▪▐█",
        " ▀▀▀   ▀ • .▀    ▀▀▀      ▀▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀ ▀▀▀ ·▀▀▀▀▀ █▪·▀▀▀▀ "
    ]

    # segundo texto ASCII
    title_ascii2 = [
        "1 ➣ Novo jogo",
        "     2 ➣ Continuar",
        "          3 ➣ Créditos",
        "               4 ➣ Sair"
    ]

    # obter dimensões da tela
    height, width = stdscr.getmaxyx()
    
    # criar pads
    pad1 = curses.newpad(len(title_ascii1) + 1, len(title_ascii1[0]) + 1)
    pad2 = curses.newpad(len(title_ascii2) + 1, len(title_ascii2[0]) + 1)
    
    # adicionar os textos ASCII aos pads
    for i, line in enumerate(title_ascii1):
        pad1.addstr(i, 0, line, YELLOW)
    for i, line in enumerate(title_ascii2):
        pad2.addstr(i, 0, line, CYAN)

    # calcular posições finais (centro da tela)
    final_y1 = max(0, (height - len(title_ascii1)) // 2 - 4)  # primeiro texto fica um pouco acima
    final_y2 = final_y1 + len(title_ascii1) + 2  # segundo texto fica abaixo do primeiro
    start_x1 = max(0, (width - len(title_ascii1[0])) // 2)
    start_x2 = max(0, (width - len(title_ascii2[0])) // 2)

    # começar da parte inferior da tela
    current_y1 = height
    current_y2 = height + 6  # começa um pouco depois do primeiro
    
    try:
        # movimento suave para cima dos dois textos
        while current_y2 > final_y2:
            stdscr.clear()
            stdscr.refresh()
            
            # atualizar primeiro pad se ainda estiver em movimento
            if current_y1 > final_y1:
                screen_start_y1 = max(0, int(current_y1))
                screen_end_y1 = min(height - 1, screen_start_y1 + len(title_ascii1))
                screen_end_x1 = min(width - 1, start_x1 + len(title_ascii1[0]))
                
                try:
                    pad1.refresh(0, 0, screen_start_y1, start_x1, screen_end_y1, screen_end_x1)
                except curses.error:
                    pass

                current_y1 -= 0.5
            else:
                # manter primeiro pad na posição final
                try:
                    pad1.refresh(0, 0, final_y1, start_x1,
                               min(height - 1, final_y1 + len(title_ascii1)),
                               min(width - 1, start_x1 + len(title_ascii1[0])))
                except curses.error:
                    pass

            # atualizar segundo pad
            screen_start_y2 = max(0, int(current_y2))
            screen_end_y2 = min(height - 1, screen_start_y2 + len(title_ascii2))
            screen_end_x2 = min(width - 1, start_x2 + len(title_ascii2[0]))
            
            try:
                pad2.refresh(0, 0, screen_start_y2, start_x2, screen_end_y2, screen_end_x2)
            except curses.error:
                pass

            current_y2 -= 0.5
            time.sleep(0.2)

        # manter os textos na posição final
        while True:
            try:
                pad1.refresh(0, 0, final_y1, start_x1,
                           min(height - 1, final_y1 + len(title_ascii1)),
                           min(width - 1, start_x1 + len(title_ascii1[0])))
                pad2.refresh(0, 0, final_y2, start_x2,
                           min(height - 1, final_y2 + len(title_ascii2)),
                           min(width - 1, start_x2 + len(title_ascii2[0])))
            except curses.error:
                pass
                
            # verificar se uma tecla foi pressionada
            key = stdscr.getch()
            if key != -1:
                break
            time.sleep(0.02)
            
    except KeyboardInterrupt:
        pass

wrapper(main)
