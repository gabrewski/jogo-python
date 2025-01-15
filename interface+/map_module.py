import curses
from curses import wrapper
import time

def show_map(window):
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

    ascii_map = [
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
        "_______▲▲▲__▲______≈≈≈≈≈≈≈≈___≈≈≈≈≈≈≈≈_______________YYYYYYYYYYYYYYYYYYYYY_____",
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
    max_y, max_x = window.getmaxyx()

    # limpar janela
    window.clear()
    window.box()    

    # posição do mapa
    start_y = (max_y - len(ascii_map)) // 2
    start_x = 2
  
    # Desenhar o mapa
    for y, line in enumerate(ascii_map):
        for x, char in enumerate(line):
            try:
                window.addch(y + start_y, x + start_x, char, TERRAIN_COLORS.get(char, curses.color_pair(6)))
            except curses.error:
                pass

    # Adicionar legenda
    legend_y = start_y + 10
    legend_x = start_x + len(ascii_map[0]) + 2
    legends = [
        ("1. ▲ - Mountains", curses.color_pair(5)),
        ("2. Y - Forest", curses.color_pair(2)),
        ("3. _ - Plains", curses.color_pair(3)),
        ("4. ≈ - Water", curses.color_pair(1)),
        ("5. ∼ - Desert", curses.color_pair(6)),
        ("6. ≋ - Magma", curses.color_pair(4))
    ]

    # Verificar se há espaço suficiente para a legenda
    longest_legend = max(len(text) for text, _ in legends)
    if legend_x + longest_legend < max_x - 2:  # -2 para margem da borda
        for i, (text, color) in enumerate(legends):
            try:
                window.addstr(legend_y + i, legend_x, text, color)
            except curses.error:
                pass
    
    # Atualizar a janela
    window.refresh()

    # Aguardar input do usuário
    while True:
        try:
            key = window.getch()
            if key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6')]:
                return int(chr(key))
            elif key in [27, ord('q'), ord('Q')]:  # ESC ou Q para sair
                return 6  # Retorna como se tivesse selecionado "Return"
        except curses.error:
            continue
    
    return 0  # Retorno padrão se algo der errado
