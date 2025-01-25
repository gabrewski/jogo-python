import curses
from map_module import show_map
from character import Player
from save_load import SaveLoadSystem

# fazer os imports aqui
# Importar os coisos do jogador (nome e level) do sistema de progresso
# Importar os coiso de mapa aleatório
# Importar os itens do sistema de inventário
# Importar o combate

class GameInterface:
    def __init__(self, stdscr):
        # inicializa o sistema de progressão
        self.stdscr = stdscr
        curses.start_color()
        curses.use_default_colors()
        curses.curs_set(0)
        
        # configuração de cores
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        self.BLUE = curses.color_pair(1)
        self.CYAN = curses.color_pair(2)
        self.GREEN = curses.color_pair(3)
        self.MAGENTA = curses.color_pair(4)
        self.RED = curses.color_pair(5)
        self.WHITE = curses.color_pair(6)
        self.YELLOW = curses.color_pair(7)
        
        self.setup_windows()
        self.refresh_all()
        
    # DESENHANDO OS QUADRADINHOS E PAH
    def setup_windows(self):
        self.max_y, self.max_x = self.stdscr.getmaxyx()
        
        # Área principal do jogo (70% da largura)
        game_width = int(self.max_x * 0.75)
        game_height = self.max_y - 7    # Altura total menos área de comandos
        self.game_win = curses.newwin(game_height, game_width, 0, 0)
        
         # Largura dos painéis laterais
        side_width = self.max_x - game_width
        
        # Informações do personagem (nome, level e HP)
        self.char_win = curses.newwin(5, side_width, 0, game_width)

        # Status do personagem
        self.stats_win = curses.newwin(6, side_width, 5, game_width)

        # Inventário (área vertical menos os comandos)
        inv_height = self.max_y - 18
        self.inv_win = curses.newwin(inv_height, side_width, 11, game_width)

        # Área de comandos
        cmd_y = self.max_y - 7
        self.cmd_win = curses.newwin(7, side_width, cmd_y, game_width)

        # Área de narração (mesma largura da área do jogo)
        self.txt_win = curses.newwin(7, game_width, game_height, 0)
        
        self.draw_borders()
    
    def draw_borders(self):
        for win in [self.game_win, self.char_win, self.stats_win, self.inv_win, self.txt_win]:
            win.box()
    
    def refresh_all(self):
        self.stdscr.refresh()
        self.game_win.refresh()
        self.char_win.refresh()
        self.stats_win.refresh()
        self.inv_win.refresh()
        self.cmd_win.refresh()
        self.txt_win.refresh()
    
    #ATUALIZAÇÕES DE INFORMAÇÕES
    def update_game_area(self, game_map=None):
        # Atualiza a área principal do jogo
        self.game_win.clear()
        self.game_win.box()

        # Por enquanto, apenas um exemplo
        self.game_win.addstr(2, 3, "começa na vila")
        self.game_win.refresh()

    def update_character(self, name="Hero", level=1, exp=0, level_exp=100):
        # Atualiza informações do personagem
        self.char_win.clear()
        self.char_win.box()
        self.char_win.addstr(1, 2, f"Name: {name}")
        self.char_win.addstr(2, 2, f"Level: {level}")
        
        # valores dinâmicos para a barra de experiência
        exp_bar = int((exp / level_exp) * 10)   # barra de xp com 10 blocos
        exp_display = f"EXP: {'█' * exp_bar}{'─' * (10 - exp_bar)} {exp}/{level_exp}"
        self.char_win.addstr(3, 2, exp_display)
        
        self.char_win.refresh()

    # sistema de progressao do leo
    def update_stats(self, player):
        # atualiza status do personagem
        self.stats_win.clear()
        self.stats_win.box()
        
        # valores dinâmicos para a barra de HP
        hp_bar = int((player.hp / player.hp_max) * 10)
        hp_display = f"HP: "
        
        # determina a cor da barra de HP baseado na porcentagem de vida
        if player.hp / player.hp_max >= 0.5:
            color = self.GREEN    # verde quando a vida esta acima de 50%
        elif player.hp / player.hp_max >= 0.25:
            color = self.YELLOW   # amarelo quando a vida esta acima de 25%
        else:
            color = self.RED   # vermelho quando a vida esta abaixo de 25%
        
        self.stats_win.addstr(1, 2, hp_display)
        self.stats_win.addstr(1, 6, f"{'█' * hp_bar}{'─' * (10 - hp_bar)} {player.hp}/{player.hp_max}", color)
        
        # stats do personagem
        stats = [
            f"ATK: {player.atk + player.weapon.atk_value if player.weapon else player.atk}",
            f"DEF: {player.armor.def_value if player.armor else 0}",
        ]
        

        # atualiza a janela de status
        for i, stat in enumerate(stats, 2):
            self.stats_win.addstr(i, 2, stat)
        self.stats_win.refresh()

    def update_inventory(self, inventory=None):
        # atualiza o inventario
        self.inv_win.clear()
        self.inv_win.box()
        self.inv_win.addstr(1, 2, "Inventory:")
        
        # Por enquanto, itens de exemplo, tem que pegar do inventario
        items = ["Health Potion", "Iron Sword", "Leather Armor", "Magic Ring"]
        
        for i, item in enumerate(items, 2):
            self.inv_win.addstr(i, 2, f"- {item}")
        self.inv_win.refresh()
    
    def update_commands(self):
        # atualiza a área dos comandos
        self.cmd_win.clear()
        self.cmd_win.box()
        commands = [
            "    W         ↑    | P - Pause    ",
            "                   | Q - Quit     ",
            " A  S  D   ←  ↓  → | I - Inventory",
            "                   | M - Map      ",
            "       Move        | ↲ - Confirm  "
            ]
        for i, command in enumerate(commands, 1):
            self.cmd_win.addstr(i, 2, command)
            
        self.cmd_win.refresh()

    def update_pause_menu(self):
        # atualiza o menu de pause
        self.cmd_win.clear()
        self.cmd_win.box()
        pause_menu = [
            " P - Voltar       ",
            " S - Salvar e sair"
        ]
        for i, option in enumerate(pause_menu, 1):
            self.cmd_win.addstr(i, 2, option)
        self.cmd_win.refresh()

    def update_text(self):
        """Atualiza a área de narração"""
        self.txt_win.clear()
        self.txt_win.box()

        # Por enquanto, apenas um exemplo
        self.txt_win.addstr(1, 1, "Narração")
        self.txt_win.refresh()        

    # COISAS ACONTECENDO 
    def show_world_map(self):
        """Mostra o mapa do mundo na área principal do jogo"""
        selected_area = show_map(self.game_win)
        self.game_win.refresh()
        return selected_area

