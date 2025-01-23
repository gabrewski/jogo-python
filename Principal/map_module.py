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
        "_______________________________________________________________________________≈≈≈≈≈_____",
        "_______________________________________________________________≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈_______",
        "___________________________________________________________≈≈≈______≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈______",
        "____________________________________________________________≈≈≈__≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈_____",
        "__________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈_______",
        "_____________∼∼______∼∼∼∼∼∼∼____∼∼∼___________≈≈≈≈______≈≈≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈__♣_",
        "__________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼______∼∼∼____≈≈≈≈__♣♣♣♣♣♣____________≈≈≈≈≈≈≈≈≈≈____♣♣♣__",
        "________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈______________♣♣♣♣♣♣________♣♣____♣♣♣♣____",
        "____________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈_______♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣_____♣♣♣♣_______",
        "________________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼______≈≈≈≈___♣♣_________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣________",
        "_______________∼∼∼∼________∼∼_____∼∼∼∼∼∼∼_____≈≈≈____________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣____",
        "________________________________________________≈≈≈≈____♣♣______♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣___",
        "__________________▲____________≈≈≈≈__________≈≈≈≈____________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣______",
        "_________________▲▲▲__▲______≈≈≈≈≈≈≈≈___≈≈≈≈≈≈≈≈_______________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣_____",
        "____________▲__▲▲▲▲▲▲▲▲▲______≈≈≈___≈≈≈≈≈≈____≈≈≈________________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣________",
        "___________▲▲▲▲▲▲▲▲▲__▲▲▲▲____________________≈≈≈≈≈_______♣♣♣♣♣♣♣_______♣♣♣♣♣♣♣♣♣♣♣______",
        "______________▲▲▲▲____▲▲_________________________≈≈≈≈_______________♣♣♣__________________",
        "_________________________________________≋≋≋______≈≈≈≈______________________▲_________▲__",
        "________________________≋≋≋≋____≋≋≋≋≋≋≋____________≈≈≈≈≈≈_________▲________▲▲▲___▲_______",
        "________________________≋≋≋≋≋≋≋≋≋≋≋___≋≋≋__________≈≈≈≈______________▲____▲▲▲▲▲_▲▲▲______",
        "_________________≋≋≋_____≋≋≋≋≋≋≋≋≋≋≋______≋≋________≈≈≈≈_______▲____▲▲▲__▲▲▲▲▲▲▲▲▲▲▲__▲__",
        "_______________________≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋____________≈≈≈≈≈________▲_▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲_",
        "___________________≋≋≋__≋≋≋≋≋≋≋≋______≋≋≋≋___________≈≈≈≈≈≈≈_______▲▲▲_________▲▲▲▲▲▲____",
        "_____________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈______▲▲▲__________▲▲___",
        "__________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈________________________",
        "_______________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈____________________",
        "_____________________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈___________",
    ]

    # Obter dimensões da tela
    max_y, max_x = window.getmaxyx()

    # limpar janela
    window.clear()
    window.box()    

    # posição do mapa
    start_y = 1
    start_x = (max_x - len(ascii_map[0])) // 2
  
    # Desenhar o mapa
    for y, line in enumerate(ascii_map):
        for x, char in enumerate(line):
            try:
                window.addch(y + start_y, x + start_x, char, TERRAIN_COLORS.get(char, curses.color_pair(6)))
            except curses.error:
                pass

    # legenda
    captions = [
        ("1. ⌂ - Vila do Alvorecer", curses.color_pair(7)),
        ("2. ♣ - Floresta dos Ecos", curses.color_pair(2)),
        ("3. ∼ - Dunas do Desolado", curses.color_pair(6)),
        ("4. ▲ - Terra Congelada", curses.color_pair(5)),
        ("5. ≈ - Pântano das Águas Místicas", curses.color_pair(1)),
        ("6. ≋ - Fornalha do Apocalipse", curses.color_pair(4)),
        ("7. a - Fortaleza de...", curses.color_pair(7))
    ]

    #configurações da legenda
    caption_y = start_y + len(ascii_map) - 2
    caption_x = start_x
    per_rows = 2 # 3 itens por linha

    # tamanho máximo da legenda
    max_lenght = max(len(text) for text in captions)
    column_width = max_lenght

    # desenhar legenda
    for i, (text, color) in enumerate(captions):
        row = i // per_rows
        col = i % per_rows

        pos_y = caption_y + row
        pos_x = caption_x + (col * column_width)

    # verificação de espaço
    if pos_y < max_y - 2 and pos_x + len(text) < max_x - 2:
        try:
            window.addstr(pos_y, pos_x, text, color)
        except curses.error:
            pass


    # Atualizar a janela
    window.refresh()

    # Aguardar input do usuário
    while True:
        try:
            key = window.getch()
            if key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7')]:
                return int(chr(key))
            elif key in [27, ord('q'), ord('Q')]:  # ESC ou Q para sair
                return 7  # Retorna como se tivesse selecionado "Return"
        except curses.error:
            continue
    
    return 0 
