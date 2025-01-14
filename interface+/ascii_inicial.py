import curses
from curses import wrapper
import time

# setando cores
def main(stdscr):
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

    curses.curs_set(0) # esconde o cursor

    # nome do jogo em ASCII
    title_ascii = [
        "                        █████                                                   ",
        "                      █████████                                                 ",
        "                     ███████████                                                ",
        "                    █████████████                                               ",
        "                   ███████████████                                              ",
        "                   █████████     █                                              ",
        "                  █████████                                                     ",
        "                  █████████                                                     ",
        "                  █████████                                                     ",
        "                  █████████                                                     ",
        "                  █████████                                                     ",
        "                   █████████     █                                              ",
        "                   ███████████████                                              ",
        "                    █████████████                                               ",
        "                     ███████████                                                ",
        "                      █████████                                                 ",
        "                        █████                                                   ",
        "                                               █                                ",
        "                                             .███.                              ",
        "                                            •█████•                             ",
        "                                          •█████████•                           ",
        "         ▌                                  ▪█████▪                ▌            ",
        "       .███.                              .█████████.            .███.          ",
        "      •█████•                            •███████████•          •█████•         ",
        "    •█████████•                         •█████████████•       •█████████•       ",
        "      ▪█████▪                             ▪██████████▪          ▪█████▪         ",
        "     .███████.                          .█████████████.        .███████.        ",
        "    •█████████•                 █▌     •████████████████•     •█████████•       ",
        " •██████████████•             .███▌.  •██████████████████•  •██████████████•    ",
        "     ▪███████▪               •██████•     ▪█████████▪          ▪███████▪        ",
        "    .█████████.       █    •█████████•  .█████████████.       .█████████.       ",
        "  •█████████████•   .███.     ▪████▪   •████████████████•   •█████████████•     ",
        "•██████████████████•██████•  •██████• •██████████████████••██████████████████•  ",
        "        ███       •████████•██████████•       ███                 ███           ",
        "        ███           ██       ███            ███                 ███           ",
        "        ███           ██       ███            ███                 ███           "
        ]
    # dimensões da tela
    height, width = stdscr.getmaxyx()

    # criar pad com o tamanho certo do texto
    pad_height = len(title_ascii) + 2
    pad_width = len(title_ascii[0]) + 2
    pad = curses.newpad(pad_height, pad_width)
    
    for i, line in enumerate(title_ascii):
        pad.addstr(i, 0, line, YELLOW)

    # calcular centro
    start_y = (height - len(title_ascii)) // 2
    start_x = (width - len(title_ascii[0])) // 2

    # loop de exibição
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        #posicionamento
        pad.refresh(0, # linha (conteudo)
                    0, # coluna (conteudo)
                    start_y, # linha inicial (tela)
                    start_x, # coluna inicial (tela)
                    start_y + len(title_ascii) + 1, #  linha final (tela)
                    start_x + len(title_ascii[0]) + 1) # colunha final (tela)
        time.sleep(0.2)
    stdscr.getch()

wrapper(main)