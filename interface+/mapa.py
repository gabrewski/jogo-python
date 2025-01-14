import curses
from curses import wrapper
import time

def main(stdscr):
    # Configuração de cores
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    TERRAIN_COLORS = {
        '≈' : curses.color_pair(1), # lago/rio
        'Y' : curses.color_pair(2), # floresta
        '_' : curses.color_pair(3), # planicie
        '≋' : curses.color_pair(4), # magma
        '▲' : curses.color_pair(5), # montanha
        '∼' : curses.color_pair(6) # deserto
    }

    map_ascii = [
        "_____________________________________________________________________≈≈≈≈≈_____",
        "_____________________________________________________≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈_______",
        "_________________________________________________≈≈≈______≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈______",
        "________∼∼∼_______________________________________≈≈≈__≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈_____",
        "____________________________∼∼∼∼________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈_______",
        "___∼∼______∼∼∼∼∼∼∼____∼∼∼___________≈≈≈≈______≈≈≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈__Y_",
        "________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼_____________≈≈≈≈__YYYYYY____________≈≈≈≈≈≈≈≈≈≈____YYY__",
        "______∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈______________YYYYYY________YY____YYYY____",
        "__________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈_______YYYYYYYYYYYYYYYYY_____YYYY_______",
        "______________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼______≈≈≈≈___YY_________YYYYYYYYYYYYYYYYY________",
        "_____∼∼∼∼________∼∼_____∼∼∼∼∼∼∼_____≈≈≈____________YYYYYYYYYYYYYYYYYYYYYYYY____",
        "______________________________________≈≈≈≈____YY______YYYYYYYYYYYYYYYYYYYYYY___",
        "________▲____________≈≈≈≈__________≈≈≈≈____________YYYYYYYYYYYYYYYYYYYYYY______",
        "_______▲▲▲__▲______≈≈≈≈≈≈≈≈___≈≈≈≈≈≈≈≈________________YYYYYYYYYYYYYYYYYYYYY_____",
        "__▲__▲▲▲▲▲▲▲▲▲______≈≈≈___≈≈≈≈≈≈____≈≈≈________________YYYYYYYYYYYYYYYY________",
        "_▲▲▲▲▲▲▲▲▲__▲▲▲▲____________________≈≈≈≈≈_______YYYYYYY_______YYYYYYYYYYY______",
        "____▲▲▲▲____▲▲_________________________≈≈≈≈_______________YYY__________________",
        "________________________________________≈≈≈≈______________________▲_________▲__",
        "______________≋≋≋≋_______________________≈≈≈≈≈≈_________▲________▲▲▲___▲_______",
        "______________≋≋≋≋≋≋≋≋≋≋≋___≋≋≋__________≈≈≈≈______________▲____▲▲▲▲▲_▲▲▲______",
        "_______≋≋≋_____≋≋≋≋≋≋≋≋≋≋≋______≋≋________≈≈≈≈_______▲____▲▲▲__▲▲▲▲▲▲▲▲▲▲▲__▲__",
        "_____________≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋____________≈≈≈≈≈________▲_▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲_",
        "_________≋≋≋__≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋___________≈≈≈≈≈≈≈_______▲▲▲_________▲▲▲▲▲▲____",
        "______≋_______≋≋≋≋≋≋≋≋≋≋≋≋≋________________≈≈≈≈≈≈≈≈≈≈≈≈______▲▲▲__________▲▲___",
        "____________≋≋≋≋≋≋≋≋≋≋≋≋≋≋__≋≋≋_________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈________________________",
        "________________≋≋≋≋≋≋≋≋≋≋≋≋≋________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈____________________",
        "___________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈___________",
    ]

    # Obter dimensões da tela
    height, width = stdscr.getmaxyx()
    
    # Criar pad com tamanho suficiente para o texto ASCII
    pad_height = len(map_ascii) + 2  # Altura do texto + margem
    pad_width = len(map_ascii[0]) + 2  # Largura do texto + margem
    pad = curses.newpad(pad_height, pad_width)
    
    # Adicionar o texto ASCII ao pad
    for i, line in enumerate(map_ascii):
        for j, char in enumerate(line):
            pad.addstr(i, j, char, TERRAIN_COLORS.get(char, curses.color_pair(1)))

    # Calcular posição central
    start_y = (height - len(map_ascii)) // 2
    start_x = (width - len(map_ascii[0])) // 2

    # Loop de exibição
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        
        # Atualizar pad com posicionamento centralizado
        pad.refresh(0,  # pad starting line
                   0,  # pad starting column
                   start_y,  # screen starting line
                   start_x,  # screen starting column
                   start_y + len(map_ascii) + 1,  # screen ending line
                   start_x + len(map_ascii[0]) + 1)  # screen ending column

    stdscr.getch()

wrapper(main)