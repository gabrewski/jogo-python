import curses
from Interface.main import start_interface


def story(stdscr, player):
    # setando cores
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

    # artezinha
    ascii = [
        "                        █████          ˚       *                 *      ✦ ˚     ",
        "        .   *         █████████                              .                  ",
        "                     ███████████             ˚        ₊         ⡀    ₊    .     ",
        "             ₊      █████████████                           ✦          ˚        ",
        "    ✦              ███████████████                 .            *               ",
        "                   █████████     █          ˚          ˚   ˚          ₊         ",
        "         ⡀        █████████           ✦         ₊                .        ₊     ",
        "             .    █████████                  .       *         ₊                ",
        "                  █████████                    ˚          ⡀               ˚     ",
        " ⡀        ₊     ˚ █████████            *  ₊            ✦                        ",
        "       .          █████████        ˚            *              .                ",
        "           *       █████████     █                 ˚                            ",
        "    ˚       ˚      ███████████████     ✦      *                        *    .   ",
        "  *     ✦        ₊  █████████████         ₊            ⡀                        ",
        "              ˚      ███████████     ˚                                          ",
        "   ₊        .         █████████ *              .                      .         ",
        " ˚     .       *        █████                                                   ",
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
        "        ███           ██        ███           ███                 ███           ",
        "        ███           ██        ███           ███                 ███           "
        ]
    
    phrases1 = [
        ("Peregrino↲", WHITE),
        ("Um chamado distante ecoa em sua mente.", YELLOW),
        ("Peregrino, acorde, peregrino.", WHITE),
        ("O brilho prateado da Lua banha sua pele, trazendo uma sensação de urgência.", YELLOW),
        ("Você abre os olhos.", YELLOW)
    ]
    
    phrases2 = [
        ("Finalmente, você despertou.", WHITE),
        ("Você, Peregrino, foi escolhido para enfrentar a escuridão que assola esta terra.", WHITE),
        ("Escolhido? Eu sou apenas... um viajante.", CYAN),
        ("Sim, exatamente. Há um feitiço sob os moradores da vila.", WHITE),
        ("O (nome do final boss) os amaldiçoou, tirando sua força de vontade e coragem, para que eles não consigam se opor a ele.", WHITE),
        ("Você é um visitante, Peregrino. A maldição dele não toca naqueles que vêm de fora.", WHITE),
        ("Não será uma jornada fácil. Ele é protegido por monstros e lacaios que infestam esta terra.", WHITE),
        ("Fortaleça-se. Encontre equipamentos que o tornarão capazes de enfrentar a força do (boss).", WHITE)
    ]

    # Dimensões da tela
    height, width = stdscr.getmaxyx()

    # Efeito de typewriter
    def typewriter_effect(stdscr, text, color, height, width):
        # Limpa área de texto
        stdscr.addstr(height - 2, 0, " " * width)
        
        # Posição inicial do texto
        start_text_x = (width - len(text)) // 2
        
        # Renderiza texto caractere por caractere
        for i in range(len(text) + 1):
            stdscr.addstr(height - 2, start_text_x, text[:i], color)
            stdscr.refresh()
            curses.napms(50)  # Pausa de 50 milissegundos entre caracteres
        
        # Aguarda ENTER
        while True:
            key = stdscr.getch()
            if key == 10 or key == 13:  # Códigos para ENTER
                break

    # Primeira função de exibição de texto (sem arte ASCII)
    def display_text(phrases):
        for text, color in phrases:
            typewriter_effect(stdscr, text, color, height, width)

    # Exibir primeira sequência de frases
    display_text(phrases1)

    # Preparar arte ASCII
    pad_height = len(ascii) + 2
    pad_width = len(ascii[0]) + 2
    pad = curses.newpad(pad_height, pad_width)
    
    # cor ascii
    for i, line in enumerate(ascii):
        if i < 17:  # Primeira seção em amarelo
            pad.addstr(i, 0, line, WHITE)
        else:  # Próxima seção em verde
            pad.addstr(i, 0, line, GREEN)

    # Centralizar horizontalmente e no fundo da tela
    start_x = (width - len(ascii[0])) // 2
    start_y = height - len(ascii) - 2

    # Exibir arte ASCII
    pad.refresh(0, 0, start_y, start_x, 
                start_y + len(ascii) + 1, 
                start_x + len(ascii[0]) + 1)
    
    # Aguardar entrada
    stdscr.getch()

    # Segunda função para exibir texto com arte ASCII preservada
    def display_text_with_ascii(phrases, pad, start_y, start_x):
        for text, color in phrases:
            # Limpa área de texto
            stdscr.addstr(height - 2, 0, " " * width)
            
            # Reexibe arte ASCII
            pad.refresh(0, 0, start_y, start_x, 
                        start_y + len(ascii) + 1, 
                        start_x + len(ascii[0]) + 1)
            
            # Renderiza texto caractere por caractere
            start_text_x = (width - len(text)) // 2
            for i in range(len(text) + 1):
                stdscr.addstr(height - 2, start_text_x, text[:i], color)
                stdscr.refresh()
                curses.napms(50)  # Pausa de 50 milissegundos entre caracteres

            # Aguarda ENTER
            while True:
                key = stdscr.getch()
                if key == 10 or key == 13:  # Códigos para ENTER
                    break

    # Exibir segunda sequência de frases
    display_text_with_ascii(phrases2, pad, start_y, start_x)

    # Aguardar saída
    stdscr.getch()

    start_interface(stdscr, player)