def main(stdscr):
    # Verifica tamanho mínimo do terminal
    height, width = stdscr.getmaxyx()
    if height < 24 or width < 80:
        stdscr.addstr(0, 0, "Terminal muito pequeno! Precisa ser pelo menos 80x24")
        stdscr.refresh()
        stdscr.getch()
        return
    
    stdscr.clear()
    stdscr.refresh()
    
    # Inicializa a interface
    interface = GameInterface(stdscr)

    # inicializar os outros módulos? talvez fique tudo igual eu coloquei o mapa
    # player = Player("Hero", 1)
    # world = World()
    # inventory = Inventory()
    # sei lá, algo assim

    # Inicializa o jogador
    player = Player("Hero", 100, 10, 0.1, 1.5)      # os valores são respectivamente: hp inicial, atk inicial, chance de critico e multiplicador de critico

    # Inicializa o sistema de save/load
    save_load_system = SaveLoadSystem("savefile.txt")

    # Atualiza todas as áreas
    interface.update_game_area()
    interface.update_character()
    interface.update_stats(player)
    interface.update_inventory()
    interface.update_commands()
    interface.update_text()
    
    paused = False

    # Loop principal
    while True:
        try:
            key = stdscr.getch()
            
            if key == ord('q'):
                break

            # o menu muda para o de Pause, ainda precisa ver se vai adicionar mais opções
            elif key == ord('p') or key == ord('P'):
                paused = not paused
                if paused:
                    interface.update_pause_menu()
                else:
                    interface.update_commands()

            elif paused:
                # salva o jogo
                if key == ord('s') or key == ord('S'):
                    save_load_system.save_game(player, player.inventory)
                    interface.cmd_win.addstr(5, 2, "Jogo salvo. Pressione qualquer tecla.")
                    interface.cmd_win.refresh()
                    stdscr.getch()  # espera por uma tecla
                    paused = False
                    interface.update_commands()
                elif key == ord('p') or key == ord('P'):
                    paused = False
                    interface.update_commands()

            else:
                if key == ord('m') or key == ord('M'):
                    selected_area = interface.show_world_map()

                    #talvez tenha que mudar pq vão ter outras partes que vão ser com número, tipo o menu principal ou o combate, veremos
                    if selected_area == 1:
                        # carregar montanha
                        interface.update_game_area()

                    elif selected_area == 2:
                        # carregar floresta
                        interface.update_game_area()

                    elif selected_area == 3:
                        # carregar planícies
                        interface.update_game_area()

                    elif selected_area == 4:
                        # carregar água
                        interface.update_game_area()

                    elif selected_area == 5:
                        # carregar deserto
                        interface.update_game_area()

                    elif selected_area == 6:
                        # carregar magma
                        interface.update_game_area()

                    else:   # selected_area == 7 ou inválido
                        interface.update_game_area()

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except curses.error as e:
        print(f"Erro ao inicializar curses: {e}")
        curses.endwin()
